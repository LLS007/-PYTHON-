# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:07:11 2019

@author: LLS
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 19:56:45 2019

@author: LLS
"""
# date _>>>>>> 10.19

import requests

from bs4 import BeautifulSoup

import os 

import re 


def download_one_page(url):
    
    headers =  {
            
            'Referer':url,
            
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
            }
    
    reponse = requests.get(url,headers=headers)
    
    patterns  =  re.compile('https.*?jpg')
    
    img_links = re.findall(patterns,reponse.text)
    
    for i in img_links:
        
        pic_name = i[-12:-4]
        
        print(pic_name)
        
        img_response =  requests.get(i,headers=headers)
        
        print('正在下载第{}张图'.format(i[-6:-4]))
        
        with open(pic_name+'.jpg','wb') as f:
            
            f.write(img_response.content)
            
            f.close()
        

def get_url(url):
      
    headers = {
            
            'Referer':url,
            
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
            }
    
    response = requests.get(url,headers=headers)
    
    content_links  = BeautifulSoup(response.text,'lxml').find('div',class_='box tu_list').find_all('a')
    
    for content_link in content_links:
        
        content_link = content_link['href']
        
        all_link = '' + str(content_link)
        
        print(all_link)
        
        download_one_page(all_link)
    
    
def main():
    
    for i in range(1,645):
        
        main_url = ''+str(i)+'.htm'
        
        get_url(main_url)

if __name__ == '__main__': 
    main()