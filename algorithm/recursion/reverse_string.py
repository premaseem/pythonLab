def recure(var):
    if len(var == 0):
        return ""
    return var[-1] + recure(var[:-1])

print(recure("aseem is a good man"))