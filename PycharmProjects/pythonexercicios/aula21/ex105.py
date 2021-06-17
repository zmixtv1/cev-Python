def notas(*n, sit=False):
    r= dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["média"] = sum(n)/len(n)
    if sit:
        if r["média"] >= 7:
            r["situação"] = "Boa"
        elif r["média"] >= 5:
            r["situação"] = "Razoável"
        else:
            r["situação"] = "Ruim"
    return r


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
