# JupyterLab Demonstration

[![Build Status](https://travis-ci.org/jupyterlab/jupyterlab-demo.svg?branch=master)](https://travis-ci.org/jupyterlab/jupyterlab-demo)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyterlab/jupyterlab-demo/master?urlpath=lab)

This repository contains some demonstrations of
[JupyterLab](https://github.com/jupyter/jupyterlab), the next
generation user interface of Project Jupyter.

## Installation

The demo requires [conda](https://conda.io/miniconda.html) and the package
 requirements are described in `environment.yml`

To install the environment and demofiles, we use [pyinvoke](http://pyinvoke.org). To install pyinvoke with conda call:
```bash
# add the conda forge channel.
conda config --add channels conda-forge --yes
```
```bash
conda install -c conda-forge invoke pyyaml
```

### Create the environment

To create the conda environment with all the dependencies and jupyterlab extensions for the demo, run:

```bash
invoke environment  # optionally --env-name=my-env-name
```

The default environment name is `jupyterlab-demo`.

To create the environment and remove previous installation, call:

```bash
invoke environment --clean
```

### Activate/deactivate the environment

To activate the conda environment, run:

```bash
source activate jupyterlab-demo
```

To deactivate the conda environment, run:

```bash
source deactivate
```

### Additional demo files

The demo includes files from a number of other repositories. To install these files,
run:

```bash
invoke demofiles
```

To remove demofiles and download again all:
```
invoke demofiles --clean
```

### R Language support

To add R language support, run:

```bash
invoke r
```

### Julia Language support

To add Julia language support follow the instructions [here](https://github.com/JuliaLang/IJulia.jl#installation).


### Uninstalling

To uninstall the demofiles and enviornment, call:

```
invoke clean
```

# Demo guide

The basic outline of the JupyterLab demo is described in the file `jupyterlab.md`.


# External Repositories

Our `invoke demofiles` clones repos from other authors.  The details of these repos are as follows:

| Name  | Author |License |
|---|---|---|
| PythonDataScienceHandbook/LICENSE-CODE  | Jake Vanderplas  | [MIT](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/LICENSE-CODE)|
| PythonDataScienceHandbook/LICENSE-TEXT   |  Jake Vanderplas | [CC-BY-NC-ND-3.0](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/LICENSE-TEXT) |
| altair   |  Jake Vanderplas | [BSD 3-clause](https://github.com/altair-viz/altair/blob/master/LICENSE) |
| Urban-Data-Challenge   |  [Data Canvas](http://datacanvas.org/) | [CC-BY-NC-3.0](http://datacanvas.org/public-transportation/) |
| QuantEcon.notebooks   |  QuantEcon | [BSD 3-clause "New" or "Revised" License](https://github.com/QuantEcon/QuantEcon.notebooks/blob/master/LICENSE) |
| TCGA   |  Gross et. al. | None Listed | None Listed |
| TensorFlow-Examples   |  Aymeric Damien | [MIT](https://github.com/aymericdamien/TensorFlow-Examples/blob/master/LICENSE) |
