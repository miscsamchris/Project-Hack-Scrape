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
def scraped2c():
    link="https://dare2compete.com/e/hackathons/ending"
    browser=wd.Chrome()
    browser.get(link)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    res=browser.execute_script("return document.documentElement.outerHTML")
    browser.quit()
    bs=BeautifulSoup(res,"html.parser")
    contests=bs.find_all("div",{"class":"search-listing-wrapper clearfix ng-star-inserted"})
    nr=[[]]
    for i in contests:
        j=BeautifulSoup(str(i),"html.parser")
        heading=j.find("span",{"class":"mr-5"}).getText()
        subheading=j.find("p",{"class":"single-wrap ng-star-inserted"}).getText().strip()
        enddate=j.find("span",{"class":"center-align ng-star-inserted"}).getText()
        enddate=enddate.replace('\n'," ")
        topic=j.find("div",{"class":"single-wrap"}).getText()
        topic=topic.replace('#',"")
        prize="None"
        url=link
        nr.append([heading,subheading,enddate,topic,prize,url])
    return nr
def scrapeav():
    link="https://datahack.analyticsvidhya.com/contest/all/"
    browser=wd.Chrome()
    browser.get(link)
    res=browser.execute_script("return document.documentElement.outerHTML")
    browser.quit()
    bs=BeautifulSoup(res,"html.parser")
    contests=bs.find_all("div",{"class":"contest__details infinite-item"})
    nr=[[]]
    for i in contests:
        j=BeautifulSoup(str(i),"html.parser")
        test=j.find("div",{"class": "tags--upcoming"})
        if test!=None:
            if test.getText().strip()=="Upcoming":
                heading=j.find("span",{"class":"name"}).getText()
                subheading="None"
                enddate=j.find("div",{"class":"contest__details--body"}).find_all("p")[0].getText().strip("\n")
                topic="Machine Learning AI"
                prize=j.find("div",{"class":"contest__details--body"}).find_all("p")[1].getText().strip("\n")
                url="https://datahack.analyticsvidhya.com"+j.find("a",{"class":"contest__details__link"})["href"]
                nr.append([heading,subheading,enddate,topic,prize,url])
    return nr
def scrapeskill():
    link="https://skillenza.com"
    browser=wd.Chrome()
    browser.get(link)
    login=browser.find_element_by_id("navbar")
    l=login.find_elements_by_tag_name("li")[2]
    l.click()
    time.sleep(3)
    username = browser.find_element_by_name('username')
    username.send_keys('dummyaccount')    
    password = browser.find_element_by_name('password')
    password.send_keys('niceandeasy')
    form=browser.find_element_by_name('loginForm')
    sub=form.find_elements_by_tag_name('button')[2]
    sub.click()
    time.sleep(3)
    browser.get(link+"/activities")
    for i in range(15):
        browser.execute_script("window.scrollTo(0, document.getElementsByClassName('live-activities animated fadeIn')[0].scrollHeight);")
        time.sleep(2)
        browser.execute_script("window.scrollTo(0, document.getElementsByClassName('navbar-header')[0].scrollHeight);")
        time.sleep(1)
    res=browser.execute_script("return document.documentElement.outerHTML")
    browser.quit()
    bs=BeautifulSoup(res,"html.parser")
    contests=bs.find_all("a",{"class":"activity-card ng-scope margin-rb"})
    contests+=bs.find_all("a",{"class":"activity-card ng-scope margin-sb"})
    contests+=bs.find_all("a",{"class":"activity-card ng-scope margin-lb"})
    nr=[[]]
    for i in contests:
        j=BeautifulSoup(str(i),"html.parser")
        test=j.find("div",{"class": "activity-name ng-binding"}).getText()
        if "athon" in test.lower() or  "hack" in test.lower() or "innovation" in test.lower():
                heading=j.find("div",{"class":"activity-name ng-binding"}).getText()
                subheading="None"
                enddate=j.find("div",{"class":"activity-stage-date ng-binding"}).getText().strip("\n")
                topic=j.find("div",{"class":"activity-tags"}).getText()
                prize="None"
                url="https://skillenza.com"+j.find("a")["href"]
                nr.append([heading,subheading,enddate,topic,prize,url])
    return nr
@app.route('/')
def hello():
    main=scrapehackathon()
    main+=scrapetechgig()
    main+=scrapehackerearth()
    main+=scraped2c()
    main+=scrapeav()
    main+=scrapeskill()
    main=[value for value in main if value != []]
    contests=[]
    for i in range(len(main)):
        contests.append({x:y for x,y in zip(["ID","Title","Description","Date","Skills","Prize Money","URL"],[i+1]+main[i])})
    return jsonify(contests)
if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.104', port="5000")