import boto3

import config
import homepage

from flask import Flask

def create_app(test_config=None):

    dynamo_client = boto3.client('dynamodb', region_name='us-east-1')
    dynamoTableName = ''
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = config.SECRET_KEY,
    )

    app.register_blueprint(homepage.bp)

    return app

app = create_app()

