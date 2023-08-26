from bs4 import BeautifulSoup
import requests
import re
import json

url = 'https://youtu.be/mEPm9w5QlJM?si=dOoRdqZVzoUf6AuW'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

script_tag = soup.find('script')
# print(script_tag)
print('\n')

if script_tag:
    script_string = str(script_tag)
    # print(script_string)
    # print('\n')


# x = soup.find_all('script', {'nonce' : "fBs8pGFUXLS_xwND5wE2Lw"})
# if x:
#     for script in x:
#         print(script)
#         print('\n')
# else:
#     print('no data')

html_string = script_string

# Use regular expression to extract the value of nonce
pattern = r'nonce="([^"]*)"'
match = re.search(pattern, html_string)

if match:
    nonce_value = match.group(1)
    print("Nonce Value:", nonce_value)
else:
    print("Nonce value not found.")


script_data_list = soup.find_all('script', {'nonce' : str(nonce_value)})

print('\n')

# for i,script in enumerate(script_data_list):
#     print(i, script)
#     print('\n')

# print(script_data_list[45])

# print('\n')
# print('\n')

script_data_string = str(script_data_list[45])
#print(script_data_string)

# script_data_json = json.loads(script_data_string)

# label = script_data_json['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']
# simple_text = script_data_json['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['simpleText']

# print("Label:", label)
# print("Simple Text:", simple_text)

# Find the indices of 'label' and 'simpleText'
label_index = script_data_string.find('"label":"')
simple_text_index = script_data_string.find('"simpleText":"')

# Extract the values of 'label' and 'simpleText'
label = script_data_string[label_index + 9 : script_data_string.find('"', label_index + 9)]
simple_text = script_data_string[simple_text_index + 14 : script_data_string.find('"', simple_text_index + 14)]

# Print the extracted values
print("Total Likes:", label)
print("Total Views:", simple_text)

