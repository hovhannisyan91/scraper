from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd
import re
import requests
# import socks
# import socket

# socks.set_default_proxy(socks.SOCKS5, 'localhost', 9150)
# socket.socket = socks.socksocket


class LinkedIn():
    pass   

class Spyur:

    def __init__(self,url) -> None:
        self.url = url
        self.urls=[]
        self.data = {}
        # self.table=pd.DataFrame([self.data])
        self.response=requests.get(self.url)
        self.html_content = self.response.content
        self.soup=BeautifulSoup(self.html_content,'html.parser')

    def _get_urls(self)->list: 

        results_div=self.soup.find('div', class_='results_list')
        links = results_div.find_all('a')
        self.urls=['https://www.spyur.am/'+i['href'] for i in links]
        
    def get_name(self):
        self.data['Name']=self.soup.find('h1', class_='page_title').text.strip()

    def get_address(self):
        try:
            tag=self.soup.find('div', class_='address_block').text.strip()
            lines=tag.split('\n')

            if lines:
                first_line_elements = lines[0].split(',')

                self.data['Country']=first_line_elements[0]
                self.data['Zip Code']=first_line_elements[1]
                self.data['City']=first_line_elements[2]
                self.data['Street Address']=lines[1]
                self.data['District']=self.soup.find('div', class_='destriction_block').text.strip()
        except:
            SyntaxError
    

    def get_phone(self):
        
        try:
            tag=self.soup.find('div', class_='phone_info').text.strip()
            lines=tag.split('\n')
            for index,value in enumerate(lines,start=1):
                self.data[f'Phone Number {index}']=''.join(re.findall(r'\d+',value))
        except:
            SyntaxError
    
    def e_addresses(self):
        try:
            self.data['Website']=self.soup.find('a', class_='web_link').text.strip()
            self.data['Facebook']=self.soup.find('a', class_='web_link facebook_link')['href']
            self.data['Instagram']=self.soup.find('a', class_='web_link instagram_link')['href']
            self.data['YouTube']=self.soup.find('a', class_='web_link youtube_link')['href']
        except:
            SyntaxError


if __name__=='__main__':
    counter=1
    ListOfAllUrls=[]
    # industry={
    #     'esthetics':' https://www.spyur.am/am/yellow_pages-{counter}/yp/2682/ '
    # }
    while counter<4:
        #! Clinics
        #! Plastic surgery
        #! Hair
        url=f'https://www.spyur.am/am/home/search-{counter}/?company_name=%D4%B7%D5%BD%D5%A9%D5%A5%D5%BF%D5%AB%D5%AF+%D5%A2%D5%AA%D5%B7%D5%AF%D5%B8%D6%82%D5%A9%D5%B5%D5%A1%D5%B6+%D5%AF%D5%A5%D5%B6%D5%BF%D6%80%D5%B8%D5%B6'
        Inst=Spyur(url)
        Inst._get_urls()
        ListOfAllUrls.append(Inst.urls)
        counter+=1


    ListOfUrls=[i for sublist in ListOfAllUrls for i in sublist]
    len(ListOfUrls)


    L=[]
    for i in ListOfUrls:
        CompN=Spyur(i)
        # print(i)
        CompN.get_name()
        CompN.get_address()
        CompN.get_phone()
        CompN.e_addresses()
        L.append(pd.DataFrame([CompN.data]))
    
    data=pd.concat(L)
    print(data.shape)
    data.to_csv('spyur_data_esthetic.csv',index=False)