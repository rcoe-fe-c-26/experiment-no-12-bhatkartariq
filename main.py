# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder:
# Date:

#print("--- Extracting Words from Text File ---\n")
num = int(input("Enter Length of Words: "))
words = []
file=open("story.txt","r")
content = file.read().split()
for i in content:
    if len(i) == num:
        words.append(i)
words=set(words)
words=list(words)
words.sort
print(f"Following Unique words of length 8 present: {words}")


