docker-compose up -d 

docker-compose exec web python manage.py migrate

Swagger
http://localhost:8091/tasks/swagger

Postman 
Проверка фильтров
http://localhost:8091/tasks/?status=in_progress&due_date_after=2025-12-01&due_date_before=2025-12-20