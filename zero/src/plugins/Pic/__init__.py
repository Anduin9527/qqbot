import pathlib
from nonebot.plugin import on_command, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.bot import Bot


jg = on_keyword(keywords={"jg", "杰哥", "yyj"}, rule=to_me(), priority=10)


@jg.handle()
async def _(bot: Bot, event: Event, state: T_State):
  pic_path = r"/home/anduin9527/qqbot/zero/src/picture/memeofos.jpg"
  msg = MessageSegment.image(pathlib.Path(pic_path).as_uri())
  await jg.finish(msg)
