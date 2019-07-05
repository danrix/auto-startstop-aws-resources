from __future__ import print_function
import boto3
import time

# BELOW: EVENT ............................................................... #
#
# { "region": "us-east-1", "instance": "instance_name" }
#
# ABOVE: EVENT ............................................................... #

def lambda_handler(event, context):
    # Prepare timestamp for snapshot name .................................... /
    curr_time = time.gmtime()    
    str_time=time.strftime('%Y-%m-%d-%H-%M', curr_time)

    # Prepare rds client and...
    client = boto3.client('rds', region_name=event['region'])
    # initiate stop command
    try:
        client.stop_db_instance(
            DBInstanceIdentifier=event['instance'],
            DBSnapshotIdentifier=event['instance']+"-"+str_time # Name for snapshot
        )
    except Exception as e:
        print('failed to stop instance: {0} {1}'.format(event['instance'],e))
        return 500
    else:
        print('stopped instance: ', event['instance'])
        return 200