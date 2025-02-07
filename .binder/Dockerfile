# Inherit from an upstream image
FROM quay.io/jupyter/base-notebook:2025-02-03

COPY environment.yml /tmp/environment.yml

RUN mamba env update  --debug --prefix ${CONDA_DIR} --file /tmp/environment.yml