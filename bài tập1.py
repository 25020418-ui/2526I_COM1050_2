def kiemtratamgiac(a, b, c): 
    if a + b <= c or a + c <= b or b + c <= a:
      print("Không phải tam giác")
    if a == b == c:
        print("Đây là tam giác đều")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Đây là tam giác vuông")
    elif a == b or b == c or a == c:
        print("Đây là tam giác thường")
    else:
        print("Là tam giác thường")
       
a = int(input())
b = int(input())
c = int(input())
kiemtratamgiac(a, b, c)

        