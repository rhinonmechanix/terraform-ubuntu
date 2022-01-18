
This script copies defined number of items from one DynamoDB table to another. It covers the following use-cases.

1. Both the tables do not exist
2. Source Table does not exist
3. Destination Table does not exist
4. Both the table exist



**Python Command to the run the script:**
`python main.py -st <sourceTableName>` - This will create two json file dynamoresponse and sourcetable

`python jsonToMain.py -dt <destinationTableName>` - this will upload or copy the following table to destination folder
