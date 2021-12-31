# ({{cookiecutter.event_type}}SNS) Lambda

===============================

({{cookiecutter.event_type}}) `AWS Lambda`

- Git repo: https://gitlab.com/path_to_repo
- Documentation: https://gitlab.com/path_to_repo/README.md

* Free software: {{cookiecutter.license}}

## About

---

This Lambda is to be triggered by an {{cookiecutter.event_type}} event that ...

The Lambda function is responsible for:

- what this Lambda does

See the official docs [here](https://docs.aws.amazon.com/lambda/ 'official docs').

## Prerequisite, Setup and Usage

---

> as a base prerequisite you should have AWS SAM [installed](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

From the **package root**,

1. Check/Change incoming mock `event.json` [file](./events/event.json)

2. Suppply `env-vars` in [envs.json]events/event.json) and [template.yaml]events/template.yaml)

   > Be aware that for a successful local invokation variables in [envs.json]events/event.json) and [template.yaml]events/template.yaml) have to be duplicated and [match](https://github.com/aws/aws-sam-cli/issues/139#issuecomment-334977285)

3. Use `make local-invokation` local invokation of Lambda

   This will call the `main` function with a sample event using AWS SAM [framework](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) in Docker replicated environment that copies
   AWS CLOUD Lambda set-up. The sample event is
   picked up from the `./events/event.json` file which, ideally speaking, contains
   a sample copy of the actual AWS event object that this handler receives when
   it is deployed live.

## Deployment

---

1. Ensure the `VERSION` file has the correct package version

2. Then, build the package in order to output a `.zip` file in `dist` folder.
   The package name is the expansion of `payload-$lambda_version-$ENVIRONMENT.zip`

```sh
ENVIRONMENT=staging MODULE_NAME=data_retrieval_file_s3 make build-lambda
```

_If not using the Makefile (not recommended), you can invoke the following shell command:_

```sh
ENVIRONMENT=staging
cp $PROJECT_ROOT/.env.${ENVIRONMENT} .env
ENVIRONMENT=${ENVIRONMENT} lambda_version=$(cat VERSION) ./build.sh
```

_Make sure you are aware of the $ENVIRONMENT you're building the package for._

3. Finally, publish the package to the project's Gitlab package registry:

```sh
ENVIRONMENT=staging MODULE_NAME=cognito_post_confirmation make publish-lambda
```

_If not using the Makefile (not recommended), you can invoke the following shell command:_

```sh
ENVIRONMENT=staging
cp $PROJECT_ROOT/.env.${ENVIRONMENT} .env
# To publish to the project, get the backend project id from the common env file
PROJECT_ID="23852426" ENVIRONMENT=${ENVIRONMENT} lambda_version=$(cat VERSION) ./publish.sh
```

_Make sure you are aware of the $ENVIRONMENT you're building the package for._

4. Once published, inform the operations team of a new package that is ready for
   deployment.
