#!/usr/bin/env bash

export DEMO_ENV_NAME=jupyterlab-demo

# Create a new environment
conda env create -f environment.yml
source activate $DEMO_ENV_NAME

# Currently need prereleases of widgets
# and bqplot in yml file
#pip install bqplot --pre
#pip install ipywidgets --pre

# Install the environment kernel
ipython kernel install --name $DEMO_ENV_NAME --display-name $DEMO_ENV_NAME --sys-prefix

# Install google-drive
jupyter labextension install @jupyterlab/google-drive@0.3.1
jupyter lab clean && jupyter lab build

# Install ipywidgets
jupyter labextension install @jupyterlab/nbwidgets@0.21

#Install bqplot
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install bqplot-jupyterlab

# To remove the environment
# source deactivate $DEMO_ENV_NAME
# conda remove --all -n $DEMO_ENV_NAME