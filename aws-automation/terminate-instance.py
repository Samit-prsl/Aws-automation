import boto3

client = boto3.client('ec2')
response = client.terminate_instances(
    InstanceIds=[
        'i-05c8b5248db0db3e9',
    ]
)    