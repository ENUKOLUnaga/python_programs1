


def outer(ref):
    def wrapper(lst):
        if 0 in lst:
            print("0 is present in lst")
        else:
            ref(lst)
    return wrapper
@outer
def get_product(lst):
    p=1
    for i in lst:
        p*=i
    print(p)
mod_get_product=outer(get_product)
mod_get_product([1,2,3,4])
mod_get_product([1,2,3,0])