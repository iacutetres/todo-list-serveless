import json
import logging
import os
import sys
import boto3
sys.path.append(".")
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
    tablename = os.environ['DYNAMODB_TABLE']

    from todoTableClass import todoTable
    # constructor
    create = todoTable(tablename, dynamodb)
    # call function put_todo  with two results
    item, response = create.put_todo(data['text'], None)
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
