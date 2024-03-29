#Tally Export should be in xml file format.

import xml.etree.ElementTree as ET
import pandas as pd

def parse_element(element):
    data = {}
    if element.text:
        data[element.tag] = [element.text.strip()]
    else:
        data[element.tag] = ['']
    for child in element:
        child_data = parse_element(child)
        for key, value in child_data.items():
            if key in data:
                data[key].extend(value)
            else:
                data[key] = value
    return data

# Read XML file
tree = ET.parse(r'path to Tally Exported xmlfile.xml')
root = tree.getroot()

# Parse XML data
data = parse_element(root)

# Find the maximum length among the lists
max_length = max(len(value) for value in data.values())

# Pad the shorter lists with empty strings
for key, value in data.items():
    if len(value) < max_length:
        data[key].extend([''] * (max_length - len(value)))

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(data)

# Write DataFrame to Excel file
df.to_excel(r'Path to save the Structured Data Excel file.xlsx', index=False)
