COMPOSE=docker-compose -f docker-compose.yaml -f docker/book_storage/docker-compose.yaml -f docker/delivery/docker-compose.yaml -f docker/cabinet/docker-compose.yaml

SERVICES=book_storage delivery cabinet
MIGRATIONS=migrate_book_storage migrate_delivery
DATABASES=book_storage_db delivery_db

clean:
	$(COMPOSE) stop $(SERVICES) $(DATABASES)
	yes | $(COMPOSE) rm -f $(SERVICES) $(DATABASES)

migrate: clean
	$(COMPOSE) up --build $(MIGRATIONS)

up:
	$(COMPOSE) up --build $(SERVICES) jaeger filebeat
