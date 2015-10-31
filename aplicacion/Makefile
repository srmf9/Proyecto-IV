clean:
	- rm -rf *~*
	- find . -name '*.pyc' -exec rm {} \;

test: clean
	python manage.py test

install: clean
	python setup.py install
run:
	python manage.py runserver
