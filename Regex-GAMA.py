import re

sample_text = '''
user@example.com
firstname.lastname@company.co.uk
https://www.example.com
http://subdomain.example.org/page
(123) 456-7890
123-456-7890
123.456.7890
1234 5678 9012 3456
1234-5678-9012-3456
14:30
2:30 PM
<p>
<div class="example">
<img src="image.jpg" alt="description">
#example
#ThisIsAHashtag
$19.99
$1,234.56
'''

patterns = {
    "Email addresses": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    "URLs": r'https?://[a-zA-Z0-9./-]+',
    "Phone numbers (various formats)": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    "Credit card numbers": r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}',
    "Time": r'\b\d{1,2}:\d{2}(?:\s?[APMapm]{2})?\b',
    "HTML tags": r'<[^>]+>',
    "Hashtags": r'#\w+',
    "Currency amounts": r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
}

for category, pattern in patterns.items():
    matches = re.findall(pattern, sample_text)
    print(f"- {category}:")
    for match in matches:
        print(f"  ○ {match}")
    print()
