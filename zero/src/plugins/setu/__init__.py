from nonebot import on_keyword, on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment
from pydantic.tools import T

from .data_source import get_pic_url

setu = on_keyword({'setu', '涩图', '色图', '来点'}, rule=to_me(), priority=7)
r18_switch = on_command(
    '就这', aliases={'来点给劲的', '不够涩'}, rule=to_me(), permission=SUPERUSER, priority=8)
r18 = False


@setu.handle()
async def _(bot: Bot, event: Event, state: T_State):
  
  key_word = str(event.get_message()).strip()
  words = ['setu', '涩图', '色图', '来点']
  for word in words:
    key_word = key_word.replace(word, '')
  tags = key_word.split()
  if len(tags) > 2:
    await setu.finish("最多只支持两个关键词检索哦！关键词之间请用空格分隔")
  img_url = await get_pic_url(tag=tags, r18=r18)
  if not img_url:
    await setu.finish('找不到相关的图o')
  await setu.send(message=MessageSegment.image(img_url))
  await setu.finish()


@r18_switch.handle()
async def _(bot: Bot, event: Event, state: T_State):
  global r18
  if r18:
    r18 = False
    await setu.finish("启动青少年模式！")
  else:
    r18 = True
    await setu.finish("启动青壮年模式！")
