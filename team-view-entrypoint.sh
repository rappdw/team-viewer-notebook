#!/usr/bin/env bash

/configure_notebooks.py
exec /docker-entrypoint.sh $*

