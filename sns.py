import requests
import json

url = "https://3u42tnm3ll.execute-api.us-west-2.amazonaws.com/SNS_Sender"

def sendText(recipients, message):
    payload = {"numbers": [], "message": message}
    for number in recipients:
        payload["numbers"].append(number)
    headers = {"username": "sns_api"}
    response = requests.post(url, headers=headers, json=payload)
    return response
