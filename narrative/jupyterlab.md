# JupyterLab Demo

JupyterLab: The next generation user interface for Project Jupyter

https://github.com/jupyter/jupyterlab

It started as a collaboration between:

* Project Jupyter
* Bloomberg
* (then) Continuum

and now involves many other people from many other places (not purely academic or business)

## 1) Building blocks of interactive computing

### Start with the launcher


Use it to open different activities:

* Notebook
* Console
* Editor
* Terminal

### Notebooks

* Open example notebooks to show that notebooks still work
* Collapse input/output
* Drag and drop cells

### Demonstrate left panel plugins:

* File Browser (file operations, context menu, including drag and drop)
* Running
* Command Palette (fuzzy searching for 'new')

### Markdown example

* Open `markdown_python.md` in the File Editor
* View the rendered markdown, arrange side by side
* Attach a Kernel/Console and run the code by selecting blocks and pressing
  `Shift+Enter`

### Arrange the building blocks in the main area

The dock panel allows you to arrange the activites into an
arbitrary layout.

Tabs and single document mode allow you to focus.

## 4) File handlers

JupyterLab has a powerful and extensible architecture for handling a wide range of file formats:

* CSV
  - `./data/iris.csv` (small)
  - `TCGA_Data` (small to medium)
  - Urban_Data_Challenge: `data/big.csv`
* Images
  - `data/hubble.png`
* Vega-Lite
  - `data/vega.vl.json`
* Open DC museum GeoJSON file from [OpenData DC](http://opendata.dc.gov/datasets/2e65fc16edc3481989d2cc17e6f8c533_54): `data/Museums_in_DC.geojson`
* Notebook demonstrating bqplot widgets: `notebooks/bqplot.ipynb`

## 5) Find and Replace
first class support for find and replace across JupyterLab, currently supported in 
notebooks and text files and is extensible for other widgets who wish to support it.

## 6) Status Bar
We have integrated the JupyterLab Status Bar package package into the core distribution. Extensions can add their own status to it as well 

## 7) Printing

A printing system allows extensions to customize how documents and activities are printed. 

## 8) JupyterHub

We now include the JupyterHub extension as a core JupyterLab extension, so you no longer need to install @jupyterlab/hub-extension (supporting multi-user + authentication workflows)

## 9) Plugin architecture

The genius of open-source is being able to shape your tools to your heart's content.

Just like Jupyter is built on top of building blocks of the protocol and message spec, *you* can build on this platform for your workflow.

* Everything in JupyterLab is an extension, including everything we have demoed
* Extensions are just `npm` packages with metadata
* Anyone can create, package, ship plugins
* Extension can, for example:
  - Add things to command palette, menu
  - Add viewers for documents
  - Expose other controls (e.g., manage a spark cluster?)
  - Provide more capabilities to the system

## What will you build?

