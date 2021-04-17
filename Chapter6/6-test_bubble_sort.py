#  定义一个被测函数List升序
def ascending_order(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] > list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
#  定义一个被测函数List降序
def descending_order(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] < list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
'''
定义4个List
'''
list1 = [2, 10, 25, 30, 45, 100, 325]
list3 = [325, 10, 25, 45, 30, 100, 2]
list4 = [11, 3, 41, 101, 327, 26, 46]
list2 = [327, 101, 46, 41, 26, 11, 3]
#  定义测试降序函数的测试方法
def test_descending_order():
    list5 = descending_order(list4)
    assert list5==list2  #  断言
#  定义测试升序函数的测试方法
def test_ascending_order():
    list6 = ascending_order(list3)
    assert list6==list1  # 断言  

if __name__ == '__main__':
    test_descending_order()
    test_ascending_order()
    