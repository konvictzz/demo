# -*- coding:UTF-8 -*-

#traceroute(target,dport=80,minttl=1,maxttl=30,sport=<RandShort>,I4=None,filter=None,timeout=2,verbose=None,**kargs)
#http://blog.csdn.net/uoyevoli/article/details/565373

import os

print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))
print(os.path.abspath(__file__))

print(os.path.join(os.path.dirname(__file__), 'db.sqlite3'))
print(os.path.join("d:\\test", 'db.sqlite3'))