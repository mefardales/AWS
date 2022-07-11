import json
import uuid

def lambda_handler(event, context):
    # 1 - Read off the input arguments
    customer_id = event['customerId']
    
    # 2 - Generate a random id
    transactionsId = str(uuid.uuid4())
    
    # 3 - Do some stuff i.e. save to s3, save to dynamodb, etc...
    
    # 4 - Format return response
    return {
        'CustomerId': customer_id,
        'Success': 'true',
        'TransactionsId': transactionsId
    }
    