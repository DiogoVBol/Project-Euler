# Largest Palindrome Product (4)

found = False

for i in range(999, 899, -1):

    for j in range(999, 899, -1):

        number = i * j

        reversal_number = str(number)[::-1]

        if str(number) == reversal_number:

            print(number, "é um palindrome number")

            found = True 

    if found == True:
        break