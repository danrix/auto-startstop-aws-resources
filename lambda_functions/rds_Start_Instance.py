from __future__ import print_function
import boto3

# BELOW: EVENT ............................................................... #
#
# { "region": "us-east-1", "instance": "instance_name" }
#
# ABOVE: EVENT ............................................................... #

def lambda_handler(event, context):
    # Prepare rds client and...
    client = boto3.client('rds', region_name=event['region'])
    # initiate stop command
    try:
        client.start_db_instance(
            DBInstanceIdentifier=event['instance']
        )
    except Exception as e:
        print('failed to start instance: {0} {1}'.format(event['instance'],e))
        return 500
    else:
        print('started instance: ', event['instance'])
        return 200