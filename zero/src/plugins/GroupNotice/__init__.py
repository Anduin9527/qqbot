from nonebot.plugin import on_command, on_keyword, on_message,on_notice
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.event import GroupIncreaseNoticeEvent,GroupDecreaseNoticeEvent
from nonebot.adapters.cqhttp.bot import Bot

group_notice = on_notice()


@group_notice.handle()
async def welcome(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
  await group_notice.finish(message="欢迎欢迎",
                            at_sender=True)


@group_notice.handle()
async def sayBye(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):
  await group_notice.finish(message="呜呜呜他走了",
                            at_sender=True)
