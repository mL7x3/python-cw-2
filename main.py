my_name = input("what your name : ")
my_age = int(input("how old are you? : "))
print(f"ok {my_name}, your age is {my_age}")

first_number = int(input("enter the first number : "))
secound_number = int(input("enter the secound number : "))
operation = input("enter operation : ")

if operation == "+":
    print(first_number + secound_number)
elif operation == "-":
    print(first_number - secound_number)
elif operation == "*":
    print(first_number * secound_number)
elif operation == "/":
    print(first_number / secound_number)
else:
    print("operation is not validthe (*,+,-,/)")

bus_capacity = 25
rkab = int(input("enter al rkab : "))
km_ale_ra7_yrkbon = int(input("enter 3dd ale ra7 yd5lon : "))

result = rkab + km_ale_ra7_yrkbon

if result > bus_capacity:
    print("ya walad ma ykfe")
elif result < bus_capacity:
    print("ok (:")
else:
    print("ok")

