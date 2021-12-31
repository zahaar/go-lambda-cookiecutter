## Usage

Let's pretend you want to create a AWS Lambda project called "sns-processor". Rather than using `lambda`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter\_ to do all the work.

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo::

    $ cookiecutter https://github.com/zahaar/go-lambda-cookiecutter

You'll be prompted for some values. Provide them, then a Lambda sample project will be created for you.

**Warning**: After this point, change '[My Lambda]', 'lambda_description', etc to your own information.

Answer the prompts with your own desired options\_. For example::

    lambda_name [My Lambda]:
    lambda_version [0.1.0]:
    lambda_slug [MyLambda]:
    lambda_slug_lower [my_lambda]: sns-processor
    lambda_description [GoLang lambda for My Lambda]:
    author_name [Engineering Department]:
    author_email [engineering@company.de]:
    go_version [1.16]:
    go_module_path [example.com]:
    Select event_type:
    1 - SNS
    2 - S3
    3 - API_GW
    Choose from 1, 2, 3 [1]:
    sentry_dsn []:
    Select license:
    1 - MIT
    2 - BSD-3
    3 - GNU GPL v3.0
    4 - Apache 2.0
    5 - Mozilla 2.0
    Choose from 1, 2, 3, 4, 5 [1]:
    Select add_git:
    1 - True
    2 - False
    Choose from 1, 2 [1]:
    go: creating new go.mod: module example.com
    go: to add module requirements and sums:
    go mod tidy
    go: finding module for package github.com/getsentry/sentry-go
    go: finding module for package github.com/lib/pq
    go: finding module for package github.com/aws/aws-lambda-go/events
    go: finding module for package github.com/aws/aws-lambda-go/lambda
    go: downloading github.com/aws/aws-lambda-go v1.27.1
    go: downloading github.com/getsentry/sentry-go v0.12.0
    go: found github.com/aws/aws-lambda-go/events in github.com/aws/aws-lambda-go v1.27.1
    go: found github.com/aws/aws-lambda-go/lambda in github.com/aws/aws-lambda-go v1.27.1
    go: found github.com/getsentry/sentry-go in github.com/getsentry/sentry-go v0.12.0
    go: found github.com/lib/pq in github.com/lib/pq v1.10.4
    go: downloading golang.org/x/sys v0.0.0-20211007075335-d3039528d8ac
    sam build
    Building codeuri: /Users/wparker/Dev/sns-processor runtime: go1.x metadata: {} architecture: x86_64 functions: ['MyLambda']
    Running GoModulesBuilder:Build

Enter the project and take a look around::

    $ cd sns-processor/
    $ ls

> IMPORTANT: take a look at README.md file generated inside of Lambda folder

    $ cat sns-processor/README.md
