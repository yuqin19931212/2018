#字典扁平化
source = {'a': {'b': 1}, 'd': {'c': 2}}
def flatmaps(src):
    def flatmap(src,dest=None, prefix = " "):
        for k, v in src.items():
            if isinstance(v, (list, tuple, set, dict)):
                flatmap(v, dest, prefix=prefix + k + '.')
            else:
                dest[prefix + k] = v

    dest = {}
    flatmap(src, dest)
    return dest

print(flatmaps(source))







