
def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_resultline():
    items = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10,
             11, 12, 13, 14, 14, 30, 16, 27, 17, 18, 19,
             19, 20, 25, 26, 26, 27, 28]
    for item in take(25, distinct(items)):
        print(item)

run_resultline()