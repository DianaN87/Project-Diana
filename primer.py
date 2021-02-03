# a=5
# b=4
# c=3
# half_perimeter=(a+b+c)/2
# print(half_perimeter)
# triangle_area = (half_perimeter*(half_perimeter-a)*(half_perimeter-b)*(half_perimeter-c))**0.5
#
# a= float(input("Please enter side A"))
# b= float(input("Please enter side B"))
# c= float(input("Please enter side c"))
# half_perimeter=(a+b+c)/2
# print(half_perimeter)
# triangle_area = (half_perimeter*(half_perimeter-a)*(half_perimeter-b)*(half_perimeter-c))**0.5
# a, b, c= 4, 5, 6
# print (a)
# print (b)
# print (c)
# half_perimeter=(a+b+c)/2
# print(half_perimeter)
# triangle_area = (half_perimeter*(half_perimeter-a)*(half_perimeter-b)*(half_perimeter-c))**0.5

a, b, c=input("Please enter 3 sides: ").split (" ")

half_perimeter= (float(a)+float(b)+float (c))/2
print(half_perimeter)
triangle_area = (half_perimeter*(half_perimeter-float(a))*(half_perimeter-float(b))*(half_perimeter-float(c)))**0.5
print(triangle_area)