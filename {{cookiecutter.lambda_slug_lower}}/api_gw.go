package main

import (
	"fmt"
	"log"
	"os"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
	"github.com/getsentry/sentry-go"

	_ "github.com/lib/pq"
)

var (
	sentryDsn = os.Getenv("SENTRY_DSN")
)

func checkError(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func printRecordsMessage(records []events.SNSEventRecord) {
	for _, r := range records {
		fmt.Printf("Event Record Message: %s \n", r.SNS.Message)
	}

}

func handler(event events.SNSEvent) (string, error) {
	printRecordsMessage(event.Records)
	return "all good", nil
}

func main() {
	err := sentry.Init(sentry.ClientOptions{
		Dsn:         sentryDsn,
		Environment: "development",
		Debug:       true,
	})
	checkError(err)

	lambda.Start(handler)

}
