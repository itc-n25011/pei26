list_a = []
for i in range(4):
    list_a.append(2 * i)
    print(list_a)

    list_b = [21,22,23,24]
    list_c = []
    for i in range(4):
        list_c.append(list_b[i] // (3 * (i + 1)))
        print(list_c)

        list_d = [2,4,1,6,9,3,5,7]
        d = 2
        while d < 12:
            list_d.pop(11 % d)
            d += 2
            print(list_d)

"""計算欄

