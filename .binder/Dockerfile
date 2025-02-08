# Inherit from an upstream image
FROM quay.io/jupyter/base-notebook:2025-02-03

COPY ./.binder/environment.yml /tmp/environment.yml

RUN mamba env update --prefix ${CONDA_DIR} --file /tmp/environment.yml