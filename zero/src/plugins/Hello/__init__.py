from nonebot import on_command, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.matcher import *
from nonebot.adapters.cqhttp import Message, Bot, MessageEvent
from nonebot.adapters import Event
import numpy as np

hello = on_keyword({'你好','hello', 'hi', 'こんにちは'}, priority=2)
hello_list = ['안녕하세요.', 'hello', 'Aloha',
              'Hallo', 'こんにちは', 'Bonjour', '你好QwQ', 'Привет', 'hola!']


@hello.handle()
async def hello_(bot: Bot, event: MessageEvent):
  msg = np.random.choice(hello_list)+"  "+str(event.sender.nickname)
  await hello.finish(message=msg,
                     at_sender=True
                     )
