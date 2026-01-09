def converter(value):
    value = value.split('-')
    return '/'.join(value)
print(converter('a/b/22'))


