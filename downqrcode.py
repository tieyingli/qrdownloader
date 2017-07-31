#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import urllib
import sys
import re
import json
reload(sys)
sys.setdefaultencoding('utf8')
from subprocess import *
from urllib import quote

URL_1 = 'http://biz.cli.im/Api/Getbeautify?callback=jQuery1910&qrcodeconfig%5Blogourl%5D=&qrcodeconfig%5Blogoshape%5D=rect&qrcodeconfig%5Bdata%5D={URL}&qrcodeconfig%5Bbgcolor%5D=%23FFFFFF&qrcodeconfig%5Bforecolor%5D=&qrcodeconfig%5Btext%5D={TEXT}&qrcodeconfig%5Bfontsize%5D=46&qrcodeconfig%5Bfontfamily%5D=msyh.ttf&qrcodeconfig%5Btransparent%5D=0&qrcodeconfig%5Bfontcolor%5D=&qrcodeconfig%5Blevel%5D=H&qrcodeconfig%5Bincolor%5D=&qrcodeconfig%5Boutcolor%5D=&qrcodeconfig%5Bqrcode_eyes%5D=&qrcodeconfig%5Bbackground%5D=images%2Fbackground%2Fbg13.png&qrcodeconfig%5Bwper%5D=0.74&qrcodeconfig%5Bhper%5D=0.74&qrcodeconfig%5Btper%5D=0.13&qrcodeconfig%5Blper%5D=0.13&qrcodeconfig%5Beye_use_fore%5D=1&qrcodeconfig%5Bqrpad%5D=10&qrcodeconfig%5Bmarginblock%5D=2&_=1501488594582'
_jsonp_begin = r"jQuery1910('"
_jsonp_end = r"')"

def from_jsonp(jsonp_str):
    jsonp_str = jsonp_str.strip()
    if not jsonp_str.startswith(_jsonp_begin) or \
            not jsonp_str.endswith(_jsonp_end):
        raise ValueError('Invalid JSONP')
    return json.loads(jsonp_str[len(_jsonp_begin):-len(_jsonp_end)])

def run_cmd(cmd):
	print cmd
	p = Popen(cmd, shell=True, stdout=PIPE)
	output = p.communicate()[0]
	return output

def getQRDownUrl(urltoqr, texttoqr):
	url = URL_1.replace("{URL}",quote(urltoqr)).replace("{TEXT}",quote(texttoqr))
	jsonp_r = urllib.urlopen(url)
	jsonp = jsonp_r.read()
	jsonpstr = jsonp.decode("utf8")
	jsonp_r.close()
	#print jsonpstr

	json = from_jsonp(jsonpstr)

	#print json
	return "http:" + json['qrcodehigh']

def downQR(urltoqr, texttoqr):
	url_d = getQRDownUrl(urltoqr, texttoqr)
	cmd = "curl -o " + texttoqr + ".jpg '" + url_d + "'"
	run_cmd(cmd)

ar = [
	["http://www.google.com", "google"],
	["http://www.baidu.com", "baidu"]

]

for links in ar:
	print(links[0]+'  ' + links[1])
	downQR(links[0],links[1])

