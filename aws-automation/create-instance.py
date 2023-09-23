import boto3

client = boto3.client('ec2')
response = client.run_instances(
     ImageId='ami-0989fb15ce71ba39e',
      InstanceType='t3.micro',
      MaxCount=1,
      MinCount=1,
      KeyName='automation',
       SecurityGroupIds=[
        'sg-065665d59b165b70e',
    ],
    )

for instances in response['Instances']:
    print(instances['InstanceId'],instances['LaunchTime'])