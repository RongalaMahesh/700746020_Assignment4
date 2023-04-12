import boto3
import configparser


config = configparser.ConfigParser()
config.read('config.ini')


sns = boto3.client('sns')


response = sns.create_topic(
    Name=config['SNS']['topic_name']
)


sns.subscribe(
    TopicArn=response['TopicArn'],
    Protocol='email',
    Endpoint=config['SNS']['email_address']
)
