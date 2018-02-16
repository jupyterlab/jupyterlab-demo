from __future__ import print_function
from invoke import task, Collection
import os
import yaml
from subprocess import check_output

from shutil import which
import shutil

env_name = 'jupyterlab-demo'
demofolder = 'demofiles'
source = '' if os.name == 'nt' else 'source'


def rmdir(dirname):
    """Safely remove a directory, cross-platform
    """
    if not os.path.exists(dirname):
        return
    if os.name == 'nt':
        check_output('rmdir {0!s} /S /Q'.format(dirname), shell=True)
    else:
        check_output(['rm', '-rf', dirname])


@task
def environment(ctx, clean=False, env_name=env_name):
    '''
    Creates environment for demo
    Args:
    clean: deletes environment prior to reinstallation
    env_name: name of environment to install
    '''
    if clean:
        print('deleting environment')
        ctx.run('{0!s} deactivate; conda remove -n {1!s} --all'.format(source, env_name))
    # Create a new environment
    print('creating environment {0!s}'.format(env_name))
    ctx.run("conda env create -f binder/environment.yml -n {0!s}".format(env_name))

    build(ctx, env_name=env_name)


@task
def build(ctx, env_name=env_name, kernel=True):
    '''
    Builds an environment with appropriate extensions.
    '''
    ctx.run("""
        {0!s} activate {1!s} &&
        jupyter labextension install @jupyterlab/fasta-extension@0.14 --no-build &&
        jupyter labextension install @jupyterlab/geojson-extension@0.14 --no-build &&
        jupyter labextension install @jupyterlab/google-drive@0.11 --no-build &&
        jupyter labextension install @jupyterlab/plotly-extension@0.14 --no-build &&
        jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.33 --no-build &&
        jupyter labextension install bqplot@0.3 --no-build &&
        jupyter lab clean && jupyter lab build
        """.format(source, env_name).strip().replace('\n', ''))
    if kernel:
        ctx.run("{0!s} activate {1!s} && ipython kernel install --name {1!s} --display-name {1!s} --sys-prefix".format(source, env_name))


@task
def demofiles(ctx, clean=False, demofolder=demofolder):
    '''
    Clones demofiles into demofolder
    Args:
    clean: deletes demofiles from demofolder prior to installation
    demofolder: name of demofolder
    '''
    print('cleaning demofiles')
    if clean:
        rmdir(demofolder)

    print('creating demofolder')
    if not os.path.exists(demofolder):
        os.makedirs(demofolder)
    os.chdir(demofolder)

    # list of repos used in demo
    print('cloning repos into demo folder {}'.format(demofolder))
    reponames = [
        'jakevdp/PythonDataScienceHandbook',
        'swissnexSF/Urban-Data-Challenge',
        'altair-viz/altair',
        'QuantEcon/QuantEcon.notebooks',
        'theandygross/TCGA',
        'aymericdamien/TensorFlow-Examples',
        'bloomberg/bqplot'
    ]
    for repo in reponames:
        if not os.path.isdir(repo.split('/')[1]):
            ctx.run('git clone --depth 1 https://github.com/{}.git'.format(repo))
        assert os.path.isdir(repo.split('/')[1]), '{} failed download'.format(repo)
    # This empty file and empty folder are for showing drag and drop in jupyterlab
    ctx.run('touch move_this_file.txt; mkdir move_it_here')


@task
def clean(ctx, env_name=env_name, demofolder=demofolder):
    '''
    Deletes both environment and demofolder
    Args:
    env_name: name of conda environment
    demofolder: path to folder with demofiles
    '''
    cmd = '{0!s} deactivate && conda remove --name {1!s} --all'
    ctx.run(cmd.format(source, env_name))

    with open("talks.yml", 'r') as stream:
        talks = yaml.load(stream)
    for t in talks:
        rmdir(t)

    rmdir(demofolder)


@task
def r(ctx, env_name=env_name):
    '''
    Installs the r kernel and associated libs.
    '''
    cmd = '{0!s} activate {1!s} && conda install -c conda-forge r-irkernel r-ggplot2'
    ctx.run(cmd.format(source, env_name))


@task
def talk(ctx, talk_name, clean=False):
    '''
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
    '''
    with open("talks.yml", 'r') as stream:
        talks = yaml.load(stream)
    if clean:
        rmdir(talk_name)
    if not os.path.exists(talk_name):
        os.makedirs(talk_name)

    if 'files' in talks[talk_name]:
        for f in talks[talk_name]['files']:
            if ((f.split('/')[0] == demofolder) and not
                    os.path.exists(demofolder)):
                demofiles(ctx)
                os.chdir('..')
            copied_path = os.path.join(talk_name, os.path.basename(f))
            shutil.copy(f, copied_path)
            assert os.path.isfile(copied_path), \
                '{} failed to copy into {}'.format(f, talk_name)

    if 'folders' in talks[talk_name]:
        for src, dst in talks[talk_name]['folders'].items():
            dst = os.path.join(talk_name, dst)
            if not os.path.exists(dst):
                shutil.copytree(src, dst)

    if 'rename' in talks[talk_name]:
        for old_file, new_file in talks[talk_name]['rename'].items():
            moved_file = os.path.join(talk_name, os.path.basename(old_file))
            if os.path.isfile(moved_file):
                os.rename(moved_file, os.path.join(talk_name, new_file))
            elif os.path.isfile(old_file):
                shutil.copy(old_file, os.path.join(talk_name, new_file))


# Configure cross-platform settings.
ns = Collection(environment, build, demofiles, r, clean, talk)
ns.configure({
    'run': {
        'shell': which('bash') if os.name != 'nt' else which('cmd'),
        'pty': False if os.name == 'nt' else True
    }
})
