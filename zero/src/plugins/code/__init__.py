from nonebot.plugin import on_command, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters.cqhttp.event import GroupMessageEvent
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.bot import Bot
import aiohttp

lang_list = on_command("code list", priority=10)
run = on_command("run", priority=10)


@lang_list.handle()
async def _(bot: Bot, event: Event, state: T_State):
  url = "https://glot.io/api/run"
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
      response = await resp.json()
      msg = "glot.io 目前支持的语言有"
      for r in response:
        msg += r['name']+", "
      msg = msg[:-3]
      await lang_list.finish(msg)


@run.handle()
async def _(bot: Bot, event: Event, state: T_State):
  url = "https://glot.io/api/run/"
  headers = {
      "Authorization": "Token 6f321066-d193-42be-b300-52bd80baf574"
  }
  content = str(event.get_message())
  lang = content.split(' ')[0]         # 编程语言
  content = content[len(lang):].strip()   # 代码内容
  data = {
      "files": [{"name": "main.py", "content": "print(123)"}]
  }
  url += lang+"/latest"
  async with aiohttp.ClientSession() as session:
    async with session.post(url, headers=headers, data=data) as resp:
      await run.send(str(resp))
