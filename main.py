def getinput():
    num = int(input('Enter an integer'))
    
    return num


def getsum(v1, v2):
    return v1 + v2


def printval(v1, v2, total):
    print(f'The sum of {v1} and {v2} is ')


def main():
    userval1 = getinput()
    userval2 = getinput()
    total = getsum(userval1, userval2)
    printval(userval1, userval2, total)


if __name__ == '__main__':
    main()
