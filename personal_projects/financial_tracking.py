import os
import sys
import pandas as pd
from datetime import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from dotenv import load_dotenv
import pickle
import json

# Load environment variables
load_dotenv()

# Google Sheets API setup
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
GOOGLE_SHEET_ID = os.getenv('GOOGLE_SHEET_ID')

def get_google_credentials():
    """Get or refresh Google API credentials."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

def get_categories(service):
    """Fetch categories and their keywords from Google Sheet."""
    result = service.spreadsheets().values().get(
        spreadsheetId=GOOGLE_SHEET_ID,
        range='Categories!A2:B'
    ).execute()
    
    categories = {}
    for row in result.get('values', []):
        if len(row) >= 2:
            category = row[0]
            keywords = [k.strip().lower() for k in row[1].split(',')]
            categories[category] = keywords
    
    return categories

def categorize_transaction(description, amount, categories):
    """Categorize a transaction based on its description."""
    description = description.lower()
    for category, keywords in categories.items():
        if any(keyword in description for keyword in keywords):
            return category
    return 'Uncategorized'

def process_bank_statement(csv_path, service, categories):
    """Process the bank statement CSV and categorize transactions."""
    # Read CSV file - adjust column names based on your bank's CSV format
    df = pd.read_csv(csv_path)
    
    # Assuming standard columns - adjust these based on your CSV structure
    required_columns = ['Date', 'Description', 'Amount']
    
    # Verify required columns exist
    if not all(col in df.columns for col in required_columns):
        print("Error: CSV file must contain Date, Description, and Amount columns")
        sys.exit(1)
    
    # Add category column
    df['Category'] = df.apply(
        lambda row: categorize_transaction(row['Description'], row['Amount'], categories),
        axis=1
    )
    
    # Group by category and sum amounts
    summary = df.groupby('Category')['Amount'].sum().reset_index()
    
    # Update Google Sheet with results
    update_google_sheet(service, summary)
    
    return df

def update_google_sheet(service, summary_df):
    """Update Google Sheet with categorized expenses."""
    # Convert DataFrame to values list
    values = [['Category', 'Total Amount']]
    values.extend(summary_df.values.tolist())
    
    # Create a new sheet with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    sheet_name = f'Expenses_{timestamp}'
    
    # Create new sheet
    request_body = {
        'requests': [{
            'addSheet': {
                'properties': {
                    'title': sheet_name
                }
            }
        }]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=GOOGLE_SHEET_ID,
        body=request_body
    ).execute()
    
    # Update the new sheet with values
    range_name = f'{sheet_name}!A1'
    body = {
        'values': values
    }
    service.spreadsheets().values().update(
        spreadsheetId=GOOGLE_SHEET_ID,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()

def main():
    if len(sys.argv) != 2:
        print("Usage: python financial_tracking.py <bank_statement.csv>")
        sys.exit(1)
    
    csv_path = sys.argv[1]
    if not os.path.exists(csv_path):
        print(f"Error: File {csv_path} not found")
        sys.exit(1)
    
    try:
        # Set up Google Sheets API
        creds = get_google_credentials()
        service = build('sheets', 'v4', credentials=creds)
        
        # Get categories from Google Sheet
        categories = get_categories(service)
        
        # Process bank statement
        processed_df = process_bank_statement(csv_path, service, categories)
        
        print("Successfully processed and categorized expenses!")
        print("\nCategory Summary:")
        summary = processed_df.groupby('Category')['Amount'].sum()
        print(summary)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

