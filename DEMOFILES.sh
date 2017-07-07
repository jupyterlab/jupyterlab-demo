#!/usr/bin/env bash

mkdir demofiles
cd demofiles
git clone https://github.com/jakevdp/PythonDataScienceHandbook.git
git clone https://github.com/swissnexSF/Urban-Data-Challenge.git
git clone https://github.com/altair-viz/altair.git
git clone https://github.com/QuantEcon/QuantEcon.notebooks.git
git clone https://github.com/theandygross/TCGA.git
git clone https://github.com/aymericdamien/TensorFlow-Examples.git

# to remove demofiles
# rm -rf demofiles