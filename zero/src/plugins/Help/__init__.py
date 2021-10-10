from nonebot.plugin import on_command, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.bot import Bot

help = on_command("help", aliases={'帮助'})


@help.handle()
async def _(bot: Bot, event: Event, state: T_State):
  await help.finish("""
  zerobot v1.4
  -------------------------------------
  目前的插件如下：
  1.问好        
  命令： hi 、こんにちは 等

  2.翻译翻译     
  命令： @bot /nbnhhsh、@bot /翻译翻译 等
  eg. @bot /翻译翻译 惊喜

  3.setu
  命令：来点、setu 等
  (青壮年模式，青少年模式解禁)
  eg. @bot 来点 眼镜 伏特加

  4.jg
  命令： @bot jg

  5.狗屁不通小作文
  命令： @bot /写点
  eg. @bot /写点 圣

  6.以图搜图
  命令： @bot /搜图 图片

  7.精灵宝可梦(怪)
  命令：/精灵 占卜的姓名
       /融合 精灵1 精灵2

  8.一个魂儿小作文
  命令: /发病 
  eg. /发病 杰哥
  -------------------------------------
  """)
