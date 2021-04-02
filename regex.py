text = "Emeka's phone number is 361-488-3015, that is his phone number"
import re
pattern = 'phone'
x = re.search(pattern, text)
print(x.span(), x.start(), x.end())
# #using the finall function instead

# matches = re.findall(pattern, text)
# print(matches)

# """Notice that findall returns a list format"""

# for i in re.finditer('phone', text):
#     print(i.group())


# # First pattern matching key \d for numbers
# number = re.search(r"\d{3}-\d{3}-\d{4}", text)
# print(number.group())

# results = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
# new_results = re.search(results,text)
# print(new_results.group(1))


# #additional regex syntax

re.search(r"cat| dog", "the cat is here") # The | acts as an or operator
 
print(re.findall(r'.at', "The cat in the hat sat there")) #The perioda acts like a wild card. Add more dots to increase the length of your wild card

print(re.findall(r'^\d', "1 is a number")) # The ^ symbol stands for starts with. For endswith however use a $ sign. For example (r'\d$', '2 is a number')

# phrase = "there are 3 numbers 34 inside this sentence "

# pattern1 = r'[^\d]+' #The plus operator groups sequences that occur one or more times
# pattern2 = r'[^\d]'# Exclusion operator
# print(re.findall(pattern1, phrase))
# # print(re.findall(pattern2, phrase))

# #To remove punctuations of a string
# Example_string = "Hey, My name is Emeka! How do you do ?"
# Lacking_Punctuations = re.findall(r'[^,!?]', Example_string)
# str = ""
# print(str.join(Lacking_Punctuations))
# print(Lacking_Punctuations)

# Alpha_num = "Hello-Emeka, You are going to look for alphanumeric-characters, to do that use re.findall"
# print(re.findall(r"[\w]+-[\w]", Alpha_num))