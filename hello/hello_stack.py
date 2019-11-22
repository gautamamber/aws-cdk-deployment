from aws_cdk import (
    aws_lambda as _lambda,
    core,
    aws_apigateway as apigw
)

class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define aws lambda resource
        my_lambda = _lambda.Function(self, "HelloHandler",
        runtime = _lambda.Runtime.PYTHON_3_6,
        code = _lambda.Code.asset('lambda'),
        handler = 'hello.handler'
        )

        apigw.LambdaRestApi(
            self, "Endpoint",
            handler= my_lambda
        )
