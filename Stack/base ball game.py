def calPoints(lists):
    x = []

    for i in range(len(lists)):
        if lists[i] == "C":
            x.pop()
        elif lists[i] == "D":
            x.append(int(x[-1]*2))
        elif lists[i] == "+":
            x.append(int(x[-1]+x[-2]))
        else:
            x.append(int(lists[i]))
    return sum(x)

operations = ["5","2","C","D","+"]
print(calPoints(operations))
