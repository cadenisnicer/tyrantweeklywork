import math

print("X equals negative B, plus or minus the square root of B squared minus 4AC, all over 2A ")
print("Please input a, b, and c of your quadratic equation to find x")
print("ax^2 + bx + c")

def uinput(): #this function is solely responsible for handling user input and then passing on the variables onto the quadratic function that does the calculation
  while True: # Begins a loop until valid input is received and passed onto quadratic()
    try:
      a = float(input("enter your a value "))
      b = float(input("enter your b value "))
      c = float(input("enter your c value "))
      print(a,"x^2 +", b,"x +", "(",c,")")
      return a, b, c
    except ValueError: #allows user to re-enter values if invalid without crashing
      print("Invalid input. Enter real numbers only")
      continue

a, b, c = uinput()

def quadratic(a, b, c): #the function responsible for the actual calculation
  discriminant = math.pow(b, 2) - 4 * a * c
  if discriminant >= 0: #discriminant can not be negative
    #quadratic formula has a plus or minus section where you must do the calculation for both adding and subtracting which is why the next 2 lines are addans(answer if you were to add) and subans (answer if you were to subtract)
    addans = (-b + math.sqrt(discriminant)) / (2 * a) 
    subans = (-b - math.sqrt(discriminant)) / (2 * a)
    print("x =",addans,",",subans)
  else:
    print("discriminant can not be negative")
    uinput()

quadratic(a, b, c)

