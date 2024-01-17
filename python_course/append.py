with open("/Users/soumitra/Desktop/python_course/file1.txt", "r") as first:
    first = first.read()
    with open("/Users/soumitra/Desktop/python_course/file2.txt", "r") as second:
        second = second.read()
        with open("/Users/soumitra/Desktop/python_course/file3.txt", "r") as third:
            third = third.read()
with open("/Users/soumitra/Desktop/python_course/file123.txt", "a") as file123:
    file123 = file123.write(first + "\n" + second + "\n" + third + "\n")
