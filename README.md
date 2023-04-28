***[English Version](README_en.md)***
# Backend aplikacji do zarządzania zadaniami
## Uruchomienie
Aplikacja wymaga do uruchomienia programu Docker oraz docker-compose.  
Aby uruchomić aplikację w kontenerach docker (tworzony jest kontener bazy danych "db", kontener aplikacji "backend" oraz kontener serwera nginx "web"), należy wykonać w katalogu TaskboardProject następujące polecenia:  
<code>docker-compose up -d  --build  
docker-compose exec web python manage.py collectstatic  
docker-compose exec web python manage.py migrate</code>  
Aby dodać konto administratora, należy dodatkowo wykonać polecenie:  
<code>docker-compose exec web python manage.py createsuperuser</code>  
