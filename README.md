# JupyterLab Demonstration

[![Build Status](https://travis-ci.org/jupyterlab/jupyterlab-demo.svg?branch=master)](https://travis-ci.org/jupyterlab/jupyterlab-demo)

This repository contains some demonstrations of
[JupyterLab](https://github.com/jupyter/jupyterlab), the next
generation user interface of Project Jupyter.

## Installation

The requirements for this demo are described in `environment.yml`

For users with [Anaconda](https://anaconda.org/), this JupyterLab uses a conda environment named `jupyterlab-demo`.

To install the environment and demofiles, we use [pyinvoke](pyinvoke.org). To install pyinvoke with pip call:

```bash
pip install invoke
```

### Create the environment

To create the conda environment with all the dependencies and jupyterlab extensions for the demo, run:

```bash
invoke environment
```

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
| PythonDataScienceHandbook/LICESNSE-CODE  | Jake Vanderplas  | [MIT](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/LICENSE-CODE)|
| PythonDataScienceHandbook/LICESNSE-TEXT   |  Jake Vanderplas | [CC-BY-NC-ND-3.0](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/LICENSE-TEXT) |
| altair   |  Jake Vanderplas | [BSD 3-clause](https://github.com/altair-viz/altair/blob/master/LICENSE) |
| Urban-Data-Challenge   |  www.urbandatachallenge.org | None Listed | None Listed |
| QuantEcon.notebooks   |  QuantEcon | [BSD 3-clause "New" or "Revised" License](https://github.com/QuantEcon/QuantEcon.notebooks/blob/master/LICENSE) |
| TCGA   |  Gross et. al. | None Listed | None Listed |
| TensorFlow-Examples   |  Aymeric Damien | [MIT](https://github.com/aymericdamien/TensorFlow-Examples/blob/master/LICENSE) |
