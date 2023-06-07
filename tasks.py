import json
import os
import re
from pathlib import Path
from subprocess import check_output
from invoke import task, Collection
from packaging.version import parse
from yaml import safe_load

from shutil import which
import shutil

env_name = "jupyterlab-demo"
demofolder = "demofiles"
source = "" if os.name == "nt" else "source"


def activate_path() -> str:
    conda_path = which("conda")
    return os.path.join(os.path.dirname(conda_path), os.path.pardir, "bin")


def rmdir(dirname):
    """Safely remove a directory, cross-platform"""
    if not os.path.exists(dirname):
        return
    if os.name == "nt":
        check_output("rmdir {0!s} /S /Q".format(dirname), shell=True)
    else:
        check_output(["rm", "-rf", dirname])


@task
def environment(ctx, clean=False, env_name=env_name):
    """
    Creates environment for demo
    Args:
    clean: deletes environment prior to reinstallation
    env_name: name of environment to install
    """
    if clean:
        print("deleting environment")
        path = os.environ.get("PATH")
        ctx.run(
            f"{source!s} deactivate; mamba remove -n {env_name!s} --all",
            env={"PATH": f"{activate_path()}:{path}"},
        )
    # Create a new environment
    print(f"creating environment {env_name!s}")
    ctx.run(
        f"mamba env update -f .binder/environment.yml -n {env_name!s} && mamba clean -yaf"
    )

    build(ctx, env_name=env_name)


@task
def build(ctx, env_name=env_name, kernel=True):
    """
    Builds an environment with appropriate kernels.
    """

    if kernel:
        path = os.environ.get("PATH")
        ctx.run(
            f"{source!s} activate {env_name!s} && ipython kernel install --name {env_name!s} --display-name {env_name!s} --sys-prefix",
            env={"PATH": f"{activate_path()}:{path}"},
        )


@task
def demofiles(ctx, clean=False, demofolder=demofolder):
    """
    Clones demofiles into demofolder
    Args:
    clean: deletes demofiles from demofolder prior to installation
    demofolder: name of demofolder
    """
    print("cleaning demofiles")
    if clean:
        rmdir(demofolder)

    print("creating demofolder")
    if not os.path.exists(demofolder):
        os.makedirs(demofolder)
    os.chdir(demofolder)

    # list of repos used in demo
    print(f"cloning repos into demo folder {demofolder}")
    reponames = [
        "jakevdp/PythonDataScienceHandbook",
        "swissnexSF/Urban-Data-Challenge",
        "altair-viz/altair",
        "QuantEcon/QuantEcon.notebooks",
        "theandygross/TCGA",
        "aymericdamien/TensorFlow-Examples",
        "bloomberg/bqplot",
    ]
    for repo in reponames:
        if not os.path.isdir(repo.split("/")[1]):
            ctx.run(f"git clone --depth 1 https://github.com/{repo!s}.git")
        assert os.path.isdir(repo.split("/")[1]), f"{repo!s} failed download"
    # This empty file and empty folder are for showing drag and drop in jupyterlab
    ctx.run("touch move_this_file.txt; mkdir move_it_here")


@task
def update(ctx, env_name=env_name):
    """Check for conda environment update and modify the environment file"""
    result = ctx.run(f"mamba update -qn {env_name!s} --json --dry-run --all")
    # clean the output
    from_ = result.stdout.find("{")
    to = result.stdout.rfind("}")
    data = json.loads(result.stdout[from_:to+1])

    if "error" in data:
        print(data["error"])
    elif "actions" in data:
        links = data["actions"].get("LINK", [])
        # Data structure in LINK
        #   List of dictionary. Example:
        # {
        #     "base_url": null,
        #     "build_number": 0,
        #     "build_string": "mkl",
        #     "channel": "defaults",
        #     "dist_name": "blas-1.0-mkl",
        #     "name": "blas",
        #     "platform": null,
        #     "version": "1.0"
        # }

        if links:
            environment = Path(".binder/environment.yml")
            raw_content = environment.read_text()
            env_content = safe_load(raw_content)
            dependencies = {}
            for dep in env_content["dependencies"]:
                if "=" in dep:
                    package, version = dep.split("=", maxsplit=1)
                    dependencies[package] = parse(version)
            new_content = raw_content
            has_update = False
            for link in links:
                name = link.get("name")
                if name in dependencies:
                    version = link["version"]
                    if parse(version) > dependencies[name]:
                        new_content = re.sub(f"- {name}={dependencies[name]!s}", f"- {name}={version}", new_content)
                        has_update = True
            
            if has_update:
                environment.write_text(new_content)


@task
def clean(ctx, env_name=env_name, demofolder=demofolder):
    """
    Deletes both environment and demofolder
    Args:
    env_name: name of conda environment
    demofolder: path to folder with demofiles
    """
    cmd = f"{source!s} deactivate && mamba remove --name {env_name!s} --all"
    path = os.environ.get("PATH")
    ctx.run(cmd, env={"PATH": f"{activate_path()}:{path}"})

    with open("talks.yml", "r") as stream:
        talks = safe_load(stream)
    for t in talks:
        rmdir(t)

    rmdir(demofolder)


@task
def r(ctx, env_name=env_name):
    """
    Installs the r kernel and associated libs.
    """
    path = os.environ.get("PATH")
    ctx.run(
        f"{source!s} activate {env_name!s} && mamba install -yc conda-forge -c nodefaults r-irkernel r-ggplot2",
        env={"PATH": f"{activate_path()}:{path}"},
    )


@task
def talk(ctx, talk_name, clean=False):
    """
      Reads yaml file talks.yml and
      moves files and folders specified
      in yaml file to the a folder
      matching the name of the talk
      Args:
      talk_name: name of talk in talks.yml
      Note: yaml file is assumed to be
      a dict of dicts of lists and
    dict with the following python format:
      {'talk_name':
          {'folders':
              {'src0': 'dest0', 'src1': 'dest1']
          'files':
              ['file0', file1']
       'rename':
        {'oldname': 'newname'}
          }
      }
      or in yaml format:
      talk_name:
          folders:
              src0: dest0
              src1: dest1
          files:
              - file0
              - file1
          rename:
              oldname: newname
    """
    with open("talks.yml", "r") as stream:
        talks = safe_load(stream)
    if clean:
        rmdir(talk_name)
    if not os.path.exists(talk_name):
        os.makedirs(talk_name)

    if "files" in talks[talk_name]:
        for f in talks[talk_name]["files"]:
            if (f.split("/")[0] == demofolder) and not os.path.exists(demofolder):
                demofiles(ctx)
                os.chdir("..")
            copied_path = os.path.join(talk_name, os.path.basename(f))
            shutil.copy(f, copied_path)
            assert os.path.isfile(copied_path), f"{f} failed to copy into {talk_name}"

    if "folders" in talks[talk_name]:
        for src, dst in talks[talk_name]["folders"].items():
            dst = os.path.join(talk_name, dst)
            if not os.path.exists(dst):
                shutil.copytree(src, dst)

    if "rename" in talks[talk_name]:
        for old_file, new_file in talks[talk_name]["rename"].items():
            moved_file = os.path.join(talk_name, os.path.basename(old_file))
            if os.path.isfile(moved_file):
                os.rename(moved_file, os.path.join(talk_name, new_file))
            elif os.path.isfile(old_file):
                shutil.copy(old_file, os.path.join(talk_name, new_file))


# Configure cross-platform settings.
ns = Collection(environment, build, demofiles, r, clean, update, talk)
ns.configure(
    {
        "run": {
            "shell": which("bash") if os.name != "nt" else which("cmd"),
            "pty": False if os.name == "nt" else True,
        }
    }
)
