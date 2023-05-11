Address Data Cleaner
This is a Python script that cleans up messy address data in an Excel spreadsheet.

Dependencies
This script requires the following dependencies:

pandas
pycountry
You can install these dependencies using pip:

Copy code
pip install pandas pycountry
Usage
To use this script, follow these steps:

Create a new Google Sheets document with the messy address data you wish to clean.
Share the Google Sheets document with the email address associated with your Google API credentials.
Copy the ID of the Google Sheets document from the URL (e.g. https://docs.google.com/spreadsheets/d/{DOCUMENT_ID}/edit).
Paste the Google Sheets document ID into the url variable in the script.
Run the script using Python.
The script will clean up the address data in the Google Sheets document and print the cleaned up data to the console.

Customization
You can customize this script to handle different formats of address data by modifying the following code:

To split the address data into different columns, modify the split() function in the line df[['Address1','Address2','Address3']] = df['Address'].str.split('\n', n=2, expand=True).
To extract the country code from the address data in a different way, modify the apply() function in the line df['CountryCode'] = df['Address3'].apply(lambda x: pycountry.countries.search_fuzzy(x)[0].alpha_2 if x else None).
To remove different patterns from the address data, modify the replace() function in the line df['Address3'] = df['Address3'].str.replace(r',?\s*' + df['CountryCode'] + r'\s*', '').
License
This script is licensed under the MIT License. See the LICENSE file for more information.
