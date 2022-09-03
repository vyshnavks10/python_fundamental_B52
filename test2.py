text1 = input()

text2 = input()

# vowels = set("aeiou") we can just initialize this later inside the loop instead

# text3 = (text1 + text2).lower()
text3 = [text1.lower(), text2.lower()]

for text in text3:

    # just iterating through them
    vowels = set("aeiou")
    # Write your code here. for each text you have to print("YES") or print("NO") as described in the problem
    for character in text:

        if character in vowels:
            vowels.remove(character)

    if len(vowels) == 0:

        print("YES")

    else:

        print("NO")