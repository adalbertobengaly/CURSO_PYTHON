def timeConversion(stringTime):
    # Formato '12:40:22AM'
    _h, _m, _s = stringTime.split(":")
    _format = _s[2:]
    _s = _s[:2]

    if _format == 'PM':
        _h = int(_h) + 12
        if _h == 24:
            _h = 12

    if _format == 'AM' and _h == '12':
        _h = 00   

    _h = str(_h).zfill(2)
    _24horas = [_h, _m, _s] 

    return ':'.join(_24horas)


print(timeConversion('12:40:22AM'))
print(timeConversion('12:45:54PM'))
print(timeConversion('07:05:45AM'))