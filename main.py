def primfaktoren(zahl: int) -> list:
    faktor: int = 2
    _primfaktoren: list = list()
    while zahl > 1:
        while zahl % faktor == 0:
            _primfaktoren += [faktor]
            zahl /= faktor
        faktor += 1
    return _primfaktoren


print(primfaktoren(eval(input('geben Sie eine natürliche Zahl ein: '))))
