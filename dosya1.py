def printLine():
    for x in range(6):
        for y in range(20):
            if y == 0:
                print('|', end="")
            elif y == 6 - x:
                print('/', end="")
            elif x == 5:
                print('_', end="")
            else:
                print('*', end="")
        print("\n")

if __name__ == "__main__":
    printLine()