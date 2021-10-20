from curses.ascii import isdigit
from difflib import IS_LINE_JUNK
from nonebot.plugin import on_command, on_keyword, on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.adapters.cqhttp.event import GroupMessageEvent
from nonebot.adapters._base import Event
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.exception import ActionFailed
import random
bang = on_command("俄罗斯轮盘", aliases={"bang"}, priority=4)
six = 6
ratio = 1


@bang.handle()
async def _(bot: Bot, event: Event, state: T_State):
  global six, ratio
  ra = str(event.get_message())
  if ra.isdigit() == True and ra != '':
    ratio += int(ra)
    six += random.randint(1, 10 if int(ra) > 10 else int(ra))
  res = random.randint(1, six)
  group_id = event.get_session_id().split('_')[1]
  user_id = event.get_session_id().split('_')[2]
  if (res == 1):
    url = "https://i.ytimg.com/vi/fMQBGINH9so/maxresdefault.jpg"
    await bang.send(MessageSegment.image(url), at_sender=True)
    try:
      six = 6
      ratio = 1
      await bot.call_api("set_group_ban", group_id=group_id, user_id=user_id, duration=int(ratio)*60)
    except ActionFailed:
      await bang.send("可恶！权限不够！", at_sender=True)
  else:
    six -= 1
    url = "https://tx-free-imgs.acfun.cn/o_1e4j5v4qh59jcsr1jjm1fjddm20.png"
    await bang.send("还剩{}发！目前倍率为{}".format(six, ratio)+MessageSegment.image(url), at_sender=True)
