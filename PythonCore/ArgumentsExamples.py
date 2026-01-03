def pizza(*toppings):
    print("Pizza Name:",toppings)
pizza("onion","crunchy","olive")


def collect_student_data(*student):
    print("Student Name:",student)
    print(type(student))
collect_student_data("self",19,50.0,"M")

def collect_student_data1(**student):
    print("Student Name:",student)
    print(type(student))
collect_student_data1(name="self",age=19,weight=50.0,gender="M")


