# n=5
# for i in range (0,n+1):
#     for j in range (i):
#         print ('*',end='')
#     print('')
# for k in range (1,n+1):
#     for l in range(k,n):
#         print ('*',end='')
#     print('')

# *****
# *   *
# *   *
# *   *
# *****

# n=5
# for i in range (0,n):
#     for j in range(0,n):
#         if i ==0 or j ==0 or i ==n-1 or j ==n-1:
#             print( "*",end="")
#         else:
#             print(" ",end="")
#     print("\n")


# __________________________________________________


# **********
# *        *
# *        *
# **********

# l=10
# b=4

# for i in range (0,b):
#     for j in range (0,l):
#         if i==0 or j==0 or i==b-1 or j==l-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("\n")
# ______________________________________________


#      *
#     ***
#    *****
#   *******
#  *********

# l=5 mine
# for i in range (1,l+1):
#     for j in range(l-i):
#         print(" ",end="")
#     for k in range (i+(i-1)):
#         print("*",end="")
#     print("\n")

# l=5  
# for i in range (1,l+1):
#     for j in range(l-i):
#         print(" ",end="")
#     for k in range (2*i-1):
#         print("*",end="")
#     print("\n")

# ________________________________________________


# l=5
# for i in range (1,l+1):
#     for j in range (i,l+1):
#         print("*",end="")
#     print("\n")

# for k in range (2,l+1):
#     for m in range (k):
#         print("*",end="")
#     print("\n")

# ____________________________________


# n=5
# for i in range(1,n+1):
#     for j in range (n-i):
#         print(" ",end="")
#     for k in range (i+(i-1)):
#         print("*",end="")
#     print("\n")

# for l in range (1,n):
#     for m in range (l):
#         print(" ",end="")
#     for p in range ((n-l)*2-1):
#         print("*",end="")
#     print("\n")

#     *

#    ***

#   *****

#  *******

# *********

#  *******

#   *****

#    ***

#     *

# _______________________________________________

# n=5
# for i in range (1,n+1):
#     for j in range (n-i):
#         print (" ",end="")
#     for k in range (i):
#         print ("*",end="")
#     print("\n")

# for l in range (1,n):
#     for m in range (n-l):
#          print ("*",end="")
#     print("\n")

#     *

#    **

#   ***

#  ****

# *****

# ****

# ***

# **

# *

# __________________________________________________


# **********
# *
# *
# *
# **********
# n = 10
# for i in range (0,n-5):
#     for j in range(1,n+1):
#         if i==0 or j==1 or i==n-5-1:
#             print ("*",end="")
#         else:
#             print(" ",end="") 
#     print("\n")

n = int(input("enter any number : "))
for i in range (1,n+1):
    for j in range (1,i):
        if i == 1 or j ==1 or i == j or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")

# * 

# * *

# *   *

# *     *

# * * * * *
# _________________________________________________________



    