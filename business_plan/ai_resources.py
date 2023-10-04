```python
import boto3

# Initialize boto3 client for DynamoDB
dynamodb = boto3.resource('dynamodb')

# Define the schema for AI resources
ai_resource_schema = {
    'AttributeName': 'resource_id',
    'AttributeType': 'S'
}

# Create the DynamoDB table for AI resources
def create_ai_resources_table():
    table = dynamodb.create_table(
        TableName='AIResources',
        KeySchema=[
            {
                'AttributeName': 'resource_id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[ai_resource_schema],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return table

# Function to add a new AI resource to the table
def add_ai_resource(resource_id, resource_type, cost):
    table = dynamodb.Table('AIResources')
    response = table.put_item(
        Item={
            'resource_id': resource_id,
            'resource_type': resource_type,
            'cost': cost
        }
    )
    return response

# Function to get an AI resource from the table
def get_ai_resource(resource_id):
    table = dynamodb.Table('AIResources')
    response = table.get_item(
        Key={
            'resource_id': resource_id
        }
    )
    return response['Item']

# Function to delete an AI resource from the table
def delete_ai_resource(resource_id):
    table = dynamodb.Table('AIResources')
    response = table.delete_item(
        Key={
            'resource_id': resource_id
        }
    )
    return response
```