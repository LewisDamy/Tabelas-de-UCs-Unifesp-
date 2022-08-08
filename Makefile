# install libraries cmd
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
			pip install --force-reinstall tabula-py # problem with this library

# install requirments.txt
freeze:
	pip freeze > requirements.txt

# format code
format:
	black *.py
lint:
	pylint --disable=R,C file.py
test:
	#test
	python main.py
run:
	python pdf-xslx-converter.py
deploy:
	#deploy
all:
	install lint test deploy
