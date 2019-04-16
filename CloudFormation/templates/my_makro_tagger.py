
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
    
    
    
    resources = event['fragment']['Resources'];
    for key in resources:
        
        if resources[key]['Type'] in ['AWS::EC2::Subnet', 'AWS::EC2::VPC','AWS::EC2::RouteTable', 'AWS::EC2::InternetGateway']:
            tag_key = 'Name';
            tag_value = {'Fn::Sub': '${AWS::StackName}-' + key}
            tag = {'Key' : tag_key, 'Value' : tag_value};
            
            if 'Properties' not in resources[key]:
                resources[key]['Properties'] = {}
                
            resources[key]['Properties']['Tags'] = []
            resources[key]['Properties']['Tags'].append(tag);
    

    macro_response['fragment'] = event['fragment']
    
    print(macro_response);
    
    return macro_response
