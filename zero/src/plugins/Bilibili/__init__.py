from ast import Pass
import imp
from urllib import response
from nonebot.plugin import on_command, on_keyword, on_message, on_regex
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters.cqhttp.event import GroupMessageEvent
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.bot import Bot
import aiohttp
Parse = on_regex(
    r"((http | https):\/\/)?(www.)?bilibili.com\/video\/", block=True, priority=1)
Parse_short = on_regex(
    r"((http|https):\/\/)?b23.tv\/\w*", block=True, priority=1)


@Parse.handle()
async def _(bot: Bot, event: Event, state: T_State):
  await Parse.send("正在解析....")
  bvid = str(event.get_message())
  url = ""
  if "/BV" in bvid:
    bvid = bvid.split("/BV")[1].split("?")[0]
    url = "https://api.bilibili.com/x/web-interface/view?bvid="+bvid
  if "/av" in bvid:
    avid = bvid.split("/av")[1].split("?")[0]
    url = "https://api.bilibili.com/x/web-interface/view?aid="+avid
  if url == "":
    await Parse.finish("嗯？没有检测到av或者bv号诶")
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
      response = await resp.json()
      if response["code"] != 0:
        await Parse.send(response["message"])
      msg = """
标题:{}
作者:{}
tags:{}
简介:{}
▶️:{}   ❤️:{}   🪙:{}
      """.format(response["data"]["title"], response["data"]["owner"]["name"],
                 response["data"]["tname"], response["data"]["desc"],
                 response["data"]["stat"]["view"], response["data"]["stat"]["like"],
                 response["data"]["stat"]["coin"])
      pic_url = response["data"]["pic"]
  await Parse.send(message=MessageSegment.image(pic_url)+msg)


@Parse_short.handle()
async def _(bot: Bot, event: Event, state: T_State):
  await Parse_short.send("好短，但是还是得解析")
  url = str(event.get_message()).split("b23.tv/")[1]
  url = "https://b23.tv/" + url
  try:
    async with aiohttp.ClientSession() as session:
      async with session.get(url) as resp:
        bvid = str(resp.history[1]).split("/video/BV")[1].split("?")[0]
  except IndexError:
    await Parse_short.finish("誒？目前只能识别视频类的链接诶[丧气]")
  url = "https://api.bilibili.com/x/web-interface/view?bvid="+bvid
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
      response = await resp.json()
      if response["code"] != 0:
        await Parse.send(response["message"])
      msg = """
标题:{}
作者:{}
tags:{}
简介:{}
▶️:{}   ❤️:{}   🪙:{}
      """.format(response["data"]["title"], response["data"]["owner"]["name"],
                 response["data"]["tname"], response["data"]["desc"],
                 response["data"]["stat"]["view"], response["data"]["stat"]["like"],
                 response["data"]["stat"]["coin"])
      pic_url = response["data"]["pic"]
  await Parse.send(message=MessageSegment.image(pic_url)+msg)
