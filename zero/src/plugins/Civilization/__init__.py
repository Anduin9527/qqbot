from nonebot.plugin import on_command, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters.cqhttp.event import GroupMessageEvent
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.bot import Bot
from nonebot import get_driver
import csv
import os
civil_list = on_command("文明列表", priority=3)
search = on_command("文明", aliases={'文明查找'}, priority=3)
cosaddr = get_driver().config.tencentcos


@civil_list.handle()
async def _(bot: Bot, event: Event, state: T_State):
  with open(os.getcwd()+'/src/plugins/Civilization/Civ.csv', 'r')as f:
    data = f.read()
    await civil_list.send(data)


@search.handle()
async def _(bot: Bot, event: Event, state: T_State):
  f = 0
  keyword = str(event.get_message())
  if keyword == "":
    await search.finish("记得输入领袖或者文明喔！")
  with open(os.getcwd()+'/src/plugins/Civilization/Civ.csv', 'r')as f:
    csvf = csv.DictReader(f)
    for row in csvf:
      if (row["文明"] == keyword):
        f = 1
        await search.send(MessageSegment.image(cosaddr+"/Civilization/Leaders/"+row["领袖"]+".jpg"))
        continue
      if (row["领袖"].find(keyword) != -1):
        f = 1
        await search.send(MessageSegment.image(cosaddr+"/Civilization/Leaders/"+row["领袖"]+".jpg"))
    if f == 0:
      await search.finish("找不到你要的查找的文明或者领袖喔！")
