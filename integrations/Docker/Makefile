IMAGE_NAME = subsidy-crawl-url
CONTAINER_NAME = crawl-test
DOCKER_TAG = $(shell git rev-parse --abbrev-ref HEAD)

DOCKER_REGISTRY_NAME = fionn88

build:
	docker build -t $(DOCKER_REGISTRY_NAME)/$(IMAGE_NAME):$(DOCKER_TAG) .
