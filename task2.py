import re


list1 = list(range(1, 11))

numbers_str = str(list1)


match_obj= re.findall(r'\d+', numbers_str)[:5]
first_five = list(map(int, match_obj))

Reversed_string = first_five[::-1]

print(f"Original list: {list1}")
print(f"Extracted first five elements: {first_five}")
print(f"Reversed extracted elements: {Reversed_string}")
