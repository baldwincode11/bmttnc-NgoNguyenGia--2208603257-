def tao_tuple_tu_list(lst):
    return tuple(lst)
    
input_list = input("nhap danh sach cac so, cach nhau bang dau phay:")
number = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(number)
print("list:", number)
print("tuple tu list:", my_tuple)