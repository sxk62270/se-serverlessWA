import json
import boto3

# Get the service resource.
dydbTable = boto3.resource('dynamodb').Table('PropertyBasic')

def lambda_handler(event, context):
    item = json.loads(event["body"])
    
    # update attributes of the item in the table using DynamoDB.Table.update_item()
    dydbTable.update_item(
        Key={"pid":event["queryStringParameters"]["pid"]},
        UpdateExpression="set sqft=:sqft, beds=:beds, baths=:baths",
        ExpressionAttributeValues={
            ":sqft": item["sqft"],
            ":beds": item["beds"],
            ":baths": item["baths"]
            },
        ConditionExpression="attribute_exists(pid)",
        ReturnValues="ALL_NEW"          
        )
    
    body = {"result":f'The property is updated.'}
   
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(body)
    }