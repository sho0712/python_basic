"""
A-10: サイコロ
下記のコードが期待通り動作するような、1から6の整数をランダムに出力する dice() 関数を実装してください
print(dice()) # 1から6の整数をランダムに出力する
"""

import random


def dice():
    number = [1, 2, 3, 4, 5, 6]
    return random.choice(number)


print(dice())
