import requests
from bs4 import BeautifulSoup
import re

# URL of the webpage to extract data from
url1 = "https://uit-ci.org/index.php/feed/"

def getfeed(url):
	# Check if the request was successful (status code 200)
	response = requests.get(url)
    print(response)

#    if response.status_code == 200:
    		# Parse the HTML content with BeautifulSoup    
#		coutent = type(BeautifulSoup(response.content,'html.parser'))
#		return BeautifulSoup(response.content, 'html.parser')
#	else:
#    		print(f"Failed to retrieve data, status code: {response.status_code}")

getfeed(url1)

#content = getfeed(url1)
#result = re.search(r'<content:encoded>(.*?)</content:encoded>', content)
#if result:
#    extracted_string = result.group(1)
#    print(extracted_string)  # Output: hey
