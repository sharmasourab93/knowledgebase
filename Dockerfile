FROM python:3.6

RUN pip install setuptools
COPY . /kb 
WORKDIR kb/ 
RUN apt-get update
RUN apt-get install -y \
    gettext \
    postgresql
RUN python kb/setup.py develop
RUN python - m pip install -e kb/.
CMD ["pserve", "development.ini", "--reload"]
