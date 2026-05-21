class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi," + self.name + ",your avg score is: " + str(sum / 3))
        return


s1 = Student("pratik", [99, 98, 99])
s2 = Student("kartik", [99, 99, 99])
s1.get_avg()
s2.get_avg()