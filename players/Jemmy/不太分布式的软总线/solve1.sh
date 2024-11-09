#!/bin/bash

dbus-send --system \
          --print-reply \
          --dest=cn.edu.ustc.lug.hack.FlagService \
          /cn/edu/ustc/lug/hack/FlagService \
          cn.edu.ustc.lug.hack.FlagService.GetFlag1 \
          string:"Please give me flag1"