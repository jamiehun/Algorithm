# 1024 768 24

w, h, b = map(int, input().split())

k = w * h * b / 8 / 1024 / 1024 

print(format(k, '.2f'), "MB")