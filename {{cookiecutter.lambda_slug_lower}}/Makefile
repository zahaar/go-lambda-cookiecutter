###############################################################################
#
# @description Commands to setup, develop and deploy the project
# @author Engineering Department <engineering@company.de>
#
###############################################################################
# Make
###############################################################################

SHELL=/bin/bash

ENVIRONMENT=testing

lambda_version ?= 0.1-$(ENVIRONMENT)
GO_VERSION ?= 1.16
PAYLOAD_NAME := payload-$(lambda_version).zip
PROJECT_ROOT := $(PWD)


# --- Makefile starts here
.DEFAULT_GOAL := all

# ================== Makefile commands ====================
.PHONY: all build zip local-invokation

# all: build

sam-build:
	sam build

local-invokation: sam-build
	sam local invoke "{{ cookiecutter.lambda_slug }}" -e events/event.json --env-vars envs.json

################################################################
PROJECT_NAME := "{{ cookiecutter.lambda_slug }}"
PKG := "example.com"
PKG_LIST := $(shell go list ${PKG} | grep -v /vendor/)
# GO_FILES := $(shell find . -name '*.go' | grep -v /vendor/ | grep -v _test.go)

format: ## format the files
	@gofmt -w .

lint: ## Lint the files
	@golint -set_exit_status ${PKG_LIST}

test: ## Run unittests
	@go test -short ${PKG_LIST}

race: dep ## Run data race detector
	@go test -race -short ${PKG_LIST}

msan: dep ## Run memory sanitizer
	@go test -msan -short ${PKG_LIST}

dep: ## Get the dependencies
	@go get -v -d .

build:  ## Build the binary file
	@GOOS=linux CGO_ENABLED=0 go build main.go

zip: build
ifeq ($(PAYLOAD_NAME), )
	@echo "==> Usage: PAYLOAD_NAME=payload_name make zip"
	exit 1
else
	@mkdir -p dist && \ 
	zip ./dist/$(PAYLOAD_NAME) main
endif


clean: ## Remove previous build
	@rm -f $(PKG)

# help: ## Display this help screen
#   @grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

