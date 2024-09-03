import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoTable')

def lambda_handler(event, context):
    todo_id = event['pathParameters']['id']
    result = table.get_item(Key={'id': todo_id})
    item = result.get('Item', {})
    return {
        'statusCode': 200,
        'body': json.dumps({'item': item})
    }
