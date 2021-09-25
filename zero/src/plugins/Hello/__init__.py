from nonebot.plugin import on_command, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.bot import Bot
import numpy as np

hello = on_keyword({'你好', 'hello', 'hi', 'こんにちは'}, priority=2)
hello_list = ['안녕하세요.', 'hello', 'Aloha',
              'Hallo', 'こんにちは', 'Bonjour', '你好QwQ', 'Привет', 'hola!']


@hello.handle()
async def hello_(bot: Bot, event: MessageEvent):
  msg = np.random.choice(hello_list)+"  "+str(event.sender.nickname)
  await hello.finish(message=msg,
                     at_sender=True
                     )
