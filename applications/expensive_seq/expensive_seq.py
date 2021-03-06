cache = {}
def expensive_seq(x, y, z):
    # check if we can return a cached version
    if (x, y, z) in cache:
        return cache[(x, y, z)]
    # if not then we are going to have to compute the function
    else:
        if x <= 0:
            cache[(x, y, z)] = y + z
        if x >  0:
            cache[(x, y, z)] = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
        return cache[(x, y, z)]


if __name__ == "__main__":
    for i in range(50):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"count : {i} | {i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
