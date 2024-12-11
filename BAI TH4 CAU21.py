print("Sinh vien : Võ Thế Huy")
print("MSSV : 235752021610031")
print("#################")
input_str = input("Nhap chuoi cac so nhi phan: ")
numbers = input_str.split(',')
result = [num for num in numbers if int(num, 2) % 5 == 0]
print(','.join(result))
