from __future__ import print_function
import pickle
import os.path

# pip install --upgrade google-api-python-client
# pip install google-auth-oauthlib
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import CommitteeMember

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1-qWpbmCQpEXwN9bP0KoQmMJ4zVY5mkqeaA-oxB4j1I8'
SAMPLE_RANGE_NAME = 'Schedule!A1:H10'

def getCommitteeData(values):
    index = 1
    while (index < len(values) and len(values[index]) > 0):
        print("\n")
        print(values[index])
        full_name = values[index][0]

        phone_number = values[index][1]
        print("pre strip: " + phone_number)
        characters_to_remove = "()- "
        for character in characters_to_remove:
            phone_number = phone_number.replace(character, "")
        print("after strip: " + phone_number)
        # member = CommitteeMember()
        index += 1


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        getCommitteeData(values)

if __name__ == '__main__':
    main()