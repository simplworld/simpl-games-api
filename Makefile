.PHONY: image push-image build-image

include .version

build-image:
	@echo building ${IMAGE_TAG}
	@docker build -t ${IMAGE_TAG} .

push-image:
	@echo pushing ${IMAGE_TAG}
	@docker push ${IMAGE_TAG}

image: build-image push-image



