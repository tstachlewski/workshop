
import logging
import boto3
import os

logger = logging.getLogger(__name__)


def handler(event, context):
    
    print("My Makro!");
    print(event);
    
    macro_response = {
        "requestId": event["requestId"],
        "status": "success"
        
    }
    
    # Globals
    fragment = event['fragment']
    result = fragment
    templateParameterValues = event['templateParameterValues']

    identifier = templateParameterValues['Identifier'].upper()

    if '%s' in fragment['Description']:
        result['Description'] = fragment['Description'] % identifier

    macro_response['fragment'] = result
    
    return macro_response