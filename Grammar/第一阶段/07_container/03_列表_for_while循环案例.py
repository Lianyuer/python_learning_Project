"""
    取出列表内的偶数
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
index = 0
while index < len(my_list):
    element = my_list[index]
    if element % 2 == 0:
        new_list.append(element)
    index += 1
print(f"通过while循环，从列表[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]中取出偶数，组成新列表{new_list}")

new_list = []
for element in my_list:
    if element % 2 == 0:
        new_list.append(element)
print(f"通过for循环，从列表[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]中取出偶数，组成新列表{new_list}")


