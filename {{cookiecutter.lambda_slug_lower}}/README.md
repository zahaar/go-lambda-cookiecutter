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
