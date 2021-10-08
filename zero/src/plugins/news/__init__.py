import imp
from nonebot.plugin import on_command, on_keyword, on_message, require
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters.cqhttp.event import GroupMessageEvent
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.bot import Bot
from nonebot import get_driver
import aiohttp
news_60s = require('nonebot_plugin_apscheduler').scheduler

groups = [733396632, 1137819896]


@news_60s.scheduled_job('cron', hour=8, minute=0)
async def _():
  driver = get_driver()
  BOT_ID: str = str(driver.config.bot_id)
  bot = driver.bots[BOT_ID]
  url = 'https://v2.alapi.cn/api/zaobao'
  params = {
      'format': 'json',
      'token': 'P63j4LKqJpUgqEJb'
  }
  async with aiohttp.ClientSession() as session:
    async with session.get(url, params=params) as r:
      response = await r.json()
      img_url: str = response['data']['image'].split('!')[0]
  for group in groups:
    await bot.send_group_msg(group_id=group, message=MessageSegment.image(img_url))
