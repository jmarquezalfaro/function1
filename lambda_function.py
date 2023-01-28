import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hola Lambda!')
    }
# declare a lambda function
greet = lambda : print('Hello World')

# call lambda function
greet()