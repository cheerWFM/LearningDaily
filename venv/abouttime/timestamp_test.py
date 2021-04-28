#!/usr/bin/env python 
# coding:utf-8
import re
from datetime import datetime,timedelta,timezone


def t_timestamp(dstr,zstr):
    dt=datetime.strptime(dstr,'%Y-%m-%d:%H:%M:%S')
    utc=re.match(r'^UTC[\+\-\]\d:\d\d',zstr).group(1)
    utc_1=timezone(timedelta(hours=int(utc)))
    timezone1=dt.replace(tzinfo=utc_1)
    print(timezone1.timestamp())


