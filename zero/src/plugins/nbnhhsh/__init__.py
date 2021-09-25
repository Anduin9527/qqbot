import httpx
import asyncio
from random import choice, randint
from nonebot.plugin import on_command, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.bot import Bot

trans = on_command("nbnhhsh", rule=to_me(), block=True,
                   aliases={"翻译翻译", "能不能好好说话", "翻译", "你给我翻译翻译，什么叫他妈的"})


@trans.handle()
async def _(bot: Bot, event: Event, state: dict):
  args = str(event.get_message()).strip()
  if args:
    state["text"] = args
  if args == "惊喜":
    await trans.send("这还用翻译，都说了......惊喜嘛。")
    asyncio.sleep(0)
    await trans.send("我让你翻译给我听，什么叫惊喜？")
    asyncio.sleep(0)
    await trans.send("难道你听不懂什么叫惊喜？")
    asyncio.sleep(0)
    await trans.send("我就想让你翻译翻译，什么叫惊喜！")
    asyncio.sleep(0)
    await trans.send("翻译出来给我听，什么他妈的叫惊喜！什么他妈的叫他妈的惊喜！")
    asyncio.sleep(0)
    await trans.send("什么他妈的叫惊喜啊？")
    asyncio.sleep(0)
    await trans.send("惊喜就是三天之后，我出一百八十万给你们出城剿匪，接上我的腿！明白了吗？")
    asyncio.sleep(0)
    await trans.send("这就是惊喜啊。")
    asyncio.sleep(0)
    await trans.send("翻译翻译，翻译翻译！")
    asyncio.sleep(0)
    await trans.send("惊喜就是三天之后，给你一百八十万两银子出城剿匪，接上他的腿！")
    asyncio.sleep(0)
    await trans.send("哈，大哥，原来这就是他妈的惊喜啊。")
    asyncio.sleep(0)
    await trans.finish(message="懂了吗，cdd", at_sender=True)
  api = "https://lab.magiconch.com/api/nbnhhsh/guess"
  data = {"text": state["text"]}
  async with httpx.AsyncClient() as client:
    response = await client.post(api, data=data)
  response = response.json()

  if not response:
    await trans.finish("bt，wm00hdzyjh，没有对应的翻译")
  try:
    msg = "得到的翻译如下：\n"
    for i in response[0]['trans']:
      msg += i + "，"
    msg = msg.strip("，")
    await trans.finish(msg)
  except KeyError:
    await trans.finish("坏了Z世代又出新词了，没有对应的翻译")
