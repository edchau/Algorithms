"""
Python Write To File

https://www.w3schools.com/python/python_file_write.asp
"""

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# Create File
f = open("myfile.txt", "x")