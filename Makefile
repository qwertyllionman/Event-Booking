migration:
	python manage.py makemigrations
	python manage.py migrate

runserver:
	python manage.py runserver

app:
	python manage.py startapp apps

superuser:
	python manage.py createsuperuser