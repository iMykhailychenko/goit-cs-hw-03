CONTAINER_ID := $(shell docker ps -q --filter ancestor=mongo)
ALL_CONTAINERS := $(shell docker ps -a -q --filter ancestor=mongo)

up: clean build run

build:
	docker build -t mongo .

run:
	docker run -p 27017:27017 -d mongo

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
