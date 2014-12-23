#coding=utf-8
import os

lines = os.popen('ipconfig').readlines()
print 'lines - ', lines
print 'ではありません'
os.system('ipconfig')

