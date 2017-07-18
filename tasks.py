from __future__ import print_function
from invoke import task, run
import os

env_name = 'jupyterlab-demo'
demofolder = 'demofiles'

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
		ctx.run('source deactivate; conda remove -n {0!s} --all'.format(env_name))
	# Create a new environment
	print('creating environment {0!s}'.format(env_name))
	ctx.run("""
	    conda env create -f environment.yml -n {0!s};
		source activate {0!s};
		ipython kernel install --name {0!s} --display-name {0!s} --sys-prefix;
		jupyter labextension install @jupyterlab/google-drive@0.4.0 --no-build;
		jupyter labextension install @jupyterlab/geojson-extension@0.8.0 --no-build;
		jupyter labextension install @jupyterlab/json-extension@0.8.0 --no-build;
		jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.24.1 --no-build;
		jupyter labextension install bqplot-jupyterlab@0.4.0 --no-build;
		jupyter lab clean && jupyter lab build;
		""".format(env_name), pty=True)

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
		ctx.run('rm -rf {}'.format(demofolder))
	print('creating demofolder')
	ctx.run('mkdir {}'.format(demofolder))
	old_pwd = os.getcwd()
	os.chdir(demofolder)
	#list of repos used in demo
	print('cloning repos into demo folder {}'.format(demofolder))
	reponames = [
		'jakevdp/PythonDataScienceHandbook',
		'swissnexSF/Urban-Data-Challenge',
		'altair-viz/altair',
		'QuantEcon/QuantEcon.notebooks',
		'theandygross/TCGA',
		'aymericdamien/TensorFlow-Examples'
	]
	for repo in reponames:
		ctx.run('git clone https://github.com/{}.git'.format(repo))
		assert os.path.isdir(repo.split('/')[1]), '{} failed download'.format(repo)

@task
def clean(ctx, env_name=env_name, demofolder=demofolder):
	'''
	Deletes both environment and demofolder
	Args:
	env_name: name of conda environment
	demofolder: path to folder with demofiles
	'''
	ctx.run('source deactivate;\
		conda remove --name {0!s} --all;\
		rm -rf {1!s}'.format(env_name, demofolder))

@task
def scipy2017(ctx):
	# TODO: find a public licensed FASTA file, call it all.fasta,
	# (this is also used in Fasta.ipynb)

	files = {
		'big.csv': 'demofiles/urban-data-challenge/public-transportation/geneva/schedule-real-time.csv',
		'smaller.csv': 'demofiles/tcga/extra_data/c2.cp.v3.0.symbols_edit.csv',
		'vega.vl.json': 'demofiles/altair/altair/examples/json/field_spaces.vl.json',
		'notebook.ipynb': 'demofiles/pythondatasciencehandbook/notebooks/03.08-aggregation-and-grouping.ipynb',
		'iris.csv': 'data/iris.csv',
		'Messier106_NGC4217Feltoti1024.jpg': 'data/Messier106_NGC4217Feltoti1024.jpg',
		'Museums_in_DC.geojson': 'data/Museums_in_DC.geojson',
		'scipy2017.md': 'narrative/scipy2017.md'
	}
	ctx.run('mkdir -p scipy2017')
	for dest, source in files.items():
		ctx.run('cp {} scipy2017/{}'.format(source, dest))
