#Question check if the string is palidrome using recrusion and loops and other approaches
#https://youtu.be/uWYF8nL5E1A?si=b5plZ8s3NGRSGy5T


# Consult to video lecture to check if its palidrome or not be loops or recrusion 
# simple approcach

# s=input("Enter a sentence: ")

# x=s[::-1]

# if x==s:
#     print("Its Palidrome")
# else:
#     print("Its not a Palidrome")
# By Loops
# x="niti"
# is_palidrome=True
# for z in range(len(x)//2):
#     if not x[z]==x[-z-1]:
#         is_palidrome=False
#         break
# print(is_palidrome)

# By Recursion
def reverse(a,l,r):
    if l>=r:
        return True
    if not a[l]==a[r]:
        return False

    return reverse(a,l+1,r-1)

a="Rohan"
l,r=0,len(a)-1
print(reverse(a,l,r))


