first_mark= int(input())

second_mark=int(input())

third_mark=int(input())

fourth_mark=int(input())

fifth_mark=int(input())





new_list=[]





new_list.append(first_mark)

new_list.append(second_mark)

new_list.append(third_mark)

new_list.append(fourth_mark)

new_list.append(fifth_mark)









for i in new_list:

    if (i>=90 and i<=100):

        print("A",end="")

    elif (i>=80 and i<=89):

        print("B",end="")

    elif(i>=70 and i<=79):

        print("C",end="")

    elif(i>=60 and i<=69):

        print("D",end="")

    elif(i>=50 and i<=59):

        print("E",end="")

    elif(i>=0 and i<=49):

        print("F",end="")

    else:

        print("Not a valid input")