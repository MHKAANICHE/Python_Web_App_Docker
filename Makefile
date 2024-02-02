install : 
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora

format : 
	#format code
	black *.py mylib/*.py

lint : 
	#lake8 or #pylint
	pylint --disable=R,C *.py

test : 
	#test
	python -m pytest -vv --cov=mylib --cov=main test_*.py

build: 
	#build container
	docker build -t deploy-fastapi .

run : 
	#run docker
	docker run -p 127.0.0.1:8080:8080 deploy-fastapi

deploy :
	#tag the Docker image
	docker tag deploy-fastapi mhkaaniche/deploy-fastapi
	#push the Docker image to DockerHub
	docker push mhkaaniche /deploy-fastapi

all: install lint test build run deploy