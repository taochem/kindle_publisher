#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseFeedBook

def getBook():
    return NaturePhysics

class NaturePhysics(BaseFeedBook):
    title                 = 'Nature Physics'
    description           = 'Nature's Physical Sciences Research'
    language              = 'en'
    feed_encoding 		  = "utf-8"
    page_encoding 		  = "utf-8"
    mastheadfile 		  = "mh_naturePhysics.png"
    coverfile 			  =  'cv_naturePhysics.gif'
    keep_image			  = True
    fulltext_by_readability = True
    oldest_article = 1
    feeds = [
            (u'Nature Physics','http://feeds.nature.com/nphys/rss/current')
           ]