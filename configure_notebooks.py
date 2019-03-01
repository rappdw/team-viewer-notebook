#!/usr/bin/env python

import json
import pathlib
import shutil
import jinja2
from tv_extract.util.cli import extract_config_from_json


if __name__ == "__main__":
    templateLoader = jinja2.FileSystemLoader(searchpath="/templates")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template("TeamViewTemplate.json")

    with open('/root/extract/extract.json', 'r') as config_file:
        json_config = json.load(config_file)
        config = extract_config_from_json(json_config)
        # first run jinja to create seperate notebooks for each project
        for extract in config.extracts:
            with open(f'/home/jovyan/project/{extract.name}.ipynb', 'w') as file:
                file.write(template.render(extract=extract))
        # Now, setup AWS region if present
        if 'awsregion' in json_config:
            aws_dir = pathlib.Path('/home/jovyan/.aws')
            aws_dir.mkdir(parents=True, exist_ok=True)
            aws_config_file = aws_dir / 'config'
            with aws_config_file.open(mode='w') as aws_config:
                aws_config.write(f"[profile ds-notebook]\nregion = {json_config['awsregion']}\n\n")
                shutil.chown(str(aws_config_file.resolve()), user='jovyan', group='users')
            shutil.chown(str(aws_dir.resolve()), user='jovyan', group='users')
