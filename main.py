import numpy as np
arr = None
class numpy_analyzer():
     
     def create_array(self):
          try:
               print("select the type of array to create")
               print("1. 1D array")
               print("2. 2D array")
               print("3. 3D array")

               choice = int(input("Enter your Choice Number (1-3)"))

               if choice == 1:
                    element = input("Enter the element").split()
                    element = list(map(int,element))
                    arr = np.array(element)
                    print(arr)
                    return arr
                    

               elif choice == 2:
                    rows = int(input("Enter the number of row"))
                    cols = int(input("Enter the number of cols"))
                    element = input(f"Enter the {rows*cols} elements for the array separated by space").split()
                    element = list(map(int,element))
                    arr = np.array(element).reshape((rows,cols))
                    print(arr)
                    return arr

               elif choice == 3:
                    layer = int(input("Enter the number of layer"))
                    rows = int(input("Enter the number of rows"))
                    cols = int(input("Enter the number of cols"))
                    element = input(f"Enter the {layer*rows*cols} elements for the array separated by space").split()
                    element = list(map(int,element))
                    arr = np.array(element).reshape((layer,rows,cols))
                    print(arr)
                    return arr
                    
               
               else:
                     print("Invalid choice number")
                    
          except:

                    print("Invalid Number")  

obj = numpy_analyzer()
def main_menu():               
    while True:

      print("welcome to the Numpy analyzer")
      print("******************************")
      print("choose an option")
      print("1. Create a Numpy array")
      print("2. Perform mathematical operations")
      print("3. Combine or split arrays")
      print("4. Search, sort, or filter arrays")                 
      print("5. Compute Aggregates and Statistics")
      print("6. Exit")

      choice = int(input("Enter your choice number"))

      if choice == 1:
           arr = obj.create_array()
      
      elif choice == 2:
           pass
      
      elif choice == 3:
           pass
      
      elif choice == 4:
           pass
      
      elif choice == 5:
           pass
      
      elif choice == 6:
           print("Exiting Numpy Analyzer")
           break
      
      else:
         print("Invalid choice Number")  

if __name__ == "__main__":
     main_menu()            