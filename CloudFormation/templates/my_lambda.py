from __future__ import print_function
from crhelper import CfnResource
import logging
import boto3
import os

logger = logging.getLogger(__name__)
# Initialise the helper, all inputs are optional, this example shows the defaults
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL')

sns = boto3.client('sns')

try:
    ## Init code goes here
    pass
except Exception as e:
    helper.init_failure(e)


@helper.create
def create(event, context):
    logger.info("Got Create!")
    
    stackName = event['ResourceProperties']['StackName'];
    
    sns.publish(
        Message = "Somebody is creating new Stack! (" + stackName + ")",
        PhoneNumber = os.environ['PHONE']
    )
    
    
    # Optionally return an ID that will be used for the resource PhysicalResourceId, 
    # if None is returned an ID will be generated. If a poll_create function is defined 
    # return value is placed into the poll event as event['CrHelperData']['PhysicalResourceId']
    #
    # To add response data update the helper.Data dict
    # If poll is enabled data is placed into poll event as event['CrHelperData']
    helper.Data.update({"test": "testdata"})
    return "MyResourceId"


@helper.update
def update(event, context):
    logger.info("Got Update")
    # If the update resulted in a new resource being created, return an id for the new resource. CloudFormation will send
    # a delete event with the old id when stack update completes


@helper.delete
def delete(event, context):
    logger.info("Got Delete")
    
    stackName = event['ResourceProperties']['StackName'];
    
    sns.publish(
        Message = "Somebody is deleting  Stack! (" + stackName + ")",
        PhoneNumber = os.environ['PHONE']
    )
    
    # Delete never returns anything. Should not fail if the underlying resources are already deleted. Desired state.


@helper.poll_create
def poll_create(event, context):
    logger.info("Got create poll")
    # Return a resource id or True to indicate that creation is complete. if True is returned an id will be generated
    return True


def handler(event, context):
    helper(event, context)