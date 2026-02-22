import json
import urllib3
import boto3
import os
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
table = dynamodb.Table('PriceHistory')

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

  
    response = http.request('GET', url)
    price = json.loads(response.data.decode('utf-8'))['bitcoin']['usd']

    table.put_item(
        Item={
            'Timestamp': str(context.aws_request_id),
            'Asset': 'Bitcoin',
            'Price': price
        }
    )


  
    topic_arn = os.environ['SNS_TOPIC_ARN']
    
    if price > 50000:
        message = f"ALARM: Bitcoin has hit ${price}! Time to check your portfolio."
        sns.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject="Price Alert: Bitcoin"
        )
        print("Alert sent via SNS.")

    return {
        'statusCode': 200,
        'body': json.dumps(f"Price recorded: ${price}")
    }
