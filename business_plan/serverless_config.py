```python
import boto3
from serverless import Serverless

# AWS SDK and Boto3 setup
aws_sdk = boto3.Session()
serverless = Serverless(aws_sdk)

# AWS Lambda setup
lambda_function = {
    "name": "AI_Business_Plan",
    "runtime": "python3.8",
    "handler": "main.handler",
    "description": "Lambda function for orchestrating the AI business plan",
    "timeout": 60,
    "memory_size": 128
}

serverless.add_lambda_function(lambda_function)

# AWS API Gateway setup
api_gateway = {
    "name": "AI_Business_Plan_API",
    "description": "API Gateway for the AI business plan",
    "stage_name": "prod",
    "lambda_function": lambda_function["name"]
}

serverless.add_api_gateway(api_gateway)

# Deploy serverless application
serverless.deploy()
```