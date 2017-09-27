#flaskmvc

Python Flask MVC Structure

This is a open source MVC Structure for Python Flask to create small and large projects on WEB and APIs.

Basic requirements

You may already installed python. If not installed please follow the link below.

	https://www.python.org/downloads/

Install PIP that is a package installer in python.

	curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"

	python get-pip.py


Install environment for flask app.

	pip install Flask

	pip install virtualenv


After basic installments clone the Flask MVC Structuce

	https://github.com/sheetalkumar105/flaskmvc.git


To run the application use following commands:

	sudo pip install -e .

	flask runprintenv FLASK_APP

	export FLASK_APP=app/__init__.py

	export FLASK_DEBUG=1

	flask run


To change database connection open app/config.py and configure

	config['MONGO_DBNAME'] = 'flaskblog'
	config['MONGO_URI'] = 'mongodb://localhost:27017/flaskblog'