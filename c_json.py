#!/usr/bin/env python 
# coding:utf-8
import json
#将python的dict序列化成json
d=dict(name='wenfangmei',age='22',grend='female')
print(json.dumps(d))

#将json反序列化为python对象
json_str='{"city":"guangzou","job":"tester","company":"cvte"}'
python_str=json.loads(json_str)
print(python_str)

class Student(object):
    def __init__(self,name,age,score):
        self.name=name,
        self.age=age,
        self.score=score

def Student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }


s=Student('wfm','22','95')
print(json.dumps(s,default=Student2dict))

##偷懒，对每一个class直接转换
class Student1(object):

    def __init__(self, name1, age1, score1):
        self.name1 = name1
        self.age1= age1
        self.score1 = score1

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name1, self.age1, self.score1)

s = Student1('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student1(d['name1'], d['age1'], d['score1']))
print(rebuild)


