import boto3
import os
import sys
import argparse
import datetime
import json



global args
parser = argparse.ArgumentParser()

parser.add_argument('-st', '--sourceTableName', required=False, action="store", dest="sourceTableName",
                    help="Source AWS Account DyanamoDB Table", default=None)
parser.add_argument('-r', '--region', required=True, action="store", dest="region",
                    help="Source AWS Account DyanamoDB Table", default=None)
args = parser.parse_args()                                                                                                                       




sourceTableName=args.sourceTableName 
destinationTableName=args.destinationTableName 

region = args.region

sourceTableExists = "false" 
destinationTableExists = "false" 

print("Printing values")
print("sourceTableName", sourceTableName)
print("destinationTableName", destinationTableName)


timeStamp = datetime.datetime.now()
backupName = destinationTableName + str(timeStamp.strftime("-%Y_%m_%d_%H_%M_%S"))

item_count = 1000 #Specify total number of items to be copied here, this helps when a specified number of items need to be copied
counter = 1 # Don't not change this

source_session = boto3.Session(region_name=region)
source_dynamo_client = source_session.client('dynamodb')

target_session = boto3.Session(region_name=region)
target_dynamodb = target_session.resource('dynamodb')


dynamoclient = boto3.client('dynamodb', region_name=region) #Specify the region here

dynamotargetclient = boto3.client('dynamodb', region_name=region) #Specify the region here
# response = dynamotargetclient.list_tables()
# print("List of tables", response)

dynamopaginator = dynamoclient.get_paginator('scan')

def validateTables(sourceTable):
    print("Inside validateTables")
    try:
        dynamoclient.describe_table(TableName=sourceTable)
        sourceTableExists = "true"
    except dynamotargetclient.exceptions.ResourceNotFoundException:
        sourceTableExists = "false"
    
    return {'sourceTableExists': sourceTableExists}        



def copyTable(sourceTable, json1, item_count):
    
    print("Inside copyTable")
    print("Coping", sourceTable, "to", json1)

    print('Start Reading the Source Table')
    try:
            dynamoresponse = dynamopaginator.paginate(
            TableName=sourceTable,
            Select='ALL_ATTRIBUTES',
            ReturnConsumedCapacity='NONE',
            ConsistentRead=True
        )
    except dynamotargetclient.exceptions.ResourceNotFoundException:
        print("Table does not exist")
        print("Exiting")
        sys.exit()

    print('Finished Reading the Table')
    print("Writing first", item_count , "items" )
    print(dynamoresponse)
    
    with open("Dynamoresponse.json", "w") as outfile:
        json.dump(dynamoresponse, outfile)
        
    with open("sourceTable.json", "w") as outfile:
        json.dump(sourceTable, outfile)


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


result = validateTables(sourceTableName, destinationTableName)
print("value of sourceTableExists = ", result['sourceTableExists'])
print("value of destinationTableExists = ", result['destinationTableExists'])

if (result['sourceTableExists'] == "false" ) and (result['destinationTableExists'] == "false" ):
    print("Both the tables do not exist")

elif (result['sourceTableExists'] == "false" ) and (result['destinationTableExists'] == "true" ):
    print("Source Table does not exist")

elif (result['sourceTableExists'] == "true" ) and (result['destinationTableExists'] == "false" ):
    copyTable(sourceTableName, destinationTableName, item_count )

elif (result['sourceTableExists'] == "true" ) and (result['destinationTableExists'] == "true" ):
    backupTable(destinationTableName, backupName)
    copyTable(sourceTableName, destinationTableName, item_count)

else:
    print("Something is wrong")
    


