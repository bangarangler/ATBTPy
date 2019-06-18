#! /usr/bin/env python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-8586, 444-0909, (423) 555-7485, 222-0987 ext 14327, ext., 12345, x12345

(
(\d{3}|(\(\d{3}\))?   # area code (optional)
(\s|-)                # first separator
\d{3}                 # first 3 digits
-                     # separator
\d{4}                 # last 4 digits
(((ext(\.)?\s|x)      # extension word-part (optional)
(\d{2,5}))?            # extension number-part (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
#some.+_thing@something.com

[a-zA-Z0-9_.+]+    # name part
@                  # @ symbol
[a-zA-Z0-9_.+]+   # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the eamil/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = phoneEmail.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# print(extractedPhone)
# print(extractedEmail)

# Copy the extracted email/phone to the clipboard
results = "\n".join(allPhoneNumbers) +  "\n" + "\n".join(extractedEmail)
pyperclip.copy(results)
