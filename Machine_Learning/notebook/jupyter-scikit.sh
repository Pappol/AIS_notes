#!/usr/bin/env sh

export PATH="/usr/local/tensorflow/bin:/usr/local/jupyter/bin:$PATH"
export PYTHONPATH="/usr/local/jupyter/lib/python3.5/site-packages:/usr/local/tensorflow/lib/python3.5/site-packages:$PYTHONPATH"

jupyter notebook
