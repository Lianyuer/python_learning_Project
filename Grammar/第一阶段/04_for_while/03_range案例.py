"""
    统计range（1，10）的序列有几个偶数
"""

num = 100
count = 0
for x in range(1, num):
    if x % 2 == 0:
        count += 1
print(f"1-{num}（不包含10）的序列中一共有{count}个偶数")