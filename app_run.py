#!/usr/bin/python
# 導入 os 模組, 主要用來判斷是否在 OpenShift 上執行
import os
# 導入同目錄下的 myflaskapp.py
import flaskapp

flaskapp.app.run(debug=True)