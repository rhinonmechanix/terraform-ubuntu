import boto3
import os
import sys
import argparse
import datetime
import json



global args
parser = argparse.ArgumentParser()

parser.add_argument('-dt', '--destinationTableName', required=True, action="store", dest="destinationTableName",
                    help="Destination AWS Account DyanamoDB Table", default=None) 
parser.add_argument('-r', '--region', required=True, action="store", dest="region",
                    help="Source AWS Account DyanamoDB Table", default=None)
args = parser.parse_args()                                                                                                                       


destinationTableName=args.destinationTableName 

region = args.region

print("Printing values")
print("destinationTableName", destinationTableName)


timeStamp = datetime.datetime.now()
backupName = destinationTableName + str(timeStamp.strftime("-%Y_%m_%d_%H_%M_%S"))

item_count = 1000 #Specify total number of items to be copied here, this helps when a specified number of items need to be copied
counter = 1 # Don't not change this

target_session = boto3.Session(region_name=region)
target_dynamodb = target_session.resource('dynamodb')


dynamoclient = boto3.client('dynamodb', region_name=region) #Specify the region here

dynamotargetclient = boto3.client('dynamodb', region_name=region) #Specify the region here
# response = dynamotargetclient.list_tables()
# print("List of tables", response)

dynamopaginator = dynamoclient.get_paginator('scan')

def validateTables(destinationTable):
    print("Inside validateTables")
    try:
        dynamotargetclient.describe_table(TableName=destinationTable)
        destinationTableExists = "true"
    except dynamotargetclient.exceptions.ResourceNotFoundException:
        destinationTableExists = "false"
    
    return {'destinationTableExists':destinationTableExists}        




def copyToAnother(json1, destinationTable, item_count,counter):
    
    print("Inside copyTable")
    print("Coping", json1, "to", destinationTable)
    
    with open('dynamoresponse.json', 'r') as openfile:
    # Reading from json file
        dynamoresponse = json.load(openfile)
        
    for page in dynamoresponse:
        for item in page['Items']:
            if (counter ==  item_count):
                print("exiting")
                sys.exit()
            else:      
                print('writing item no', counter)
                dynamotargetclient.put_item(
                    TableName=destinationTable,
                    Item=item
                    )   
            counter = counter + 1



def backupTable(destTableName, backupTimeStamp):
    print("Inside backupTable")
    print("Taking backup of = ", destTableName)
    print("Backup Name = ", backupTimeStamp)

    response = dynamotargetclient.create_backup(
        TableName=destTableName,
        BackupName=backupTimeStamp
    )
    print("Backup ARN =", response["BackupDetails"]["BackupArn"])



def doesNotExist():
    print("Inside doesNotExist")
    print("Destination table does not exist ")
    print("Exiting the execution")
    # sys.exit()



result = validateTables( destinationTableName)
print("value of destinationTableExists = ", result['destinationTableExists'])
    


