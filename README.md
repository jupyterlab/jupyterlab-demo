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

### Uninstalling

To uninstall the demofiles and enviornment, call:

```
invoke clean
```

# Demo guide

The basic outline of the JupyterLab demo is described in the file `jupyterlab.md`.
