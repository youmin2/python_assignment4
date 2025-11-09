#25
key = input().split()
values = map(int, input().split())

a = dict(zip(key, values))

del a['alpha']
del a['delta']

print(a)

#26
park = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
print((park['english']), (park['science']))

#27
kim = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
kim.update(korean=100, english=100, mathematics=100, science=100)
print(kim)

#28
lee = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
lee = {key: value for key, value in lee.items() if key != 'english'}
print(lee)

#29
lim = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
print(lim)

#30
choi = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
choi = {key: value for key, value in choi.items() if value >= 90}
print(choi.keys())

#31
yoo = {'korean':94, 'english':91, 'mathematics':89, 'science':83}

a = 0
for i in yoo.values():
    a += i

b = a / 4
print(b)