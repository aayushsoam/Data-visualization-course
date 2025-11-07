# make mirror operation using zip function and user input
input_string = input("Enter a string : ")
n=int(input("enter n:"))


alphabet="abcdefghijklmnopqrstuvwxyz"
reverse_alphabet= alphabet[::-1]
dict = dict(zip(alphabet, reverse_alphabet))


prefix = input_string[0:n-1]
suffix = input_string[n-1:]

mirror=""
for i in range(0, len(suffix)):
    mirror += dict[suffix[i]]
    
result = prefix + mirror
print("Mirror operation result:", result)
    


