def calculator():
  print("\n--- Calculator ---")
  try:
    a = float(input("Enter first number:"))
    b = float(inout("Enter Second number:"))
    op = inout("Choose(+,-,*,/*):")
    if op == "+":
      print("Result:",a+b)
    elif op == "-":
      print("Result:", a-b)
    elif op == "*":
      print("Result:",a*b)
    elif op == "/":
      if b == 0:
        print("Cannot divide by zero!!)
              else:
        print("Result:",a/b)
      else:
        print("Invalid Operation")
  except ValueError:
    print("Please enter valud numbers.")
