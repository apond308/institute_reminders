import requests
import json

url = "https://3u42tnm3ll.execute-api.us-west-2.amazonaws.com/Email_Sender"

def sendEmail(recipients, subject, message):
    payload = {"emails": [], "subject": subject, "message": message}
    for number in recipients:
        payload["emails"].append(number)
    headers = {"username": "ses_api"}
    response = requests.post(url, headers=headers, json=payload)
    return response
    