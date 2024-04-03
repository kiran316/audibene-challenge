import boto3

# Initialize SQS and DynamoDB clients with LocalStack endpoint URL and specify the region
sqs = boto3.client('sqs', endpoint_url='http://localhost:4566', region_name='us-east-1')
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566', region_name='us-east-1')

# Specify the SQS queue URL
queue_url = 'http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/sample-queue'

# Specify the DynamoDB table name
table_name = 'global01'
table = dynamodb.Table(table_name)

while True:
    # Receive messages from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=20  # Adjust as needed
    )

    if 'Messages' in response:
        for message in response['Messages']:
            # Process message
            print("Received message:", message['Body'])

            # Parse message body
            message_body = message['Body']
            parsed_data = {}

            # Split message body if it contains the delimiter
            if ',' in message_body:
                parsed_data['id'] = message_body.split(',')[0]  # Assuming the ID is the first attribute
                parsed_data['other_attribute'] = message_body.split(',')[1]  # Assuming the other attribute is the second attribute
            else:
                parsed_data['id'] = message_body  # Set the entire message body as ID if no delimiter is found

            # Store parsed data in DynamoDB
            table.put_item(
                Item=parsed_data
            )

            # Delete message from queue after processing
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )
