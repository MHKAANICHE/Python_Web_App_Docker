install : 
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
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
	#docker run -p 127.0.0.1:8080:8080 e99963afe84d
deploy :
	#deploy 
all: install lint test deploy 
