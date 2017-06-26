# JupyterLab Demonstration

This repository contains some demonstrations of
[JupyterLab](https://github.com/jupyter/jupyterlab), the next
generation user interface of Project Jupyter.

## Installation

This JupyterLab demo is based on a conda environment named `jupyterlab-demo`,
that is defined in the associated `environment.yml` file.

### Create the environment

To create a new conda environment with all the dependencies for the demo, run:

```bash
conda env create -f environment.yml
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

### Install demo files

The demo includes files from a number of other repositories. To install these files,
run:

```bash
make demo
```

# Demo guide

The basic outline of the JupyterLab demo is described in the file `jupyterlab.md`.

A basic description of Altair can be found in the file `altair.md`.
