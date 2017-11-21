import boto3
client = boto3.client('lambda')
return_dict = client.invoke(FunctionName='cloud101')
