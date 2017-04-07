#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseFeedBook

def getBook():
    return NatureChemistry

class NatureChemistry(BaseFeedBook):
    title                 = 'Nature Chemistry'
    description           = 'Nature's Chemical Sciences Research'
    language              = 'en'
    feed_encoding 		  = "utf-8"
    page_encoding 		  = "utf-8"
    mastheadfile 		  = "mh_natureChemistry.png"
    coverfile 			  =  'cv_natureChemistry.gif'
	network_timeout       = 60
    keep_image			  = True
    fulltext_by_readability = True
    oldest_article = 7
    feeds = [
            (u'Nature Chemistry','http://www.nature.com/nchem/current_issue/rss/index.html')
           ]