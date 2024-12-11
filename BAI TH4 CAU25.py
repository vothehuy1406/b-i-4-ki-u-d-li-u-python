print("Sinh vien : Võ Thế Huy")
print("MSSV : 235752021610031")
print("#################")
input_str = input("Nhap day so: ")
numbers = list(map(int, input_str.split(',')))
odd_numbers = [num for num in numbers if num % 2 != 0]
print(",".join(map(str, odd_numbers)))
