import boto3

# Get the service resource.
dydb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dydb.create_table(
    TableName='PropertyBasic',
    KeySchema= [ {
            'AttributeName': 'pid',
            'KeyType': 'HASH'
        } ],
    AttributeDefinitions = [  {
    'AttributeName': 'pid',
    'AttributeType': 'S'
        }
    ],
     ProvisionedThroughput = {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
        }
)

# Wait until the table exists.
table.wait_until_exists()