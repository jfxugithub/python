nu_list = [5, 3, 6, 1, 0, 7, 10, 9]
##选择排序法
for i in range(len(nu_list) - 1, 0, -1):  # 从后往前获取下标
    max_val_index = i
    # 在i位下标前所有的数中查找比nu_list[i]大的数,把最大值的下标赋值给max_val_index
    for j in range(0, i):
        if nu_list[j] > nu_list[max_val_index]:
            max_val_index = j
    # 交换数据,使查找到的最大值赋值给nu_list[i]
    nu_list[max_val_index], nu_list[i] = nu_list[i], nu_list[max_val_index]

print(nu_list)

nu_list = [5, 3, 6, 1, 0, 7, 10, 9]


# 冒泡排序法
def bubble_sort(nu_list):
    # 获取列表中的所有下标(最后一位不需要比较了,因为后面没有数字可以比较了)
    for i in range(0, len(nu_list) - 1):
        # 获取i之后的所有下标,
        for j in range(i + 1, len(nu_list)):
            # 始终保证i位的数字都比之后的所有位的数字小
            if nu_list[i] > nu_list[j]:
                nu_list[i], nu_list[j] = nu_list[j], nu_list[i]
    return nu_list


print(bubble_sort(nu_list))
