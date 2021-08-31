import httpx
from random import choice, randint
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.plugin import on_command

trans = on_command("nbnhhsh", rule=to_me(), block=True,
                   aliases={"翻译翻译", "能不能好好说话", "翻译", "你给我翻译翻译，什么叫他妈的"})


@trans.handle()
async def _(bot: Bot, event: Event, state: dict):
  args = str(event.get_message()).strip()
  if args:
    state["text"] = args
  api = "https://lab.magiconch.com/api/nbnhhsh/guess"
  data = {"text": state["text"]}
  async with httpx.AsyncClient() as client:
    response = await client.post(api, data=data)
  response = response.json()

  if not response or len(response) == 1:
    await trans.finish("没有对应的翻译")
  msg = "得到的翻译如下：\n"
  for i in response[0]:
    msg += i + "，"
  msg = msg.strip("，")
  await trans.finish(msg)
