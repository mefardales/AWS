import json
import boto3

client = boto3.client('lambda')

def lambda_handler(event, context):
    input_invoker = {'CustomerId': '123', 'Amount': 50 }
    
    response = client.invoke(
        FunctionName='arn:aws:lambda:us-east-2:567081162678:function:lambdaToInvoke',
        InvocationType='RequestResponse',
        Payload=json.dumps(input_invoker)
    )
    
    responseJson = json.loads(response['Payload'])
    
    print('\n')
    print(responseJson)
    print('\n')