from nonebot.plugin import on_command, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters.cqhttp.event import GroupMessageEvent
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.bot import Bot

import asyncio
from .data_source import get_pic_url

setu = on_keyword({'setu', '涩图', '色图', '来点', '色图来'}, priority=7)
r18_on = on_keyword({'青壮年模式'}, priority=8)
r18_off = on_keyword({'青少年模式'}, priority=8)
r18 = False


@setu.handle()
async def _(bot: Bot, event: GroupMessageEvent, state: T_State):

  key_word = str(event.get_message()).strip()
  words = ['setu', '涩图',  '来点', '色图来', '色图']
  for word in words:
    key_word = key_word.replace(word, '')
  tags = key_word.split()
  if len(tags) > 2:
    await setu.finish("最多只支持两个关键词检索哦！关键词之间请用空格分隔")
  img_url = await get_pic_url(tag=tags, r18=r18)
  if not img_url:
    await setu.finish('找不到相关的图o')
  if img_url == 'time out':
    await setu.finish('搜索超时，坏掉了啦，都是你害的', at_sender=True)
  result = await setu.send(message=MessageSegment.image(img_url))
  if r18:
    message_id = result['message_id']
    await asyncio.sleep(10)
    await bot.delete_msg(message_id=message_id)
  await setu.finish()


@r18_on.handle()
async def _(bot: Bot, event: GroupMessageEvent, state: T_State):
  global r18
  if r18:
    await setu.finish("已经是青壮年模式！")
  else:
    r18 = True
    pic_path = "http://ww4.sinaimg.cn/large/ceeb653ejw1fadcutjn80j206405ia9x.jpg"
    msg = MessageSegment.image(pic_path)
    await setu.send(msg)
    await setu.finish("启动青壮年模式！")


@r18_off.handle()
async def _(bot: Bot, event: GroupMessageEvent, state: T_State):
  global r18
  if r18:
    r18 = False
    await setu.finish("为呵护未成年人健康成长, 特别推出青少年模式,该模式下部分功能无法正常使用。请监护人主动选择, 并设置监护密码。")
  else:
    pic_path = "http://wx2.sinaimg.cn/large/ab4cb34agy1fmatr6yiswj20dw0dwq3o.jpg"
    msg = MessageSegment.image(pic_path)
    await setu.send(msg)
    await setu.finish("已经是青少年模式！")
