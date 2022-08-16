def to_fareingeit(suma):
    def wrapper(c):
        return suma(c)*1.8+32
    return wrapper
@to_fareingeit
def suma(lst):
    return sum(lst)
print(suma([1,4,5,6]))