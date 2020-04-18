.PHONY: image push-image build-image rebuild shell

include .version

ifdef PKG_PROXY
	PROXY_ARGS := --build-arg=http_proxy=${PKG_PROXY} --build-arg=https_proxy=${PKG_PROXY}
else
	PROXY_ARGS :=
endif

build-image:
	@echo building ${IMAGE_TAG}
	@docker build ${PROXY_ARGS} -t ${IMAGE_TAG} .

push-image:
	@echo pushing ${IMAGE_TAG}
	@docker push ${IMAGE_TAG}

image: build-image push-image

shell:
	docker-compose run --rm web bash

rebuild:
	docker-compose rm -f web
	docker-compose rm -f celery
	docker-compose build web

