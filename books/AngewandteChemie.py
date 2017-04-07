#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseFeedBook

def getBook():
    return AngewandteChemie

class AngewandteChemie(BaseFeedBook):
    title                 = 'AngewandteChemie'
    description           = 'Angewandte Chemie International Edition'
    language              = 'en'
    feed_encoding 		  = "utf-8"
    page_encoding 		  = "utf-8"
    mastheadfile 		  = "mh_angewandteChemie.png"
    coverfile 			  =  'cv_angewandteChemie.png'
	network_timeout       = 60
    keep_image			  = True
    fulltext_by_readability = True
    oldest_article = 7
    feeds = [
            (u'Angewandte Chemie','http://onlinelibrary.wiley.com/rss/journal/10.1002/(ISSN)1521-3773')
           ]