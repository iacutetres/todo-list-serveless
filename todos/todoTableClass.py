import boto3
import time
import uuid
from botocore.exceptions import ClientError


class todoTable(object):

    def __init__(self, table, dynamodb=None):
        self.tableName = table
        if not dynamodb:
            # In this case dynamodb is the name of the docker container
            # when all the containers are in the same network.
            dynamodb = boto3.resource(
                'dynamodb', endpoint_url='http://localhost:8000')
        self.dynamodb = dynamodb

    def create_todo_table(self):
        table = self.dynamodb.create_table(
            TableName=self.tableName,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )

        # Wait until the table exists.
        table.meta.client.get_waiter(
            'table_exists').wait(TableName=self.tableName)
        if (table.table_status != 'ACTIVE'):
            raise AssertionError()

        return table

    def delete_todo_table(self):
        table = self.dynamodb.Table(self.tableName)
        table.delete()

    def put_todo(self, text, id=None):
        table = self.dynamodb.Table(self.tableName)
        timestamp = str(time.time())

        # if id null, generate uuid
        if id is None:
            id = str(uuid.uuid1())

        try:
            item = {
                'id': id,
                'text': text,
                'checked': False,
                'createdAt': timestamp,
                'updatedAt': timestamp
            }
            response = table.put_item(
                Item=item)

        except ClientError as e:
            print("ERROR ClientError:", e.response['Error']['Message'])
        else:
            return item, response

    def get_todo(self, id):
        table = self.dynamodb.Table(self.tableName)

        try:
            response = table.get_item(
                Key={
                    'id': id
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response

    def scan_todo(self):
        table = self.dynamodb.Table(self.tableName)

        try:
            # fetch all todos from the database
            response = table.scan()

        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response

    def update_todo(self, text, id, checked):
        table = self.dynamodb.Table(self.tableName)
        timestamp = str(time.time())

        try:
            response = table.update_item(
                Key={
                    'id': id
                },
                ExpressionAttributeNames={
                    '#todo_text': 'text',
                },
                ExpressionAttributeValues={
                    ':text': text,
                    ':checked': checked,
                    ':updatedAt': timestamp,
                },
                UpdateExpression='SET #todo_text = :text, '
                                 'checked = :checked, '
                                 'updatedAt = :updatedAt',
                ReturnValues='ALL_NEW',
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Attributes']

    def delete_todo(self, id):
        table = self.dynamodb.Table(self.tableName)
        try:
            response = table.delete_item(
                Key={
                    'id': id
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response
