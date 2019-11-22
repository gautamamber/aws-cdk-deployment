import json
def handler(event, context):
    print("Hello from lambda")
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": 'Hello, CDK! You have hit {}\n'.format(event['path'])
    }
    return response