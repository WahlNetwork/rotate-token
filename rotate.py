import requests
import json
import os

##### Create local variables based on environment variables

# Rubrik Variables
rubrikUrl = os.environ['rubrikBaseUrl'] + os.environ['rubrikEndpoint'] # URL to the Rubrik API
rubrikExpiration = os.environ['rubrikExpiration']                      # Expiration in minutes (1440 = 1 day)
rubrikTag = os.environ['rubrikTag']                                    # Tag to help identify the token
rubrikBasicAuth = 'Basic ' + os.environ['rubrikBasicAuth']             # Creds to auth as the service account in Rubrik

# Vault Variables
vaultUrl = os.environ['vaultUrl']                                      # URL to the Vault API
vaultToken = os.environ['vaultToken']                                  # Token to auth as the service account in Vault

def lambda_handler(event, context):
  
  ##################################################################################################################
  ##### Create the Rubrik payload (body) as a dict
  payload_raw = {'initParams': {'apiToken': {'expiration': int(rubrikExpiration), 'tag': rubrikTag}}}
  payload = json.dumps(payload_raw)

  # Create the Rubrik header using Basic Authentication with Base64 encoded value
  headers = {
    'Authorization': rubrikBasicAuth
  }

  # Create new Rubrik API Token for the service account
  # Note: Due to using a self-signed certificate on the Rubrik demo cluster, verify is set to False
  print('Sending request to Rubrik Cluster C')
  response = requests.post(rubrikUrl, headers=headers, data=payload, verify=False)
  
  # Store the new Rubrik API token by looking inside of the session response details
  token = response.json()['session']['token']
  
  ##################################################################################################################
  ##### Create the Vault payload (body) as a dict using the Rubrik API Token
  payload_raw = {'data': {'token': token}}
  payload = json.dumps(payload_raw)
  
  # Create the Vault header using Basic Authentication Base64 encoded value
  headers = {
    'X-Vault-Token': vaultToken
  }
  
  # Create new Rubrik API Token for the service account
  # Note: Due to using a self-signed certificate on the Vault demo instance, verify is set to False
  print('Sending request to Vault')
  response = requests.post(vaultUrl, headers=headers, data=payload, verify=False)
