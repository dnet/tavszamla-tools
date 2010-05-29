#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# tavszamla.py - Python API for Távszámla
#
# Copyright (c) 2010 András Veres-Szentkirályi
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

from BeautifulSoup import BeautifulSoup
import urllib2
import urllib

def cookie_init():
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
	urllib2.install_opener(opener)

def get_timestamp():
	mainpage = urllib2.urlopen('https://www.tavszamla.hu/tavszamlaportal/Welcome.jsp')
	soup = BeautifulSoup(mainpage.read())
	tsp = soup.find(attrs={'name': 'UID_A30EDF6F-4BFE-4478-9311-3C34328B97D3-TSP'})
	return tsp['value']

def login(username, password, timestamp):
	data = urllib.urlencode([
		('UID_C93867A4-CB6E-420a-BFE1-514858F336FE-', username),
		('UID_3DDC70FA-3407-44b4-95D1-764A22CD980A-', password),
		('UID_A30EDF6F-4BFE-4478-9311-3C34328B97D3-TSP', timestamp)
	])
	login = urllib2.urlopen('https://www.tavszamla.hu/tavszamlaportal/Welcome.do', data)
	soup = BeautifulSoup(login.read())
	return soup.find(attrs={'class': 'name'}).string.strip()

def logout():
	urllib2.urlopen('https://www.tavszamla.hu/tavszamlaportal/Logout.do')
