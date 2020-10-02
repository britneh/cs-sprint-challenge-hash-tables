"""
numbers that exist in all lists
"""

def intersection(arrays):
    store = {}

    for list in arrays:
        for item in list:
            if item not in store:
                store[item] = 0
            if item in store:
                store[item] += 1
    result= []

    for key, value in store.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
