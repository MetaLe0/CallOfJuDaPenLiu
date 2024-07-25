# -*- encoding: utf-8 -*-
'''
@File      :   main.py
@Author    :   MetaLeo
@Contact   :   
@License   :   AGPL
@Copyright :   (C) 2020-2021
@Desc      :   None
'''

import OlivOS
import CallOfJuDaPenLiu

import time

class Event(object):
    def init(plugin_event, Proc):
        pass

    def private_message(plugin_event, Proc):
        回复(plugin_event, Proc)

    def group_message(plugin_event, Proc):
        回复(plugin_event, Proc)

复读记录 = {}

def 回复(plugin_event, Proc):
    群号 = None
    消息 = None
    检测到复读消息 = '检测到复读消息'
    开始叠放巨大喷流 = '开始叠放巨大喷流'
    if "message" in plugin_event.data.__dict__:
        消息 = plugin_event.data.message
    if "hash" in plugin_event.bot_info.__dict__:
        群号 = str(plugin_event.bot_info.hash)
        if "group_id" in plugin_event.data.__dict__:
            群号 = str(plugin_event.data.group_id) + '|' + 群号
        else:
            群号 = None
    if 群号 != None and 消息 != None:
        if "host_id" in plugin_event.data.__dict__:
            if plugin_event.data.host_id != None:
                群号 = str(plugin_event.data.host_id) + '|' + 群号
        if 群号 in 复读记录:
            if 消息 == 复读记录[群号]:
                复读记录[群号] = None
                直接回复(plugin_event, 检测到复读消息)
                time.sleep(0.5)
                直接回复(plugin_event, 开始叠放巨大喷流)
            else:
                复读记录[群号] = 消息
        else:
            复读记录[群号] = 消息

def 直接回复(plugin_event, 消息):
    plugin_event.reply(消息)
