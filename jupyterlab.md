# JupyterLab Demo

JupyterLab: The next generation user interface for Project Jupyter

https://github.com/jupyter/jupyterlab

Collaboration between
* Project Jupyter
* Bloomberg
* Continuum

**DON'T TRY THIS AT HOME - JUPYERLAB IS EXTREMELY ALPHA!!**

## 1) Building blocks of interactive computing

### Demonstrate left panel plugins:

* File Browser (file operations, including drag and drop)
* Command Palette (fuzzy searching for 'new')

### Open the building blocks:

* Notebook
  - Image Processing.ipynb
* Editor
  - .py, .md examples
* Terminal
* Console

### Arrange the building blocks in the main area

## 2) Connecting the building blocks

The building blocks can be connected to support a wide range of different workflows:

* Open `markdown_python.md` in the File Editor
* View the rendered markdown
* Attach a Kernel/Console and run the code by selecting blocks and pressing
  `Shift+Enter`

## 3) Deconstruct components

* Drag out plot from console
  - bulk written in a few hours
* Image processing example


## 4) File handlers

JupyterLab has a powerful and extensible architecture for handling a wide range of file formats:

* Open image `jupyter.png`
* Drag to open `jupyterlab.md` in the Markdown Viewer and edit
* Open `Data.ipynb` to view data
* Open `iris.csv`
* Open DC museum GeoJSON file (from [OpenData DC](http://opendata.dc.gov/datasets/2e65fc16edc3481989d2cc17e6f8c533_54)) - -73,40
* Open `scatter_opacity.json` as a vega plot

## 5) Plugin architecture

The genius of open-source is being able to shape your tools to your heart's content.

Just like Jupyter is built on top of building blocks of the protocol and message spec, *you* can build on this platform for your workflow.

* Everything in JupyterLab is a plugin, even our own code: `extensions.js`
* Anyone can create, package, ship plugins
* Plugins can, for example:
  - add things to command palette, menu
  - add viewers for documents
  - expose other controls (e.g., manage a spark cluster?)
  - provide more capabilities to the system

* Examples:
  - [ipywidgets](https://github.com/ipython/ipywidgets)
  - [GeoJSON file handler](https://github.com/jupyter/jupyterlab_geojson)
  - [Dask JupyterLab extension](https://github.com/dask/dask-labextension)
  - [Vega/VegaLite JupyterLab extension](https://github.com/ellisonbg/jupyterlab_vega)
  - [Cookie cutter recipe](https://github.com/jupyter/jupyterlab-extension-cookiecutter-ts)

## What will you build?

