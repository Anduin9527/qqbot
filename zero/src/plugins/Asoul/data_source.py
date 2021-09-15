import aiohttp
import asyncio
import json


async def get_article(words) -> str:
  data = {'prefix': words}
  url = 'http://asoul.lapras.xyz:5089/generate'
  async with aiohttp.ClientSession() as session:
    async with session.post(url, data=json.dumps(data)) as res:
      result = await res.json()
      return str(result['reply']['generated'])
