import requests
import json


def sendEmail(recipients, subject, message):
    payload = {"emails": [], "subject": subject, "message": message}
    for number in recipients:
        payload["emails"].append(number)
    headers = {"username": "ses_api"}
    url = "https://3u42tnm3ll.execute-api.us-west-2.amazonaws.com/Email_Sender"
    response = requests.post(url, headers=headers, json=payload)
    return response


if __name__ == "__main__":
    import sys
    if (len(sys.argv) > 1):
        recipients = [sys.argv[1]]
    else:
        recipients = ["apond308@gmail.com"]
    sendEmail(recipients, "Test Email", "This is a test email.")
