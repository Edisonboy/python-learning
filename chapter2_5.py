
from types import MethodType

class Student(object):
    pass

def set_age(self, age):
    self.age = age

s = Student()
s.name = 'Edison'
print(s.name)

# 给实例绑定一个方法
s.set_age = MethodType(set_age, s)
s.set_age(24)
print(s.age)

Student.set_age = set_age
s2 = Student()
s2.set_age(100)
print(s2.age)

# __slots__ 限制添加的属性
def set_age(self, age):
    self.age = age