# JupyterLab Demo

JupyterLab: The next generation user interface for Project Jupyter

https://github.com/jupyter/jupyterlab

It has been a collaboration between:

* Project Jupyter
* Bloomberg
* Anaconda

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

## 5) Plugin architecture

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

