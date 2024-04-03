#!/bin/bash

# Create SQS queue
awslocal sqs create-queue --queue-name sample-queue

# Create DynamoDB table
awslocal dynamodb create-table \
    --table-name global01 \
    --key-schema AttributeName=id,KeyType=HASH \
    --attribute-definitions AttributeName=id,AttributeType=S \
    --billing-mode PAY_PER_REQUEST \
    --region us-east-1

# Execute the command passed to the entrypoint
exec "$@"
