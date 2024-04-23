install:
	@echo "Installing..."
	pip install --upgrade pip && pip install -r requirements.txt
test:
	python manage.py test

run:
	python manage.py runserver