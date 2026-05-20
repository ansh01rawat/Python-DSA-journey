
def marks_analyzer(marks):
    average = sum(marks)/len(marks)
    highest = max(marks)
    lowest = min(marks)

    pass_count = 0
    fail_count = 0

    for mark in marks:
        if mark >= 40:
            pass_count += 1
        else:
            fail_count += 1

    print("Average marks:",average)
    print("Highest mark:",highest)
    print("Lowest mark:",lowest)
    print("Pass count:",pass_count)
    print("Fail count:",fail_count)



marks = [89,97,98,95,79,34,32,40,99,98]
marks_analyzer(marks)
