# JupyterLab Demonstration

[![Build Status](https://travis-ci.org/jupyterlab/jupyterlab-demo.svg?branch=master)](https://travis-ci.org/jupyterlab/jupyterlab-demo)

This repository contains some demonstrations of
[JupyterLab](https://github.com/jupyter/jupyterlab), the next
generation user interface of Project Jupyter.

# Installation

To install all of the files needed for the demo, run:

```
make demo
```

This demo will need the latest release of the following
packages:

* [jupyterlab](https://github.com/jupyter/jupyterlab)
* [jupyterlab ipywidgets](https://github.com/jupyter-widgets/ipywidgets)
* [jupyterlab google drive](https://github.com/jupyterlab/jupyterlab-google-drive)
* [jupyter notebook](https://github.com/jupyter/notebook)
* [matplotlib](https://github.com/matplotlib/matplotlib)
* [pandas](https://github.com/pandas-dev/pandas)
* [scikit-image](https://github.com/scikit-image/scikit-image)
* [graphviz](http://graphviz.readthedocs.io/en/stable/manual.html)

Additionally, we require installation of:

* [graphviz](http://www.graphviz.org/Download..php)
* [nodejs version 5.0 or greater](https://nodejs.org/en/)

For users with [Anaconda](https://anaconda.org/), we have a script that creates a conda envrionment, `jlabdemo`, designed for the content of this demo.

To install, call:

```
bash INSTALL.txt
```

# Demo guide

The basic outline of the JupyterLab demo is described in the file `jupyterlab.md`.