#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseFeedBook

def getBook():
    return cnn

class cnn(BaseFeedBook):
    title                 = 'Chemical Review'
    description           = 'Chemical Review, top review articles'
    language = 'en'
    feed_encoding = "utf-8"
    page_encoding = "utf-8"
    mastheadfile = "mh_chemicalReview.gif"
    coverfile =  'cv_chemicalReview.jpg'
    keep_image = True
    fulltext_by_readability = True
    oldest_article = 1
    feeds = [
            ('Chemical Review','http://pubs.acs.org/action/showFeed?ui=0&mi=0&ai=54p&jc=chreay&type=etoc&feed=rss')
           ]