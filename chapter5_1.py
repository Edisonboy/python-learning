from collections import ChainMap
from collections import Counter
import os, argparse

# ChainMap
# 构造缺省参数
defaults = {
        'color': 'red',
        'user': 'guest'
}

# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成ChainMap
combined = ChainMap(command_line_args, os.environ, defaults)
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

c = Counter()
for ch in 'programing':
        c[ch] = c[ch] + 1
print(c)



