IMAGE_NAME = python-hexagonal-example

.PHONY: build
build:
	docker build --target release -t $(IMAGE_NAME) .

.PHONY: run
run:
	docker run -it --rm -p 8000:8000 -e PORT=8000 $(IMAGE_NAME)
