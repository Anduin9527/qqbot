#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.log import logger
from nonebot.adapters.cqhttp.bot import Bot as CQHTTPBot
from nonebot.plugin import load_from_toml, load_builtin_plugins, load_plugin

# Custom your logger
#
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
load_builtin_plugins()
load_from_toml("pyproject.toml")
# web测试插件 8080/test
load_plugin("nonebot_plugin_test")
# web私聊监视插件
# nonebot.load_plugin("nonebot_plugin_web")
# 定时任务插件
load_plugin("nonebot_plugin_youthstudy")
# 青年大学习插件
nonebot.init(apscheduler_autostart=True)
nonebot.init(apscheduler_config={
    "apscheduler.timezone": "Asia/Shanghai"
})
# Modify some config / config depends on loaded configs
#
# config = driver.config
# do something...


if __name__ == "__main__":
  logger.warning(
      "Always use `nb run` to start the bot instead of manually running!")
  nonebot.run(app="__mp_main__:app")
