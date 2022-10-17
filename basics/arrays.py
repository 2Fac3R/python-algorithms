import array

if __name__ == '__main__':
    myArray = array.array('i', [300, 100, 500, 200])

    myArray.insert(1, 1)
    myArray.remove(500)
    myArray[0] = 250

    print(myArray[1])
    print(myArray.index(200))
    print(myArray)

    for item in myArray:
        print(item)