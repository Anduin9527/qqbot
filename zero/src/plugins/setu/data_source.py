import aiohttp
from nonebot.log import logger
from nonebot.adapters.cqhttp.exception import NetworkError

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
