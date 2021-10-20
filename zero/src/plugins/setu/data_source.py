import aiohttp
import re
import execjs
import requests
import urllib.parse
from nonebot.log import logger
from nonebot.adapters.cqhttp.exception import NetworkError
from lxml import etree
import random


async def get_pic_url(tag: list, r18=False) -> str:
  url = 'https://api.lolicon.app/setu/v2'
  params = {
      'r18': 1 if r18 else 0,
      'num': 1,
      'size': ['regular'],
      'proxy': 'https://i.pixiv.cat/{{path}}',
      'tag': tag
  }
  try:
    async with aiohttp.ClientSession() as session:
      async with session.get(url, params=params) as resp:
        response = await resp.json()
    if response['error']:
      logger.warning('lolicon error: ' + response['error'])
      return ''
    try:
      result = response['data'][0]['urls']['regular']
    except IndexError:
      return ''
    else:
      return result
  except NetworkError:
    return 'time out'


async def get_mangabz_url(is_random=0):
  headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
             "Cookie": "image_time_cookie=185960|637694883538371062|0,185961|637694883592614831|0,187013|637694883614626650|0,100435|637694885955661627|0,200091|637694946275878939|5",
             }
  if is_random == 0:
    url = "http://www.mangabz.com/m200091/"
  else:
    url_dic = "http://www.mangabz.com/1312bz/"
    async with aiohttp.ClientSession() as session:
      async with session.get(url_dic, headers=headers) as rspo:
        r = await rspo.text()
        p = etree.HTML(r, parser=None)
        url = "http://www.mangabz.com" + \
            p.xpath(
              '//*[@id="chapterlistload"]/a[{}]/@href'.format(random.randint(1, 389)))[0]
  async with aiohttp.ClientSession() as session:
    async with session.get(url, headers=headers) as rspo:
      r = await rspo.text()
      mangabz_cid = re.findall("MANGABZ_CID=(.*?);", r)[0]
      mangabz_mid = re.findall("MANGABZ_MID=(.*?);", r)[0]
      page_total = re.findall("MANGABZ_IMAGE_COUNT=(.*?);", r)[0]
      mangabz_viewsign_dt = re.findall(
          "MANGABZ_VIEWSIGN_DT=\"(.*?)\";", r)[0]
      mangabz_viewsign = re.findall(
          "MANGABZ_VIEWSIGN=\"(.*?)\";", r)[0]
      headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
                 "Cookie": "image_time_cookie=185960|637694883538371062|0,185961|637694883592614831|0,187013|637694883614626650|0,100435|637694885955661627|0,200091|637694946275878939|5",
                 "Referer": url
                 }
    js_url = url + "chapterimage.ashx?" + "cid=%s&page=%s&key=&_cid=%s&_mid=%s&_dt=%s&_sign=%s" % (
        mangabz_cid, page_total, mangabz_cid, mangabz_mid, urllib.parse.quote(mangabz_viewsign_dt), mangabz_viewsign)
    async with session.get(js_url, headers=headers) as rspo:
      js = await rspo.text()
  img_urls = []
  for i in range(int(page_total)):
    i += 1
    imagesList = execjs.eval(js)
    img_urls.append(imagesList[0].split('?cid')[0])
  return img_urls
