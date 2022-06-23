h, b, c, s = map(int, input().split())

k = h * b * c * s / 8 / 1024 / 1024

print(format(k, '.1f'), "MB")