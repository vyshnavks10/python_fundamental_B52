# marks = []
# # #taking in the input for 5 marks from the user and adding it to the list
# for i in range(5):
#     marks.append(int(input()))
# # # now that we have all the marks we can just loop over it
# # print(marks[i])
# # output = ""
#     for i in marks:
#         # marks = int(input("enter your mark:"))
#         if marks >= 90:
#             print("A grade")
#             if marks > 92:
#                 print("congratulation you done it")
#         elif marks >= 80:
#             print("B grade")
#         elif marks >= 60:
#             print("c grade")
#         elif marks >= 35:
#             print("pass")
#         else:
#             print("failed")
#
#     #Write your code here
#     #for every mark concatenate grades to the output e.g output+="A"
#     #start here
#
#     #now we simply print the output
# print(marks)
marks = []

for i in range(5):
    marks.append(int(input("enter the marks:")))

for i in marks:
    if (i >= 90 and i <= 100):
        print("A")
    elif (i >= 80 and i <= 89):
        print("B")
    elif (i >= 70 and i <= 79):
        print("C")
    elif (i >= 60 and i <= 69):
        print("D")
    elif (i >= 50 and i <= 59):
        print("E")
    else:
        print("F")

# another type of programe with same meaning
marks = []

for i in range(5):
    marks.append(int(input("enter the marks:")))

for i in marks:
    if (i >= 90 and i <= 100):
        print("A",end="")
    elif (i >= 80 and i <= 89):
        print("B",end="")
    elif (i >= 70 and i <= 79):
        print("C",end="")
    elif (i >= 60 and i <= 69):
        print("D",end="")
    elif (i >= 50 and i <= 59):
        print("E",end="")
    else:
        print("F",end="")