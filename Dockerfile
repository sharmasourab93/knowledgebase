FROM archlinux\base 

RUN pacman -Syu && \
	pacman -Syu python-pip python-dev && \
	pip install --upgrade pip setuptools 
	
WORKDIR knowledgebase/kb/

RUN pip install -r requirements.txt 

ENTRYPOINT [ "python" ]

CMD [ " setup.py develop", 

"pserve development.ini --reload", 
	]
