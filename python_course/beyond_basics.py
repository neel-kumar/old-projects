temperatures = [10, -20, -289, 100]

def c_to_f(c):
    if c < -273.15:
        # print ("if block")
        return "That temperature doesn't make sense!"
    else:
        # print("else block")
        f = c* 9/5 + 32
        # print(f)
        return f

for t in temperatures:
    if c_to_f(t) != "That temperature doesn't make sense!":
        with open("/Users/soumitra/Desktop/python_course/temp.txt", "a") as myfile:
            text = str(c_to_f(t))
            print(text)
            myfile.write(text + "\n")
