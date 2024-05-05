CONTAINER_ID := $(shell docker ps -q --filter ancestor=postgres)
ALL_CONTAINERS := $(shell docker ps -a -q --filter ancestor=postgres)

up: clean build run

build:
	docker build --build-arg POSTGRES_DB=$(shell grep POSTGRES_DB .env | cut -d '=' -f2) \
                 --build-arg POSTGRES_USER=$(shell grep POSTGRES_USER .env | cut -d '=' -f2) \
                 --build-arg POSTGRES_HOST=$(shell grep POSTGRES_HOST .env | cut -d '=' -f2) \
                 --build-arg POSTGRES_PASSWORD=$(shell grep POSTGRES_PASSWORD .env | cut -d '=' -f2) \
                 -t postgres .

run:
	docker run -p 5432:5432 -d postgres

clean:
ifneq ($(CONTAINER_ID),)
	@echo "Stopping container: $(CONTAINER_ID)"
	@docker stop $(CONTAINER_ID)
else
	@echo "No running container found."
endif
ifneq ($(ALL_CONTAINERS),)
	@echo "Removing container: $(ALL_CONTAINERS)"
	@docker rm $(ALL_CONTAINERS)
else
	@echo "No old container found."
endif

stop:
ifneq ($(CONTAINER_ID),)
	@echo "Stopping container: $(CONTAINER_ID)"
	@docker stop $(CONTAINER_ID)
else
	@echo "No running container found."
endif
