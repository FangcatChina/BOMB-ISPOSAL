from gpiozero import *
import random
import time
from numbers import Number

my_1 = None
button = None
_E8_AE_BE_E5_A4_87 = None
round2 = None
timee = None
bts = None
tip = None


button = Button(24)
_E8_AE_BE_E5_A4_87 = Button(25)
print('拆弹专家小游戏')
print('按下24号GPIO按钮开始游戏')
print('按下25号GPIO按钮查看说明')
while True:
  if not button.value:
    round2 = 1
    timee = 240
    while round2 != 15:
      bts = random.randint(24, 25)
      print(''.join([str(x) for x in ['第', round2, '关']]))
      while not not timee:
        print(''.join([str(x2) for x2 in ['剩余', timee, '秒']]))
        time.sleep(1)
        if timee % 20 == 0:
          if bts == 24:
            if random.randint(1, 3) == 1:
              tip = 'tf'
            elif random.randint(1, 3) == 2:
              tip = 'wo'
            else:
              tip = 'eu'
          else:
            if random.randint(1, 3) == 1:
              tip = 'tf'
            elif random.randint(1, 3) == 2:
              tip = 'wi'
            else:
              tip = 'ev'
          print('小提示（英文）：' + str(tip))
        if not _E8_AE_BE_E5_A4_87.value:
          if bts == 25:
            break
          else:
            print('拆弹失败，游戏结束')
            break
        if not button.value:
          if bts == 24:
            break
          else:
            print('拆弹失败，游戏结束')
            break
        if not _E8_AE_BE_E5_A4_87.value:
          if bts == 25:
            round2 = (round2 if isinstance(round2, Number) else 0) + 1
            continue
          else:
            break
        if not button.value:
          if bts == 24:
            round2 = (round2 if isinstance(round2, Number) else 0) + 1
            continue
          else:
            break
        timee = (timee if isinstance(timee, Number) else 0) + -1
  elif _E8_AE_BE_E5_A4_87.value:
    print('游戏提示：您需要在规定时间内，按照提示，按下指定的按钮，提示的规范为：25的英文是twenty-five，那么可能会提示tf。如果你按错了按钮，将会自动结束游戏。游戏将会按下GPIO24号按钮后自动开始')