import importlib

import _39_m

print(_39_m.variavel)

for i in range(10):
    importlib.reload(_39_m)
    print(i)

print('Fim')