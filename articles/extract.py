import subprocess
import requests
import re
from bs4 import BeautifulSoup
def keywordGoSch(list):
#função para tornar uma list de keywords em forma de string
#de forma a poder ser usado o url de pesquisa no GoogleScholar
	output = '+'.join(list)
	return output



print("-------------------- \n script \n ------------------------")

#Aqui vamos fazer uma lista de keywords para pesquisar no google scholar com
keyword = ["pornografia","8ºano"]


url = "https://scholar.google.com/scholar?hl=pt-PT&as_sdt=0%2C5&q=" + keywordGoSch(keyword) + "&btnG="


# command = ["curl","-A","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKi"t/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",url]
# command = ["curl","-e", "http://example.com", url]


#result = subprocess.run(command, capture_output=True, shell = True, text = True)

result = requests.get(url)

string_f_url = result.text   # .stdout in subprocess.run(["curl", url])
#string_f_url = '<a href="https://example.com" data-clk="someData">Link</a>' 

#matches = re.findall(r"href=(.*?)data-clk", string_f_url) 
matches = re.findall(r"https://scholar.googleusercontent.com/scholar(.*?)\" class=\"gs_or_nvi\">", string_f_url)


for match in matches:
# aqui estamos a aceder a cada resultado da pesquisa usando os
# keywords. Agora necessitamos de dar output destes num ficheiro texto.
	url = "https://scholar.googleusercontent.com/scholar"+ match
	content = requests.get(url).text
	soup = BeautifulSoup(content, 'html.parser')
	print(soup.find_all('div'))
	print(type(soup))
