COMPOSE_FILE = compose.yaml
TEST_COMPOSE_FILE = compose.test.yaml

.PHONY: all
all: build

.PHONY: build
build:
	docker compose -f $(COMPOSE_FILE) build

.PHONY: run
run:
	docker compose -f $(COMPOSE_FILE) up

.PHONY: test
test:
	docker compose -f $(COMPOSE_FILE) -f $(TEST_COMPOSE_FILE) up --abort-on-container-exit -t 0
	docker compose -f $(COMPOSE_FILE) -f $(TEST_COMPOSE_FILE) stop -t 0
	@echo -e "\n----------------------------- burger orderer tests -----------------------------\n"
	docker logs burger_orderer_test_container --since 5s
	@echo -e "\n------------------------------ kitchen view tests ------------------------------\n"
	docker logs kitchen_view_test_container --since 5s

.PHONY: clean
clean:
	docker compose -f $(COMPOSE_FILE) down --volumes --remove-orphans
	docker compose -f $(TEST_COMPOSE_FILE) down --volumes --remove-orphans

.PHONY: help
help:
	@echo "Makefile commands:"
	@echo "  make build    - Build the Docker containers"
	@echo "  make run      - Run the application"
	@echo "  make test     - Run the tests"
	@echo "  make clean    - Clean up containers, networks, images, and volumes"
	@echo "  make help     - Show this help message"
