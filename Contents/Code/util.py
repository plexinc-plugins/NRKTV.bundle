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

import re

VIDEO_PREFIX = "/video/nrktv"

NAME = unicode(L('title'))

BASE_URL = "http://tv.nrk.no"
JSON_URL_MEDIAELEMENT = 'http://v7.psapi.nrk.no/mediaelement/%s'
# make sure to replace artwork with what you want
# these filenames reference the example files in
# the Contents/Resources/ folder in the bundle
ART_DEFAULT  = 'art-default.png'
ICON_DEFAULT = 'icon-default.png'

def pluginRoute(route):
    return VIDEO_PREFIX + route

@route(pluginRoute('/dev/null'))
def DoNothing():
    return

def emptyItem():
    return PopupDirectoryObject(
            key = Callback(DoNothing),
            title=unicode(L("empty_title")),
            summary=unicode(L("empty_description")),
            thumb='')
            
def JSONList(url):
    #Log.Debug("URL: " + url)
    if '/indexelements/' in url: #Get index
        splitUrl = url.split('/')
        index = int(splitUrl[len(splitUrl)-1])
        category = splitUrl[len(splitUrl)-3]
    else:
        index = -1
        category = ''
        
    titles = []
    urls = []
    thumbs = []
    fanarts = []
    summaries = []

    try:
        elems = JSON.ObjectFromURL(url)['Data']

        if index != -1: #No category
            for char in elems['characters']:
                for e in char['elements']:
                    #Log("Elems: " + str(e))
                    titles.append(e['Title'])
                    urls.append(BASE_URL + e['Url'])
                    thumbs.append(e['Images'][0]['ImageUrl'])
                    fanarts.append(FanartURL(e['Url']))
                    summaries.append(e['Title'])
        else:
            titles = [ e['Title'] for e in elems ]
            urls = [ BASE_URL + e['Url'] for e in elems ]
            thumbs = [ e['Images'][0]['ImageUrl'] for e in elems ]
            fanarts = [ FanartURL(e['Url']) for e in elems ]
            summaries = [ GetSummary(e['Url']) for e in elems ]
    except:
        #e = sys.exc_info()[0]
        Log.Error("Error calling: %s." % url)
    
    return titles, urls, thumbs, fanarts, summaries, index+1, category
        
def ProgramList(url):    
    httpRequest = HTTP.Request(url = url, headers = {'X-Requested-With':'XMLHttpRequest'})
    #Log.Debug(httpRequest.content)
    items = JSON.ObjectFromString(httpRequest.content)
    items = [ i for i in items if i['hasOndemandRights'] ]
    titles = []
    urls = []
    thumbs = []
    fanarts = []
    summaries = []
    for item in items:
        titles.append(item['Title'])
        urls.append(BASE_URL + item['Url'])
        thumbs.append(item['ImageUrl'])
        fanarts.append(FanartURL(url))
        summaries.append(item['Title'])
  
    return titles, urls, thumbs, fanarts, summaries

def FanartURL(url):
    fUrl = url.replace(BASE_URL, '')
    if '/serie/' in url:
        fUrl = "http://nrk.eu01.aws.af.cm/f/%s" % fUrl.lstrip('/')
    elif '/Episodes/' in url:
        fUrl = "http://nrk.eu01.aws.af.cm/f/%s" % fUrl.split('/')[3]
    else:
        fUrl = ''
    
    #Log.Debug("FANART URL: " + fUrl)    
    return fUrl
    
def ThumbURL(url):
    tUrl = url.replace(BASE_URL, '')
    if '/Episodes/' in url:
        tUrl = "http://nrk.eu01.aws.af.cm/t/%s" % tUrl.split('/')[3]
    else:
        tUrl = "http://nrk.eu01.aws.af.cm/t/%s" % tUrl.lstrip('/')

    #Log.Debug("THUMB URL: " + tUrl)
    return tUrl
    
# Too slow at the moment. Needs caching
def GetProgramInfo(url):
    matchObj = re.search( r'\w{4}\d{8}', url, re.M|re.I)
    if matchObj:
        metaurl = JSON_URL_MEDIAELEMENT % matchObj.group()
        try:
            return JSON.ObjectFromURL(metaurl)
        except:
            return None
    else:
        return None
