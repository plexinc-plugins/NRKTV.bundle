﻿# -*- coding: utf-8 -*-

# "THE BEER-WARE LICENSE" (Revision 42):
# eithe and burnbay @plexforums wrote this file.  As long as you retain this
# notice you can do whatever you want with this stuff. If we meet some day,
# and you think this stuff is worth it, you can buy us a beer in return. Eirik H.

# Some of this stuff is from:
# jonklo's NRK Plex plugin: https://github.com/plexinc-plugins/NRK.bundle
# takoi's NRK XBMC plugin: https://github.com/takoi/xbmc-addon-nrk
# Please comply with their licenses, I haven't looked at them yet.

# NRK, if you are watching, don't hesitate to make contact.

from util import *
import httplib, urllib

PROGRAM_URL = Regex('\/program\/([^\/]+)')
PROGRAM_IMAGE_BASE_URL = 'http://nrk.eu01.aws.af.cm/f/%s'
PROGRAM_LETTER_BASE_URL = BASE_URL + '/programmer/%s'
JSON_URL_RECENT = BASE_URL + '/listobjects/recentlysent.json/page/0/100'
JSON_URL_RECENT_SENT_BY_CATEGORY = BASE_URL + '/listobjects/recentlysentbycategory/%s.json/page/0'
JSON_URL_POPULAR_WEEK = BASE_URL + '/listobjects/mostpopular/Week.json/page/0/100'
JSON_URL_POPULAR_MONTH = BASE_URL + '/listobjects/mostpopular/Month.json/page/0/100'
JSON_URL_CATEGORY = BASE_URL + '/listobjects/indexelements/%s/page/0'

def GetRecommended():
    start_page = HTML.ElementFromURL(BASE_URL)

    items = start_page.xpath("//*[@id='recommended-list']/ul/li/div/a")
    titles = []
    urls = []
    thumbs = []
    fanarts = []
    summaries = []
    for item in items:
        urls.append(BASE_URL + item.get('href'))
        titles.append(item.xpath('./div/img')[0].get('alt'))
        Log("NRK - title: " + item.xpath('./div/img')[0].get('alt'))
        thumbs.append(item.xpath('./div/img')[0].get('src'))
        fanarts.append(FanartURL(item.get('href')))
        summaries.append('')

    return titles, urls, thumbs, fanarts, summaries

def GetByLetter(letterUrl):
    Log.Debug("LETTER URL: " + letterUrl)
    return ProgramList(PROGRAM_LETTER_BASE_URL % letterUrl)

def GetMostRecent():
    return JSONList(JSON_URL_RECENT)

def GetMostPopularWeek():
    return JSONList(JSON_URL_POPULAR_WEEK)

def GetMostPopularMonth():
    return JSONList(JSON_URL_POPULAR_MONTH)

def GetSeasons(url):
    Log.Debug("URL: " + url)
    html = HTML.ElementFromURL(url)
    seasons = html.xpath("//noscript/ul[@class='line-sep clearfix']//a[@class='seasonLink']")
    Log.Debug("Seasons: " + str(seasons))
    titles = []
    urls = []
    thumbs = []
    fanarts = []
    summaries = []
    for season in seasons:
        titles.append(L('season_caption') + ' ' + season.xpath('./text()')[0])
        urls.append(BASE_URL + season.get('href'))
        fanarts.append(FanartURL(url.replace(BASE_URL, '')))
        thumbs.append(ThumbURL(url.replace(BASE_URL, '')))
        summaries.append('')
    
    return titles, urls, thumbs, fanarts, summaries

def GetEpisodes(url):
    Log.Debug("URL: " + url)
    html = HTML.ElementFromURL(url)
    episodes = html.xpath("//*[@id='episodeGrid']//tr[@class='episode-row js-click ']//a")
    Log.Debug("Episodes: " + str(episodes))
    titles = []
    urls = []
    thumbs = []
    fanarts = []
    summaries = []
    for episode in episodes:
        titles.append(episode.xpath('./text()')[0])
        urls.append(BASE_URL + episode.get('href'))
        fanarts.append(FanartURL(url.replace(BASE_URL, '')))
        thumbs.append(ThumbURL(url.replace(BASE_URL, '')))
        summaries.append('')
    
    return titles, urls, thumbs, fanarts, summaries