!pip install pycountry
!pip install pandas

# Import the required libraries
import pandas as pd
import pycountry

# Load the Google Sheets document into a pandas dataframe
url = "https://docs.google.com/spreadsheets/d/1bM4qcG4ny2ijOCpn9pMt5TWUIGwEFISFG_wlQJHt3O8/export?format=csv"
df = pd.read_csv(url)

# Split the address data into separate columns
df[['Address1','Address2','Address3']] = df['Address'].str.split('\n', n=2, expand=True)

# Extract the country code from the address
df['CountryCode'] = df['Address3'].apply(lambda x: pycountry.countries.search_fuzzy(x)[0].alpha_2 if x else None)

# Remove the country code from the address
df['Address3'] = df['Address3'].str.replace(r',?\s*' + df['CountryCode'] + r'\s*', '')

# Remove any leading or trailing whitespace from the address fields
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Print the cleaned up data
print(df)
