#!/usr/bin/env python 
# coding:utf-8
from datetime import datetime, timedelta
from time import timezone

# now = datetime.now()
# print('现在的时间是：%s' % now)
# cal = now - timedelta(hours=10)
# ca1 = now + timedelta(days=1)
# print('现在的时间前10个小时：%s' % cal)
# print('一天后的时间：%s' % ca1)

# timezone change
dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(dt)
