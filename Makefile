clean:
	@find . -name "*.pyc" -delete

db:
	@python ./manage.py migrate

install:
	@pip install -r requirements.txt
	@python ./manage.py migrate

run:
	@python ./manage.py runserver

pep8:
	@pep8 --exclude 'migrations' .
	
test:
	@python manage.py test 

coverage:
	@coverage run manage.py test
	@coverage html
	@open coverage_html_report/index.html

rebuild_index:
	@python ./manage.py rebuild_index

makemessages:
	@cd atados_core; \
	django-admin.py makemessages --all
	
compilemessages:
	@cd atados_core; \
	django-admin.py compilemessages

