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

func printBucketCredentials(records []events.S3EventRecord) {
	for _, r := range records {
		fmt.Printf("\n Event Record S3 Bucket Name: %s \n", r.S3.Bucket.Name)
		fmt.Printf("\n Event Record S3 Object Key: %s \n", r.S3.Object.Key)
	}

}

func handler(event events.S3Event) (string, error) {
	printBucketCredentials(event.Records)
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
