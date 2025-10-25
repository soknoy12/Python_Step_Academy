# Ex 1 reverse 
# x = input("Enter value:  ")
# # print(x[::-1])

# print("".join(reversed(x))) ## other way

# EX2 count char by vowel and consonate
# st = input("Enter value: ")
# vowel_dict = 'aeiou'
# vowel = 0
# consonate = 0
# for char in st:
#     if char.isalpha():
#         if char.lower() in vowel_dict:
#          vowel +=1
#         else:
#             consonate +=1
# print(f"Vowels: {vowel} , consonates: {consonate}")


# EX3  panlindrom word
# str1 = input("Enter value: ")
# if str1 == str1[::-1]:
#     print(f"str1 {str1} is pamlindrom")
# else:
#     print(f"str {str} is not panlindrom")

# Ex4  longest word
# sentence = input("enter value: ")
# sentence_list = sentence.split()
# for word in sentence_list:
#     temp = word 
#     if len(word) < temp(temp):
#         temp = word
# print(temp)

# print(max(sentence_list, key = len)) ##other way

# EX5 replace space by " _ "
# w = input("Enter values: ")
# w_list = w.split()
# print("_".join(w_list))

# Ex6 sum of num by input(not using loop)
# num = input("Enter num: ")
# num2 = list(map(int, num.strip().split(" ")))
# print(num2)
# print(sum(num2))

# EX7 max and min
# num = input("Enter num: ")
# num2 = list(map(int, num.strip().split(" ")))
# print(f" max = {max(num2)} , min = {min(num2)}")

# # EX8 set of list
# num = list(map(int, input("Enter number: ").strip().split()))
# num2 = list(dict.fromkeys(num))
# print(num2)
# # other way
# input = input("Enter num").strip()
# list_input = input.split()
# list_convert_int = map(int, list_input)
# print(list(set(list_convert_int)))

# # other way
# print (list(set(list(map(int, input("enter number: ").strip().split())))))

# EX9 count most num
# num = list(map(int, input("Enter numbers: ").strip().split()))

# num_most = max(num, key=num.count)

# print("value:", num_most)
# print("Count:", num.count(num_most))

# EX10 list + list
# list1 = list(map(int, input("Enter number: ").strip().split()))
# list2 = list(map(int, input("Enter number: ").strip().split()))
# merge_list = set(list1 + list2)
# print(merge_list)

# EX11 print only second largest
# list1 = list(map(int, input("Enter number: ").strip().split()))
# list_max = max(list1)
# list1.remove(list_max)
# list2 = max(list1)
# print("Second largest", list2)

# EX12 print only common between 2 list
# list1 = list(map(int, input("Enter number: ").strip().split()))
# list2 = list(map(int, input("Enter number: ").strip().split()))

# common_num_set = set(list1) & set(list2) ## " & " and " .intersection() " looking for common
# common_num_list = list(common_num_set)
# print(common_num_list)

# EX13 delete dupe print unique
nums = list(map(int, input("Enter number: ").strip().split()))
unique = list(filter(lambda x: nums.count(x) == 1, nums))
print(unique)






               








        
