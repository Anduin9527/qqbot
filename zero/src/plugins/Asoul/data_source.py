import aiohttp
import asyncio
import json

from requests.models import Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
import random


async def get_msg() -> str:
  pageNum = random.randint(1, 245)
  index = random.randint(0, 8)
  url = "https://asoulcnki.asia/v1/api/ranking/v1/api/ranking/"
  headers = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
  params = {
      'pageSize': 10,
      'pageNum': pageNum,
      'timeRangeMode': 0,
      'sortMode':  0,
      'keywords': '嘉然'
  }
  async with aiohttp.ClientSession() as session:
    async with session.get(url, headers=headers, params=params) as r:
      r = await r.json()
      if r['message'] != "success":
        return r['message']
      else:
        return r['data']['replies'][index]["content"]


async def get_article(words) -> str:
  data = {'prefix': words}
  url = 'http://asoul.lapras.xyz:5089/generate'
  async with aiohttp.ClientSession() as session:
    async with session.post(url, data=json.dumps(data)) as res:
      result = await res.json()
      return str(result['reply']['generated'])
