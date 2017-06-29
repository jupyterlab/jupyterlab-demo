export DEMO_ENV_NAME=jupyterlab-demo

# Create a new environment
conda env create -f environment.yml
source activate $DEMO_ENV_NAME

# Install the environment kernel
ipython kernel install --name $DEMO_ENV_NAME --display-name $DEMO_ENV_NAME --sys-prefix

# Install google-drive
jupyter labextension install @jupyterlab/google-drive
jupyter lab clean && jupyter lab build

# Install ipywidgets
jupyter labextension install @jupyterlab/nbwidgets@0.21

# To remove the environment
# source deactivate $DEMO_ENV_NAME
# conda remove --all -n $DEMO_ENV_NAME