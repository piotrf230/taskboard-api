***[Polska wersja](README.md)***
# Task management application backend
## Run
Application requires Docker and docker-compose in order to run.
In order to run the app in docker containers (three containers are created: "db" - database, "backend" - app and "web" - nginx server), one should execute the following commands in TaskboardProject directory:  
<code>docker-compose up -d  --build</code>  
<code>docker-compose exec web python manage.py collectstatic</code>  
<code>docker-compose exec web python manage.py migrate</code>  
The following command can be used to add administrator user:  
<code>docker-compose exec web python manage.py createsuperuser</code>  