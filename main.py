import numpy as np
arr = None
class numpy_analyzer():
     
     def create_array(self):
          try:
               print("select the type of array to create")
               print("1. 1D array")
               print("2. 2D array")
               print("3. 3D array")
               print("4. Go Back")

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

               elif choice == 4:
                    print ("return to the main menu \n")
               
               else:
                     print("Invalid choice number")
                    
          except:

               print("Enter your valid number \n")  

     def array_operation(self,arr):
          try:
               print("choose an operation")
               print("1. Indexing")
               print("2. Slicing")
               print("3. Go Back")

               choice = int(input("Enter Your Choice Number (1-3)"))

               if choice == 1:
                   if arr.ndim == 1:
                        index = int(input("Enter your Index"))
                        print(f"element {arr[index]}\n")

                   elif arr.ndim == 2:
                        row = int(input("Enter your row Index"))
                        col = int(input("Enter your col Index"))
                        print(f"element {arr[row,col]}\n")

                   elif arr.ndim == 3:
                        layer = int(input("Enter your layer Index"))
                        row = int(input("Enter your row Index"))
                        col = int(input("Enter ypur col Index"))  
                        print(f"element {arr[layer,row,col]}\n")   

               elif choice == 2:
                     if arr.ndim == 1:
                        start = int(input("Enter the start index"))
                        end = int(input("Enter the end index"))
                        print("sliced array")
                        print(arr[start:end])
                    
                     elif arr.ndim == 2:
                        row_start = int(input("Enter the row start index"))
                        row_end =int(input("Enter the row end index"))
                        col_start = int(input("Enter the col start index"))
                        col_end = int(input("Enter the col end index"))
                        print("sliced array")
                        print(arr[row_start:row_end, col_start:col_end])

                     elif arr.ndim == 3:
                        layer_start = int(input("Enter the layer start index"))
                        layer_end = int(input("Enter the layer end index"))
                        row_start = int(input("Enter the row start index"))
                        row_end =int(input("Enter the row end index"))
                        col_start = int(input("Enter the col start index"))
                        col_end = int(input("Enter the col end index"))
                        print("sliced array")
                        print(arr[layer_start:layer_end,row_start:row_end, col_start:col_end])  

               elif choice == 3:
                        print ("return to the main menu \n")

               else:
                        print("Invalid choice number")

          except:
                print("Enter a valid index or (start-end) Range")             
                        
     def math_operation(self,arr):
          try:
               print("choose an operation")
               print("1. Addition of two array")
               print("2. Subtraction of two array")
               print("3. Multiplication of two array")
               print("4. Division of two array")

               choice = int(input("Enter Your Choice Number (1-4)"))

               if choice == 1 or choice == 2 or choice == 3 or choice == 4:
                    element = input(f"Enter the same-size array element ({arr.size} element separated by space):").split()
                    element = list(map(int,element))

                    if len(element) != arr.size:
                         print(f"Enter exactly {arr.size} element")
                         return

               arr2 = np.array(element).reshape(arr.shape)

               print("\n First array")
               print(arr)

               print("\n Second array")
               print(arr2)

               if choice == 1:
                    print("\n sum of addition")
                    print(np.add(arr, arr2))

               elif choice == 2:
                    print("\n sum of Subtraction")
                    print(np.subtract(arr,arr2))

               elif choice == 3:
                    print("\n sum of Multiplication")
                    print(np.Multiply(arr,arr2))

               elif choice == 4:
                    if np.any(arr2 == 0):
                         print("Division by Zero is not allowed")
                    else:
                         print("\n sum of Division")
                         print(np.divide(arr,arr2))

               else:
                    print("Invalid choice number")                               
         
          except:     
                print("Enter your valid number")

     def combine_split(self,arr):
          try:
               print("choose an operation")
               print("1. Combine two array")
               print("2. Split an array")
               print("3. Go Back")

               choice = int(input("Enter Your Choice Number (1-3)"))

               if choice == 1:
                    element = input(f"Enter the same-size array element ({arr.size} element separated by space):") .split()
                    element = list(map(int,element))

                    if len(element) != arr.size:
                         print(f"Enter exactly {arr.size} element")
                         return

                    arr2 = np.array(element).reshape(arr.shape)

                    print("\n First array")
                    print(arr)

                    print("\n Second array")
                    print(arr2)

                    combined_array = np.vstack((arr, arr2))
                    print("\n Combined array")
                    print(combined_array)

               elif choice == 2: 
                    split_num = int(input("Enter the number split"))
                    if split_num <= 0 or split_num >= arr.shape[0]:
                         print("Invalid split number")
                         return

                    element = np.array_split(arr, split_num, axis = 0)
                    print("\n Split array")
                    i = 1
                    for split in element:
                         print(f"split array {i}")
                         print(split)
                         i += 1

               elif choice == 3:
                    print("return to the main menu \n")   

               else:
                    print("Invalid choice number")            

          except:
               print("Enter your valid number")   


     def search_sort_filter(self,arr):
          try:
             print("choose an operation") 
             print("1. Search  a value") 
             print("2. Sort the array")
             print("3. Filter values")
             print("4. Go Back")

             choice = int(input("Enter Your Choice Number (1-4)"))

             if choice == 1:
                  element = int(input("Enter the element to search"))
                  index = np.argwhere(arr == element)
                  if index[0].size > 0:
                       print(f"element {element} found at index {index} \n")
                  else:
                       print(f"element {element} not found in the array \n")

             elif choice == 2:
                  sort_array = np.sort(arr, axis=None)
                  print("\n sorted array")
                  print(sort_array)
                  print("(sorting applied row-wise) \n")

             elif choice == 3:
                  print("\n choose a filter condition")
                  print("1. Greater thane")
                  print("2. Less thane")
                  print("3. Equal to")

                  choice = int(input("Enter your choice"))

                  value = int(input("Enter the comparison value"))

                  if choice == 1:
                       filtered = arr[arr > value]

                  elif choice == 2:
                       filtered = arr[arr < value]

                  elif choice == 3:
                       filtered = arr[arr == value]

                  else:
                       print("Invalid  filter choice number")                  
                       return
                  print("\n First array")
                  print(arr)
                  print("\n Filtered array")
                  print(filtered) 

             elif choice == 4:
                  print("return to the main menu \n")

             else:
                  print("Invalid choice number")                
            
          except:     
                print("Enter your valid number")   

     def agg_operation(self,arr): 
          try:
            print("-"*10 , "Aggregates and statistics","-"*10)

            print("choose an operation")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Go Back")

            choice = int(input("Enter Your Choice Number (1-4)"))

            if choice == 1:
                 print("First array")
                 print(arr)
                 print("Sum of the first array \n")
                 print(np.sum(arr))

            elif choice == 2:
                 print("First array")
                 print(arr)
                 print("Mean of the fisrt array \n")
                 print(np.mean(arr))

            elif choice == 3:
                 print("First array")
                 print(arr)
                 print("Median of first array \n") 
                 print(np.median(arr))

            else:
                 print("Invalid choice number")         

          except:
               print("Enter your valid number")              

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
           if arr is not None:
                obj.array_operation(arr)
           else:
                print("array is not created")    
      
      elif choice == 2:
            if arr is not None:
                 obj.math_operation(arr)
            else:
                 print("array is not created")        
        
      elif choice == 3:
            if arr is not None:
                 obj.combine_split(arr)
            else:
                 print("array is not created")

      elif choice == 4:
            if arr is not None:
                obj.search_sort_filter(arr)
            else:
                 print("array is not created")    
      elif choice == 5:
           if arr is not None:
                obj.agg_operation(arr)
           else:
                print("array is not created")     
      
      elif choice == 6:
           print("Exiting Numpy Analyzer")
           break
      
      else:
         print("Invalid choice Number")  

 
if __name__ == "__main__":
     main_menu()            