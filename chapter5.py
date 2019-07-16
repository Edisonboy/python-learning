from datetime import datetime
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict

# 获取当前日期和时间
now = datetime.now()
print(now)

# 获取指定日期和时间
dt = datetime(2015, 4, 19 ,12, 20)
print(dt)
print(dt.timestamp())

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(isinstance(p, Point))

# deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict
od = OrderedDict([('a', 1), ('c', 3), ('b', 2)])
print(od)



