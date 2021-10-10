from argparse import SUPPRESS
import imp
from lib2to3.pgen2 import driver
from nonebot.plugin import on_command, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters.cqhttp.event import GroupMessageEvent
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.permission import SUPERUSER
from nonebot import get_driver

g_msg = on_command("g", priority=1, permission=SUPERUSER)


@g_msg.handle()
async def _(bot: Bot, event: Event, state: T_State):
  driver = get_driver()
  msgs = str(event.get_message()).split(" ", 1)
  if len(msgs) != 2:
    await g_msg.finish("检查群号是否正确"+str(driver.config.groups))
  group_id = int(msgs[0])
  msg = msgs[1]
  if str(group_id) in driver.config.groups:
    await bot.send_group_msg(group_id=group_id, message=msg)
    pass
  else:
    await g_msg.finish("检查群号是否正确"+str(driver.config.groups))
