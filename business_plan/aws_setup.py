```python
import boto3

# AWS SDK and Boto3 initialization
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
region_name = 'YOUR_REGION_NAME'

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# AWS IAM client for setting up permissions
iam = session.client('iam')

# Create a role for Lambda to assume
lambda_role = iam.create_role(
    RoleName='lambda_role',
    AssumeRolePolicyDocument='''{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }'''
)

# Attach the necessary policies to the role
iam.attach_role_policy(
    RoleName='lambda_role',
    PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
)

iam.attach_role_policy(
    RoleName='lambda_role',
    PolicyArn='arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess'
)

iam.attach_role_policy(
    RoleName='lambda_role',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'
)

iam.attach_role_policy(
    RoleName='lambda_role',
    PolicyArn='arn:aws:iam::aws:policy/CloudWatchFullAccess'
)

# Save the role ARN for later use
lambda_role_arn = lambda_role['Role']['Arn']
```