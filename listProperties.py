import json
import boto3
from custom_encoder import CustomEncoder

# Get the service resource and Instantiate a table resource object
dydbTable = boto3.resource('dynamodb').Table('PropertyBasic')

def lambda_handler(event, context):
    
    response = dydbTable.scan()
    result = response['Items']
   
    while 'LastEvaluatedKey' in response:
        response = dydbTable.scan(ExclusiveStartKey = response['LastEvaluatedKey'])
        result.extend(response['Item'])
        
    # The attribute createdAt is Decimal. It is not JSON serializable. 
    # You have to encode it seperately using the for loop.
    
    for item in result:
        item['createdAt'] = json.dumps(item['createdAt'], cls=CustomEncoder)
        
    body = {'properties': result}

    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }