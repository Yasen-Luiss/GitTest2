# number = 15
#
# if number % 10 == 5:
#     print("yes")
# else:
#     print(f"{number%10}")
#
# s1 = 'hello'            # string
# s2 = "world"            # string
# s1 + ',\n' + s2 + '!'   # string, for strings the + operator is the concatenation
# print(s1 + ',\n' + s2 + '!')


Y = eval(input('does it rain? '))
Z = eval(input('is it cloudy? '))
# Y and Z are either True or False
if Y:  # if Y is True, the following block is executed
    print("I stay home")
elif Z:  # else if (shortened elif) Z is True, this other block is executed
    print("I go out, but I bring my umbrella")
else:  # else (i.e., if all previous conditions were False) the last block is executed
    print("I go out without the umbrella")