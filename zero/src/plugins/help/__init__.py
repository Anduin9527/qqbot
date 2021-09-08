from nonebot import on_keyword, on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment

help = on_command("help", aliases={'帮助'})


@help.handle()
async def _(bot: Bot, event: Event, state: T_State):
  await help.finish("""
  目前的插件如下：
  1.问好        
  命令： /hi 、/こんにちは 等
  2.翻译翻译     
  命令： @bot /nbnhhsh、@bot /翻译翻译 等
  eg. @bot /翻译翻译 惊喜
  3.setu
  命令： @bot 来点 、@bot 涩图 、@bot setu 等
  eg. @bot 来点 眼镜 伏特加
  4.jg
  命令： @bot jg
  """)
