# alu_regex-data-extraction-AMugisha-1
# **Regex-Based Data Extraction System**

## **Overview**
The **Regex-Based Data Extraction System** is a Python-based tool designed to extract structured data from unstructured text using **Regular Expressions (Regex)**. It identifies and extracts information such as **emails, URLs, phone numbers, credit card numbers, time formats, HTML tags, hashtags, and currency amounts**, making it useful for **data processing, web scraping, validation, and cybersecurity applications**.

---

## **Project Objectives**
- Extract **specific types of data** using regex patterns.
- Format extracted data in a **structured and readable format**.
- Demonstrate **regex proficiency** in real-world scenarios.
- Provide a **simple, reusable Python implementation**.

---

## **How It Works**
### **Step 1: Input Text (Unstructured Data)**
The system processes a given block of text that contains different data types such as:
- **Emails**
- **URLs**
- **Phone numbers**
- **Credit card numbers**
- **Time formats**
- **HTML tags**
- **Hashtags**
- **Currency amounts**

### **Step 2: Define Regex Patterns**
Each data type has a corresponding **regex pattern** to identify and extract relevant information efficiently.

### **Step 3: Extract Data Using `re.findall()`**
Python’s built-in `re` module scans the text and extracts matching patterns.

### **Step 4: Format the Extracted Data**
The extracted data is displayed in a **structured report format**, ensuring clarity and easy interpretation.

### **Step 5: Output the Results**
The extracted information is printed in a structured format similar to a bullet-point report.

---

## **Technologies Used**
- **Programming Language:** Python 3
- **Library:** `re` (Regular Expressions)

---

## **Regex Patterns Used**

| **Data Type** | **Regex Pattern** | **Description** |
|--------------|-----------------|----------------|
| **Emails** | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` | Matches standard email formats |
| **URLs** | `https?://[a-zA-Z0-9./-]+` | Matches both HTTP and HTTPS URLs |
| **Phone Numbers** | `\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}` | Supports multiple phone formats |
| **Credit Card Numbers** | `\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}` | Matches credit card formats with spaces or dashes |
| **Time** | `\b\d{1,2}:\d{2}(?:\s?[APMapm]{2})?\b` | Supports 12-hour and 24-hour formats |
| **HTML Tags** | `<[^>]+>` | Extracts HTML elements like `<p>` or `<img>` |
| **Hashtags** | `#\w+` | Extracts hashtags such as `#ExampleTag` |
| **Currency Amounts** | `\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?` | Matches currency values like `$19.99`, `$1,234.56` |

---

## **Installation & Usage**
### **Prerequisites**
Ensure you have Python installed on your system.

### **Installation**
Clone the repository:
```bash
$ git clone https://github.com/yourusername/regex-data-extraction.git
$ cd regex-data-extraction
```

### **Usage**
Run the script:
```bash
$ python regex_extractor.py
```

---

## **Code Implementation**
```python
import re

# Sample text input containing different data types
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

# Dictionary containing regex patterns for each data type
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

# Extract and print data in the desired format
for category, pattern in patterns.items():
    matches = re.findall(pattern, sample_text)
    print(f"- {category}:")
    for match in matches:
        print(f"  ○ {match}")
    print()
```

---

## **Expected Output**
```
- Email addresses:
  ○ user@example.com
  ○ firstname.lastname@company.co.uk

- URLs:
  ○ https://www.example.com
  ○ http://subdomain.example.org/page

- Phone numbers (various formats):
  ○ (123) 456-7890
  ○ 123-456-7890
  ○ 123.456.7890

- Credit card numbers:
  ○ 1234 5678 9012 3456
  ○ 1234-5678-9012-3456

- Time:
  ○ 14:30
  ○ 2:30 PM

- HTML tags:
  ○ <p>
  ○ <div class="example">
  ○ <img src="image.jpg" alt="description">

- Hashtags:
  ○ #example
  ○ #ThisIsAHashtag

- Currency amounts:
  ○ $19.99
  ○ $1,234.56
```

---

## **Use Cases & Applications**
- **Web Scraping & Data Extraction**
- **Form Validation**
- **Data Cleaning & Preprocessing**
- **Cybersecurity & Threat Detection**

---

## **Future Enhancements**
- Read from external files or APIs.
- Implement real-time validation.
- Optimize regex patterns for more complex edge cases.

��� **GAMA wishes you well!** ���


