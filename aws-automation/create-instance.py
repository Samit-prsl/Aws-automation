import boto3

client = boto3.client('ec2')
response = client.run_instances(
     ImageId='ami-0f5ee92e2d63afc18',
      InstanceType='t2.micro',
      MaxCount=1,
      MinCount=1,
    )

for instances in response['Instances']:
    print(instances['InstanceId'],instances['LaunchTime'])