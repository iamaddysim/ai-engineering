old_list = []
old_list.append(input("Enter a number: "))
old_list.append(input("Enter another number: "))
old_list.append(input("Enter another number: "))
old_list.append(input("Enter another number: "))
old_list.append(input("Enter another number: "))


new_list = old_list.copy()
new_list.reverse()


if (new_list == old_list):
    print("It is a palindrome")

else: 
    print("It is not a palindrome")
