if __name__ == '__main__':
    import array

    my_array = array.array('i', [300, 100, 500, 200])

    my_array.insert(1, 1)
    my_array.remove(500)
    my_array[0] = 250

    print(my_array[1])
    print(my_array.index(200))
    print(my_array.tolist())

    for item in my_array:
        print(item)
