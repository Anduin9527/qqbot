from nonebot import on_message, on_notice
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import GroupIncreaseNoticeEvent, GroupDecreaseNoticeEvent, Message
from nonebot.typing import T_State
from nonebot.matcher import *

group_notice = on_notice()


@group_notice.handle()
async def welcome(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
  await group_notice.finish(message="欢迎欢迎",
                            at_sender=True)


@group_notice.handle()
async def sayBye(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):
  await group_notice.finish(message="呜呜呜他走了",
                            at_sender=True)
