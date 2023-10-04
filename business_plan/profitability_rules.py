```python
import boto3
from botocore.exceptions import BotoCoreError, ClientError

# AWS CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Shared variables
initial_investment = 200
target_return = 2000
profitability_threshold = target_return - initial_investment

def calculate_profitability(current_revenue):
    return current_revenue - initial_investment

def monitor_profitability():
    try:
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/Billing',
            MetricName='EstimatedCharges',
            Dimensions=[
                {
                    'Name': 'Currency',
                    'Value': 'USD'
                },
            ],
            StartTime=datetime.datetime.utcnow() - datetime.timedelta(seconds=600),
            EndTime=datetime.datetime.utcnow(),
            Period=60,
            Statistics=[
                'SampleCount', 'Average', 'Sum', 'Minimum', 'Maximum'
            ],
            Unit='None'
        )
        current_revenue = response['Datapoints'][0]['Sum']
        profitability = calculate_profitability(current_revenue)
        
        if profitability < profitability_threshold:
            raise Exception('Profitability threshold not met. Current profitability: {}'.format(profitability))
        
        print('Profitability check passed. Current profitability: {}'.format(profitability))
        
    except BotoCoreError as error:
        print(error)
        return False

    except ClientError as error:
        print(error)
        return False

    return True

monitor_profitability()
```