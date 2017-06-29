# JupyterLab Demonstration

[![Build Status](https://travis-ci.org/jupyterlab/jupyterlab-demo.svg?branch=master)](https://travis-ci.org/jupyterlab/jupyterlab-demo)

This repository contains some demonstrations of
[JupyterLab](https://github.com/jupyter/jupyterlab), the next
generation user interface of Project Jupyter.

## Installation

The requirements for this demo are described in `environment.yml`

For users with [Anaconda](https://anaconda.org/), this JupyterLab uses a conda environment named `jupyterlab-demo`.

### Create the environment

To create the conda environment with all the dependencies and jupyterlab extensions for the demo, run:

```bash
bash INSTALL.sh
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

make demo

# Demo guide

The basic outline of the JupyterLab demo is described in the file `jupyterlab.md`.
