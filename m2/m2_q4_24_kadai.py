def func(a, b):  # 関数の定義
    if a ** b <= 64:
        return 1
    else:
        return 0

a = func(-5, -6)

z = [bool(a)]

# bool関数は、値をTrueまたはFalseに変換する。
# 0はFalse、それ以外の数値はTrueになる。

print(z)
