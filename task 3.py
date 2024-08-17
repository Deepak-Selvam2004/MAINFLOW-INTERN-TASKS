import requests
from bs4 import BeautifulSoup
#URL of the webpage to scrape
url=input("Enter the webpage you want to scrape: ")
#send a get  request to the webpage
response=requests.get(url)
#check if the request was successful
if response.status_code==200:
    soup= BeautifulSoup(response.text,'html.parser')
    page_text=soup.get_text()
    links=[a['href']for a in soup.find_all('a',href=True)]
    images=[img['src']for img in soup.find_all('img',src=True)]
#extract all texts, images and links from the webpage
    print("PAGE TEXTS :",page_text)
    print('\n LINKS :')
    for link in links:
        print(link)
    print('\n IMAGES :')
    for image in images:
        print(image)
else:
    print(f"failed to retrieve the webpage. status code:{response.status_code}")