#!/usr/bin/env python
#!coding:utf-8
'''
author: dinghewu
date: 2018/11/11 @ 14:28
python 3.6.2
'''
import shlex
import subprocess

# 输出日志到文件
# ff=open('log.txt','w')
# p=subprocess.Popen('test.bat',stdin=subprocess.PIPE,stdout=ff.fileno(),stderr=subprocess.STDOUT,shell=True)
# p.wait()

# 输出到管道，涉及缓存刷新，输出字节还是字符等问题
# cmd='python subprocess_test.py'
# cmd=shlex.split(cmd)  # 省去shell=True，降低命令注入风险
# p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,\
#                    universal_newlines=False)
# while p.poll() is None:
#     p.stdout.flush()  # windows 下缓冲区刷新不影响即时输出，linux下则不同
#     line=p.stdout.readline().strip().decode('utf-8')  # 去掉两端换行符,universal_newlines=True则直接输出str。
#     if line:  # stdout 存在很多空行，不输出
#         print(type(line))
#         print(line)
# p.wait()
# print('p finished')

