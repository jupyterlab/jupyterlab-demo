# JupyterLab Demo

JupyterLab: The next generation user interface for Project Jupyter

https://github.com/jupyter/jupyterlab

* Project Jupyter
* Bloomberg
* Continuum

**DON'T TRY THIS AT HOME - JUPYERLAB IS EXTREMELY ALPHA!!**

## 1) Building blocks of interactive computing

### Open the building blocks:

* Notebook
  - Explore notebooks from demofiles/PythonDataScienceHandbook
  - Explore notebooks from demofiles/Altair
* Terminal
* File Editor
* Console

### Arrange the building blocks in the main area

### Demonstrate left panel plugins:

* File Browser
  - Drag the `move_this_file.txt` to the `move_it_here` directory
* Command Palette

## 2) File handlers

JupyterLab has a powerful and extensible architecture for handling a wide
range of file formats:

* Open this file in the Markdown Viewer and edit
* Browse through CSV and GeoJSON files from 
  [Urban Data Challenge](https://github.com/swissnexSF/Urban-Data-Challenge)
* Open a [VegaLite](https://vega.github.io/vega-lite/) JSON file from the
  `vegalite` directory

## 3) Connecting the building blocks

The building blocks can be connected to support a wide range of different workflows:

* Open `markdown_python.md` in the File Editor
* View the rendered markdown
* Attach a Kernel/Console and run the code by selecting blocks and pressing
  `Shift+Enter`

## 4) Third party plugins/extensions

* Everything in JupyterLab is a plugin, even our own code
* Third party developers can create, package, ship plugins
* Examples:
  - [ipywidgets](https://github.com/ipython/ipywidgets)
  - [GeoJSON file handler](https://github.com/jupyter/jupyterlab_geojson)
  - [Dask JupyterLab extension](https://github.com/dask/dask-labextension)
  - [Vega/VegaLite JupyterLab extension](https://github.com/ellisonbg/jupyterlab_vega)
