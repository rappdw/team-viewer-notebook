FROM rappdw/docker-ds

RUN pip install tv-extract; \
    mkdir /home/jovyan/project

ADD TeamViewTemplate.json /templates/TeamViewTemplate.json
ADD configure_notebooks.py /configure_notebooks.py
ADD team-view-entrypoint.sh /team-view-entrypoint.sh

CMD ["/usr/local/bin/start-notebook.sh"]
ENTRYPOINT ["/team-view-entrypoint.sh"]
