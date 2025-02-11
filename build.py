#!/usr/bin/env python3
from pathlib import Path
import subprocess
from ruamel.yaml import YAML
import shutil
import os

yaml = YAML()

DEMO_FOLDER = "demofiles"

def setup_talks():
    """
    Reads yaml file talks.yml and moves files and folders specified in yaml
    file to the a folder matching the name of the talk Args: talk_name: name
    of talk in talks.yml Note: yaml file is assumed to be a dict of dicts of
    lists and dict with the following python format:
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
        talks = yaml.load(stream)
    for talk_name in talks:
        Path(talk_name).mkdir(parents=True, exist_ok=True)

        if "files" in talks[talk_name]:
            for f in talks[talk_name]["files"]:
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

def setup_demofiles():
    print("creating demofolder")
    demo_folder = Path("demofiles")
    demo_folder.mkdir(parents=True, exist_ok=True)

    # list of repos used in demo
    print(f"cloning repos into demo folder {demo_folder}")
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
        target_path = demo_folder / Path(repo.split("/")[1])
        if not target_path.is_dir():
            subprocess.check_call([
                "git", "clone", "--depth", "1",
                f"https://github.com/{repo}.git"
            ], cwd=demo_folder)
    # This empty file and empty folder are for showing drag and drop in jupyterlab
    Path("move_this_file.txt").touch()
    Path("move_it_here").mkdir(exist_ok=True)

def main():
    setup_demofiles()
    setup_talks()


if __name__ == "__main__":
    main()