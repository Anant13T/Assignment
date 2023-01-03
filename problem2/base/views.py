from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
import json
from lxml import etree ,html
import lxml.html



@api_view(['GET'])
def getData(request,id:str):
    url = requests.get(" https://en.wikipedia.org/wiki/"+id)
    res=url.content
    soup = BeautifulSoup(res, "html.parser")
    lst=[]
    covers = soup.select('table.infobox a.image img[src]')
    for cover in covers:
        lst.append("https:"+cover['src'])
    flag_link=lst[0]
  
    store = html.fromstring(url.text) 

    output = store.xpath('//td[@class="nickname"]')  
    for x in output:
        print(x.text.strip())

    capital = store.xpath('//table[@class="infobox ib-country vcard"]//tr[th/text()="Capital"]/td/a')
    a=capital[0].text

    Largest= store.xpath('//table[@class="infobox ib-country vcard"]//tr[th/text()="Largest city"]/td/a')
    b=Largest[0].text

    content={'flag_link':flag_link,
             'capital':a,
             'largest city':b}

    return Response(content)