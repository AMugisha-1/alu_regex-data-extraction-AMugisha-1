import re

# Example text to search
text = """
Hello! My email is example@mail.com.
Visit https://example.com for details.
Call me at +1-234-567-8901.
Price: $100.50
"""

# Patterns to find specific data
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
url_pattern = r'https?://\S+'
phone_pattern = r'\+?\d{1,3}[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}'
money_pattern = r'\$\d+(\.\d{2})?'

# Find matches
emails = re.findall(email_pattern, text)
urls = re.findall(url_pattern, text)
phones = re.findall(phone_pattern, text)
money = re.findall(money_pattern, text)

# Print results
print("Emails:", emails)
print("URLs:", urls)
print("Phone Numbers:", phones)
print("Money Amounts:", money)
