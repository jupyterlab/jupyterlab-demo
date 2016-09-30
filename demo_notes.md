# JupyterLab Demo

## 1) Building blocks of interactive computing

### Open the building blocks:

* Notebook
* Terminal
* File Editor
* Console

### Arrange the building blocks in the main area


### Demonstrate left panel plugins:

* File Browser
* Command Palette

## 2) File handlers

This works!

JupyterLab has a powerful and extensible architecture for handling a wide
range of file formats:

* Open this file in the Markdown Viewer and edit
* Browse through CSV and GeoJSON files from 
  [Urban Data Challenge](https://github.com/swissnexSF/Urban-Data-Challenge).

## 3) Connecting building blocks

The building blocks can be connected to support
a wide range of different workflows:

* Open `markdown_python.md` in the File Editor
* View the rendered markdown
* Attach a Kernel/Console and run the code

## 4) Third party plugins/extensions

* Everything in JupyterLab is a plugin - even our own code
  - NPM, webpack, etc.
* Third party developers can create, package, ship plugins.
* The GeoJSON file handler is shipped separately as
  [jupyterlab_geojson](https://github.com/jupyter/jupyterlab_geojson)
* [Dask JupyterLab extension](https://github.com/dask/dask-labextension)
  - Matt Rocklin (Dask, Continuum) is here to demo the Dask JupyterLab extension
