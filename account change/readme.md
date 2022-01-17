
This script copies defined number of items from one DynamoDB table to another. It covers the following use-cases.

1. Both the tables do not exist
2. Source Table does not exist
3. Destination Table does not exist
4. Both the table exist



**Python Command to the run the script:**
`python copy-dynamodb-table.py -sa <source-account-access-key-here> -ss <source-account-secret-key-here> -da <destination-account-access-key-here> -ds <destination-account-secret-key-here>
bV2A5cMfurscg -st <source-table-name-here> -dt <destination-table-name-here>`