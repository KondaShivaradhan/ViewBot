@echo off
title = comments count Server
:START
@REM cd "D:\Youtube\comments"
python index.py
TIMEOUT /T 3
GOTO:START