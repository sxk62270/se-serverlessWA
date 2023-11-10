import json
import boto3

# Get the service resource and stantiate a table resource object
dydbTable = boto3.resource('dynamodb').Table('PropertyBasic')

def lambda_handler(event, context):

    dydbTable.delete_item(
        Key={
        "pid":event["queryStringParameters"]["pid"]
           }
    )
    
    body = {"result":"The property is deleted"}
   
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(body)
    }