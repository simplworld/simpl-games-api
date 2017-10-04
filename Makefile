.PHONY: image push-image build-image

include .version

ifdef PKG_PROXY
	PROXY_ARGS := --build-arg proxy=${PKG_PROXY}
else
	PROXY_ARGS :=
endif

PROXY = 

build-image:
	@echo building ${IMAGE_TAG}
	@docker build ${PROXY_ARGS} -t ${IMAGE_TAG} .

push-image:
	@echo pushing ${IMAGE_TAG}
	@docker push ${IMAGE_TAG}

image: build-image push-image



