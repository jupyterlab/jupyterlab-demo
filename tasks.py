from invoke import task, run

@task
def demofiles(ctx, clean=False):
	if clean:
		ctx.run('rm -rf demofiles')
	ctx.run('mkdir demofiles')
	ctx.run('cd demofiles; git clone https://github.com/jakevdp/PythonDataScienceHandbook.git')
	ctx.run('cd demofiles; git clone https://github.com/swissnexSF/Urban-Data-Challenge.git')
	ctx.run('cd demofiles; git clone https://github.com/altair-viz/altair.git')
	ctx.run('cd demofiles; git clone https://github.com/QuantEcon/QuantEcon.notebooks.git')
	ctx.run('cd demofiles; git clone https://github.com/theandygross/TCGA.git')
	ctx.run('cd demofiles; git clone https://github.com/aymericdamien/TensorFlow-Examples.git')

@task
def clean(ctx):
	ctx.run('rm -rf demofiles')