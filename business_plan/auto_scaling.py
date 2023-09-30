```python
import boto3

# AWS SDK and Boto3 for interacting with AWS services
client = boto3.client('autoscaling')

# Define the auto scaling group
def create_auto_scaling_group():
    response = client.create_auto_scaling_group(
        AutoScalingGroupName='AIResourcesScalingGroup',
        LaunchConfigurationName='AILaunchConfig',
        MinSize=1,
        MaxSize=5,
        DesiredCapacity=1,
        AvailabilityZones=['us-west-2a'],
        Tags=[
            {
                'Key': 'Name',
                'Value': 'AIResourcesScalingGroup',
                'PropagateAtLaunch': True
            },
        ]
    )
    return response

# Define the scaling policy
def create_scaling_policy():
    response = client.put_scaling_policy(
        AutoScalingGroupName='AIResourcesScalingGroup',
        PolicyName='ScaleBasedOnLoad',
        PolicyType='TargetTrackingScaling',
        TargetTrackingConfiguration={
            'PredefinedMetricSpecification': {
                'PredefinedMetricType': 'ASGAverageCPUUtilization'
            },
            'TargetValue': 50.0,
            'DisableScaleIn': False
        }
    )
    return response

# Main function to setup auto scaling
def setup_auto_scaling():
    create_auto_scaling_group()
    create_scaling_policy()

# Call the main function
if __name__ == "__main__":
    setup_auto_scaling()
```