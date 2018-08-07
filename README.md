[![Build Status](https://img.shields.io/docker/automated/rappdw/team-view-notebook.svg)](https://hub.docker.com/r/rappdw/team-view-notebook/)


# Docker Image for Team View Analysis Notebook

While this docker image can be used standalone (with appropriate mounts when running),
it is intened for use in the Team View kubernetes application.

See [Team View](https://github.com/rappdw/TeamView) for details.

## Analytics notebooks

`TeamViewTemplate.json` is a [jinja2](http://jinja.pocoo.org/) template that is used to generate
project specific jupyter notebooks based on the configuration found in `/root/extract/extract.json`.
