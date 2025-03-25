# Financial Expense Tracker

This Python application helps categorize expenses from bank statements (CSV files) using categories defined in a Google Sheet.

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up Google Sheets API:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the Google Sheets API
   - Create credentials (OAuth 2.0 Client ID)
   - Download the credentials JSON file and rename it to `credentials.json`
   - Place the credentials.json file in the project root directory

3. Create a `.env` file with your Google Sheet ID:
   ```
   GOOGLE_SHEET_ID=your_sheet_id_here
   ```

## Usage

1. Prepare your Google Sheet with the following structure:
   - Sheet named "Categories" with columns:
     - Category
     - Keywords (comma-separated keywords that identify this category)

2. Place your bank statement CSV file in the project directory

3. Run the script:
   ```bash
   python financial_tracking.py your_statement.csv
   ```

The script will:
- Read your bank statement CSV
- Match transactions against your defined categories
- Update your Google Sheet with categorized expenses 