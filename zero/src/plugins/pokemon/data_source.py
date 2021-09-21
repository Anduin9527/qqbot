import aiohttp
from lxml import etree
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options

url = "https://pokemon.alexonsager.net/zh"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}


async def get_pokemon(name: str) -> dict:
  params = {
      'name': name
  }
  async with aiohttp.ClientSession() as session:
    async with session.get(url, headers=headers, params=params) as resp:
      r = await resp.text()
      p = etree.HTML(r, parser=None)
      pokemon_url: str = p.xpath('//img[@id="pk_img"]/@src')
      pokemon_name: str = p.xpath('//div[@id="pk_name"]/text()')
      pokemon = {'name': pokemon_name[0], 'url': pokemon_url[0]}
      return pokemon


async def merge(name1: str, name2: str) -> dict:
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-gpu')
  d = webdriver.Chrome(options=chrome_options)
  d.get(url)
  try:
    Select(d.find_element_by_id("select1")).select_by_visible_text(name1)
    Select(d.find_element_by_id("select2")).select_by_visible_text(name2)
    pic_url = d.find_element_by_xpath(
        '//img[@id="pk_img"]').get_attribute("src")
    pic_name: WebElement = d.find_element_by_id("pk_name")
    name = pic_name.get_attribute('textContent')
    d.quit()
    pokemon = {'name': name, 'url': pic_url}
  except:
    return {'name': "", 'url': ""}
  return pokemon


async def depart(name: str):
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-gpu')
  d = webdriver.Chrome(options=chrome_options)
  d.get(url)
  
  pass
