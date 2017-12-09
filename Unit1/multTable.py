def multTable(xmax, ymax):
    for x in range(1, xmax):
        for y in range(1, ymax):
            print(x*y, end="\t")
        print("\n")
multTable(13, 13)
