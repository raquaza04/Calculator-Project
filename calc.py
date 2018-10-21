from math import sqrt

user = input("Do you want to find (Q)uadratic formula, (C)alulator, or (G)et slope-intercept \nfrom two points: ")
if user == "Q":
    a = int(input("Enter the coefficients of a: "))
    b = int(input("Enter the coefficients of b: "))
    c = int(input("Enter the coefficients of c: "))

    d = b**2-4*a*c # discriminant

    if d < 0:
        print ("This equation has no real solution")
    elif d == 0:
        x = (-b+sqrt(b**2-4*a*c))/2*a
        print ("This equation has one solutions: "), x
    else:
        x1 = (-b+sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-sqrt((b**2)-(4*(a*c))))/(2*a)
        print ("This equation has two solutions: ", x1, " or", x2)
elif user == "C":
    inp = input("Would you like to (A)dd, (S)ubtract, (M)ultiply, or (D)ivide: ")
    if inp == "A":
        n = int(input("Enter first number: "))
        m = int(input("Enter second number: "))
        print(n+m)
    elif inp == "S":
        q = int(input("Enter first number: "))
        w = int(input("Enter second number: "))
        print(m-n)
    elif inp == "M":
        e = int(input("Enter first number: "))
        r = int(input("Enter second number: "))
        print(m*n)
    elif inp == "D":
        t = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
elif user == "G":
    x1, y1 = input("Enter the first point seperated by commas (don't include parentheses): ").split(",")
    x2, y2 = input("Enter the next point: ").split(",")
    slope = (int(y1)-int(y2)) / (int(x1)-int(x2))
    #print(type(slope))
    yint = ((int(x1)*-1)* slope) + int(y1)
    if yint > 0:
        equation = "y = " + str(slope) +  "x " + "+ " + str(yint)
    elif yint == 0:
        equation = "y = " + str(slope) + "x"
    else:
        yint *= -1
        equation = "y = " + str(slope) +  "x " + "- " + str(yint)
    print(equation)
