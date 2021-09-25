from nonebot.plugin import on_command, on_keyword, on_message
from nonebot.rule import keyword, to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.bot import Bot

from .data_source import get_article, get_msg

goupi_artical = on_command('写点', aliases={'狗屁不通'}, rule=to_me(), priority=5)
asoul = on_command('发病', priority=5)


@goupi_artical.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):

  keywords = str(event.get_message())
  article = await get_article(words=keywords)
  if not article:
    await goupi_artical.finish(message='发病了是吧？', at_sender=True)
  await goupi_artical.finish(keywords+article)


@asoul.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
  keyword = str(event.get_message())
  msg = await get_msg()
  if keyword:
    msg = msg.replace('嘉然', keyword)
    msg = msg.replace('然然', keyword)
  await asoul.finish(msg)
