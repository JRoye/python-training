import numpy as np
import pandas as pd
import logging
import re as regex
from validate_email import validate_email

# Variables for characters
passRegex = r"^(?!.*\s)(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,50}$"
nameRegex = r"^[a-zA-Z0-9\s\-]{2,80}$"

# Read in json file to dataframe df variable
# Read in data as a string
df = pd.read_json('93.json', dtype={'string'})

file = open("ErrorLog.txt", "w")

# Data validation check for columns
df['accountValid'] = df['account'].str.contains(nameRegex, regex=True)
df['userNameValid'] = df['userName'].str.contains(nameRegex, regex=True)
df['valid_email'] = df['email'].apply(lambda x: validate_email(x))
df['valid_number'] = df['phone'].apply(lambda x: len(str(x)) == 11)

# Prepend 86 to phone number column
df['phone'] = ('86' + df['phone'])

# Convert dataframe to csv file
df.to_csv('test.csv', index=False)
