import pathlib
from nonebot import on_command, on_message
from nonebot.plugin import on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.matcher import *
from nonebot.adapters.cqhttp import Message, Bot, MessageEvent, MessageSegment
from nonebot.adapters import Event
import numpy as np

jg = on_keyword(keywords={"jg", "杰哥", "yyj"}, rule=to_me())


@jg.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
  pic_path = r"/home/anduin9527/qqbot/zero/src/picture/memeofos.jpg"
  msg = MessageSegment.image(pathlib.Path(pic_path).as_uri())
  await jg.finish(msg)
