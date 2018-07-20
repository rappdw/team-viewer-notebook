#!/usr/bin/env python

import json
import jinja2
from tv_extract.util.cli import extract_config_from_json


if __name__ == "__main__":
    templateLoader = jinja2.FileSystemLoader(searchpath="/templates")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template("TeamViewTemplate.json")

    with open('/root/extract/extract.json', 'r') as config_file:
        config = extract_config_from_json(json.load(config_file))
        for extract in config.extracts:
            with open(f'/home/jovyan/project/{extract.name}.ipynb', 'w') as file:
                file.write(template.render(extract=extract))
