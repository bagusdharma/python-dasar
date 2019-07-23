def add_to(num, target=[]): #ingat list harus dibelakang
    target.append(num)
    return target
add_to(1)

def add_to2(element, target2=None):
    if target2 is None:
        target2 = []
        target2.append(element)
        return target2

add_to2(3)