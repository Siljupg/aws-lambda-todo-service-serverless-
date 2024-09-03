import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoTable')

def lambda_handler(event, context):
    item = json.loads(event['body'])
    item['id'] = str(uuid.uuid4())
    table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'To-Do item created', 'item': item})
    }
