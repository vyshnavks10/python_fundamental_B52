"""
 Write Python code to open a file named demo.txt and write some random data into it.
   2. Open the file, read the contents and display them as output.
  3. Write python code to add additional text to the existing file on a new line without deleting the previous contents
"""

f = open("demo.txt", "w")
f.write("hai wassup.. how are you doing..!\n")
f = open("demo.txt", "r")
read = f.read()
print(read)
f = open("demo.txt ", "a")
f.write("uh-huh... doing great today")
f = open("demo.txt", "r")
read = f.read()
print(read)
f.close()
