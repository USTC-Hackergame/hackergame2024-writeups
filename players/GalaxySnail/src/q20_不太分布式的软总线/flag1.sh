#!/bin/sh
dbus-send --system --print-reply \
  --dest=cn.edu.ustc.lug.hack.FlagService \
  /cn/edu/ustc/lug/hack/FlagService \
  cn.edu.ustc.lug.hack.FlagService.GetFlag1 \
  string:"Please give me flag1"

busctl call \
  cn.edu.ustc.lug.hack.FlagService \
  /cn/edu/ustc/lug/hack/FlagService \
  cn.edu.ustc.lug.hack.FlagService \
  GetFlag1 \
  s 'Please give me flag1'

gdbus call --system \
  --dest cn.edu.ustc.lug.hack.FlagService \
  --object-path /cn/edu/ustc/lug/hack/FlagService \
  --method cn.edu.ustc.lug.hack.FlagService.GetFlag1 \
  "Please give me flag1"
