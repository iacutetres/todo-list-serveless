
import os
import json
import logging

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')
translateaws = boto3.client('translate')
comprehend = boto3.client('comprehend')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def comprehendText(data):
    try:
        response=comprehend.detect_dominant_language(Text = data)
        return response['Languages'][0]['LanguageCode']
    except Exception as e:
        logger.error(response)
        raise Exception("[ErrorMessageComprehend]: " + str(e))

def translateText(data,source,target):
    try:
        response=translateaws.translate_text(Text = data,SourceLanguageCode=source, TargetLanguageCode=target)
        return response['TranslatedText']  
    except Exception as e:
        logger.error(response)
        raise Exception("[ErrorMessageTranslate]: " + str(e))
        
# method translate1        
def translate(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    lang = event['pathParameters']['lang']
    

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    
    sourceLang = comprehendText(result['Item']['text'])
    text = translateText(result['Item']['text'],sourceLang, lang)
    r=result['Item']
    # python object to be appended
    l={'lang':lang,'detectedLang':sourceLang,'text':text}
    # appending the data
    r.update(l)
 
    response = {
        "statusCode": 200,
        "body": json.dumps(r,
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
