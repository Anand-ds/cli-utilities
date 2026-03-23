from tools.calculator import calculator
from tools.todo import todo_menu

def main():
  while True:
      print ("\n=== CLI-Utilities ===")
      print ("1.Calculator")
      print ("2.To-Do List")
      print ("3.Exit")

      choice = Input("Choose an option")

      if choice == "1":
        calculator()
      elif choice == "2":
        todo_menu()
elif choice == "3":
  print ("Goodbye!")
  break
else:
  print ("Invalid choice. try again.")

if __name__ == "__main__":
  main()
  
