from ast import keyword
from asyncio import events
from symbol import import_as_name
from unicodedata import name
from nonebot import on_keyword, on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment
from .data_source import *
pokemon = on_command("精灵", priority=5)
hybrid = on_command("融合", aliases={'杂交'}, priority=5)


@pokemon.handle()
async def _(bot: Bot, event: Event, state: T_State):
  keyword = str(event.get_message())
  poke = await get_pokemon(keyword)
  name = poke['name']
  pic_url = poke['url']
  await pokemon.send(keyword+"的精灵是 "+name)
  await pokemon.finish(message=MessageSegment.image(pic_url))


@hybrid.handle()
async def _(bot: Bot, event: Event, state: T_State):
  keywords = str(event.get_message()).strip()
  pokemons = keywords.split()
  if (len(pokemons) > 2 or len(pokemons) <= 1):
    await hybrid.finish("融合的精灵数目必须为2,用空格分开!", at_sender=True)
  await hybrid.send("融合ing", at_sender=True)
  poke = await merge(pokemons[0], pokemons[1])
  if poke['url'] == "":
    await pokemon.finish("仅限关都地区的宝可梦！不要融合奇奇怪怪的东西", at_sender=True)
  await pokemon.send(pokemons[0] + " 与 " + pokemons[1] + " 融合成为 " + poke['name']+" !")
  await pokemon.finish(message=MessageSegment.image(poke['url']))
  