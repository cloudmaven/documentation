import boto3
client = boto3.client('lambda', 'us-east-1')
client.trigger('cloud101')
