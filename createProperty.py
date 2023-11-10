import json
import time
import uuid
import boto3

# Get the service resource.
dydbTable = boto3.resource('dynamodb').Table('PropertyBasic')

def lambda_handler(event, context):
    item = json.loads(event["body"])
    
    #Add p_id, timestamp, and userid to the dictionary
    #Unique identifier for property
    p_id = uuid.uuid4()
    timestamp = int(time.time() * 1000)    
    item["pid"]=str(p_id)
    item["createdAt"]=timestamp
    # item["userid"] = event.requestContext.authorizer.claims.sub

    dydbTable.put_item(Item=item)
    
    body = {"result":f'The property at {item["str_address"]} is added.'}
   
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(body)
    }