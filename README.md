# JupyterLab Demonstration

This repository contains some demonstrations of
[JupyterLab](https://github.com/jupyter/jupyterlab), the next
generation user interface of Project Jupyter.

# Installation

To install all of the files needed for the demo, run:

    make demo

This demo will need the latest development master of the following
packages:

* jupyterlab (https://github.com/jupyter/jupyterlab)
* jupyterlab_geojson (https://github.com/jupyter/jupyterlab_geojson)
* jupyterlab_vega (https://github.com/altair-viz/jupyterlab_vega)

Additionally, if you want to run Altair in the Jupyter Notebooks, you will need
this branch of altair:

* altair (https://github.com/ellisonbg/altair/tree/jupyterlab)

*Note:* if you have version 4.3.1 of the Jupyter Notebook, when starting `jupyter notebook` or `lab`, you *must* make the call with `--NotebookApp.disable_check_xsrf=True`.  Else nothing will work with no easy to find errors.

# Demo guide

The basic outline of the JupyterLab demo is described in the file `jupyterlab.md`.

A basic description of Altair can be found in the file `altair.md`.
