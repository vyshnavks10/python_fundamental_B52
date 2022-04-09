mark = int(input("enter your mark:"))
if mark >= 90:
    print("A grade")
    if mark > 92:
        print("congratulation you done it")
elif mark >= 80:
    print("B grade")
elif mark >= 60:
    print("c grade")
elif mark >= 35:
    print("pass")
else:
    print("failed")
