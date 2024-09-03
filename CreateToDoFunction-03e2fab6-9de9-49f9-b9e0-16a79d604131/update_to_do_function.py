import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoTable')

def lambda_handler(event, context):
    todo_id = event['pathParameters']['id']
    item = json.loads(event['body'])
    table.update_item(
        Key={'id': todo_id},
        UpdateExpression="set description=:d",
        ExpressionAttributeValues={':d': item['description']},
        ReturnValues="UPDATED_NEW"
    )
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'To-Do item updated'})
    }
