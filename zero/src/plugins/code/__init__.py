from urllib import response
from nonebot.plugin import on_command, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters.cqhttp.event import GroupMessageEvent
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.bot import Bot
import aiohttp
import requests

lang_list = on_command("code list", priority=10)
run = on_command("run", priority=10)


@lang_list.handle()
async def _(bot: Bot, event: Event, state: T_State):
  url = "https://glot.io/api/run"
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
      response = await resp.json()
      msg = "glot.io 目前支持的语言有"
      for r in response:
        msg += r['name']+", "
      msg = msg[:-3]
      await lang_list.finish(msg)

langs = {"assembly": ".asm",
         "ats": ".dats",
         "bash": ".sh",
         "c": ".c",
         "clojure": ".clj",
         "cobol": ".cob",
         "coffeescript": ".coffee",
         "cpp": ".cpp",
         "crystal": ".cr",
         "csharp": ".cs",
         "d": ".d",
         "elixir": ".ex",
         "elm": ".elm",
         "erlang": "erl",
         "fsharp": "fs",
         "go": ".go",
         "groovy": ".groovy",
         "haskell": ".hs",
         "idris": ".idr",
         "java": "java",
         "javascript": ".js",
         "julia": ".jl",
         "kotlin": ".kt",
         "lua": ".lua",
         "mercury": ".m",
         "nim": ".nim",
         "nix": ".nix",
         "ocaml": ".ml",
         "perl": ".pl",
         "php": ".php",
         "python": ".py",
         "raku": ".raku",
         "ruby": ".rb",
         "rust": ".rs",
         "scala": ".scala",
         "swift": ".swift",
         "typescript": ".ts"
         }


@run.handle()
async def _(bot: Bot, event: Event, state: T_State):
  pass


@run.got("lang", prompt="输入语言类型（使用/code list 查看支持语言）")
async def _(bot: Bot, event: Event, state: T_State):
  if state["lang"] == "/code list":
    await run.reject(str(langs.keys()))
  if state["lang"] in langs:
    pass
  else:
    await run.reject("请检查语言名称是否正确")


@run.got("content", prompt="输入代码，不排版就(￣ε(#￣)☆╰╮(￣▽￣///)")
async def _(bot: Bot, event: Event, state: T_State):
  url = "https://glot.io/api/run/"
  headers = {
      'Authorization': 'Token 6f321066-d193-42be-b300-52bd80baf574',
      'Content-type': 'application/json',
  }
  content = str(state["content"]).replace('\n', "n").replace(
      '\r', '\\').replace("&#91;", "[").replace("&#93;", "]").replace(
      "\"", "\\\"").replace("\'", "\\'")
  lang = state["lang"]        # 编程语言
  file = langs[lang]
  data = '{"files": [{"name": "%(file)s", "content": "%(content)s"}]}' % {
      "file": "main"+file,
      "content": content}
  url += lang+"/latest"
  try:
    async with aiohttp.ClientSession() as session:
      async with session.post(url, headers=headers, data=data) as resp:
        response = await resp.json()
        if response["stdout"] != "":
          await run.finish("stdout:\n"+response["stdout"], at_sender=True)
        else:
          await run.finish("stderr:\n"+response["stderr"], at_sender=True)
  except KeyError:
    await run.finish("执行失败，执行超时或格式错误\n(中之人是个笨比，各种字符转义都没neng好)\n", at_sender=True)
