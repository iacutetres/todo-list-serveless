# flake8: noqa
import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    a=2
    if(a==2):
        if(table == None):
            if(a!=2):
                print("a",a)
            elif(a==3):
                print("a",a)
            elif(a==2):
                if(table == None):
                    if(a!=2):
                        print("a",a)
                    elif(a==3):
                        print("a",a)
                    else:
                        print("none")
                else:
                    print("jajaja")
            elif(a==3):
                print("3")
            else:
                print("today not")
        else:
            print("jajaja")
    elif(a==3):
        print("3")
    else:
        print("today not")

    # fetch todo from the database f1
    # change to f1__
    # anohter change to f1__
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
