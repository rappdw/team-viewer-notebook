FROM rappdw/docker-ds

RUN pip install tv-extract; \
    mkdir /home/jovyan/project

ADD TeamViewTemplate.json /templates/TeamViewTemplate.json
ADD configure_notebooks.py /configure_notebooks.py
ADD team-view-entrypoint.sh /team-view-entrypoint.sh

# To try this out, outside of the kubernetes application environment, add an extract.json to the image
#ADD sample.extract.json /root/extract/extract.json

CMD ["/usr/local/bin/start-notebook.sh"]
ENTRYPOINT ["/team-view-entrypoint.sh"]
