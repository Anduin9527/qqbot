from nonebot import on_keyword, on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment, MessageEvent

from .data_source import get_article

asoul_artical = on_command('写点',
                           aliases={'发病', '小作文'}, rule=to_me(), priority=5)


@asoul_artical.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):

  keywords = str(event.get_message())
  article = await get_article(words=keywords)
  if not article:
    await asoul_artical.finish(message='发病了是吧？', at_sender=True)
  await asoul_artical.finish(keywords+article)
