from flask import Flask,request,redirect,jsonify
from bs4 import BeautifulSoup
import time
import requests
from selenium import webdriver as wd
import re
app = Flask(__name__)

def scrapetechgig():
    link="https://www.techgig.com/challenge/"
    request=requests.get(link)
    bs=BeautifulSoup(request.content,"html.parser")
    s=bs.find("div",{"id":"live-contest"})
    contests=s.find_all("div",{"class":"contest-box prize-hiring-2"})
    nr=[[]]
    for i in contests:
        j=BeautifulSoup(str(i),"html.parser")
        heading=j.find("h3").getText()
        subheading=j.find("div",{"class":"inner"}).find("p").getText()
        enddate=j.find("dl",{"class":"description-list"}).find_all("dd")[1].getText()
        topic=j.find("div",{"class":"contest-info clearfix"}).find_all("dl",{"class":"description-list"})[0].find_all("dd")[1].getText()
        prize=j.find("div",{"class":"contest-info clearfix"}).find_all("dl",{"class":"description-list"})[1].find("dd").getText()
        url=j.find("a")["href"]
        nr.append([heading,subheading,enddate,topic,prize,url])
    return nr
def scrapehackathon():
    link="https://www.hackathon.com/country/india"
    request=requests.get(link,verify=False)
    bs=BeautifulSoup(request.content,"html.parser")
    contests=bs.find_all("div",{"class":"ht-eb-card"})
    nr=[[]]
    for i in contests:
        j=BeautifulSoup(str(i),"html.parser")
        heading=j.find("a",{"class":"ht-eb-card__title"}).getText()
        subheading=j.find("div",{"class":"ht-eb-card__description"}).getText()
        enddate=j.find("div",{"class":"date"}).getText()
        topic=j.find("div",{"class":"ht-card-tags"}).getText()
        prize=j.find("div",{"class":"ht-eb-card__prize__name"})
        url=j.find("a",{"class":"ht-eb-card__title"})["href"]
        if prize!=None:
            prize=prize.getText()
        else:
            prize="None"
        nr.append([heading,subheading,enddate,topic,prize,url])
    return nr
def scrapehackerearth():
    link="https://www.hackerearth.com/challenges/"
    browser=wd.Chrome()
    browser.get(link)
    res=browser.execute_script("return document.documentElement.outerHTML")
    browser.quit()
    bs=BeautifulSoup(res,"html.parser")
    contests=bs.find_all("div",{"class":"challenge-card-modern"})
    nr=[[]]
    for i in contests:
        j=BeautifulSoup(str(i),"html.parser")
        test=j.find("div",{"class": "challenge-type light smaller caps weight-600"})
        if test!=None:
            if test.getText().strip()=="HACKATHON":
                heading=j.find("span",{"class":"challenge-list-title challenge-card-wrapper"}).getText()
                subheading=j.find("div",{"class":"company-details ellipsis"}).getText().strip()
                enddate=j.find("div",{"id":"days"}).getText()+j.find("div",{"id":"hours"}).getText()+j.find("div",{"id":"minutes"}).getText()
                enddate=enddate.replace('\n'," ")
                topic=heading
                prize="None"
                url=j.find("a",{"class":"challenge-card-wrapper challenge-card-link"})["href"]
                nr.append([heading,subheading,enddate,topic,prize,url])
    return nr
@app.route('/')
def hello():
    main=scrapehackathon()
    main+=scrapetechgig()
    main+=scrapehackerearth()
    main=[value for value in main if value != []]
    contests=[]
    for i in range(len(main)):
        contests.append({x:y for x,y in zip(["ID","Title","Description","Date","Skills","Prize Money","URL"],[i+1]+main[i])})
    return jsonify(contests)
if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.104', port="5000")