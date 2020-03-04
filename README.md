# Rotate Token Example

A simple example written in Python 3 that uses AWS Lambda to perform a task.

Goal: Rotate a Rubrik API token into HashiCorp Vault so that downstream tools can use the token for automated tasks.

1. Store environmental variables stored in the Lambda function using `os.environ` calls.
1. Grab a new Rubrik API token.
1. Store the new Rubrik API token in Vault.
1. Repeat every 24 hours by using a CloudWatch event.

Note: The `requests` module is no longer a part of the `boto3` module set that is native to AWS Lambda. You'll need to use a layer. Either add the module yourself to your own layer or [use someone else's layer](https://github.com/keithrozario/Klayers).
