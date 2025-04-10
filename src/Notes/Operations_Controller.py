# -- External Imports --#
from pathlib import Path 
import importlib.util
import ast
import inspect
import textwrap

# -- Internal Imports --#

# -- Constants --#
base_path = Path(__file__).parent
operations_path = base_path / "Operations"
suffix = ".py"

# -- Notes Operations --#
Notes_Operations_List = []

# -- Operations Class - #
class operation_class:
    # Operation Class
    def __init__(self, name, function):
        self.name = name # Operation Name
        self.function = function  # Function attached to operation

    def call_function(self):
        # Call the function attached to the operation
        return self.function()

# -- Check for Init -- #
'''def fetch_file_init(operation_file_path):
    file_name = {str(operation_file_path.stem + suffix)}
    file_name = str(file_name).replace("'" , "")
    file_name = str(file_name).replace("{" , "")
    file_name = str(file_name).replace("}" , "")

    file_total_name = str(file_name)
    print("File Total Name: ", file_total_name)
    
    with open(operation_file_path, "r", encoding = "utf-8") as file:
        print("Hello")
        
        file_content = ast.parse(file.read())

        for instance in file_content.body:
            if isinstance(instance, ast.FunctionDef) and instance.name == "init":
                print("assdsd")
                print("Instance: ", instance)
                print("Instance Body: ", instance.body)
                print("Inspect: ", inspect.getsource(instance))
                function = textwrap.dedent(str(instance.body))

                list = {}
                exec(function, list)

                return list["init"]

        
     
       #         print("HELLO?")
        #        file_contents = file.read()
         #       if "init" in file_contents:
          #          print(f"Init found in file: {operation_file_path}")
           #         imported_file = importlib.import_module(file_total_name)
            #        print(f"Imported File: {imported_file}")
             #       init = imported_file.init
              #      return init
               # else:
                #    print(f"No init found in file: {operation_file_path}")
                 #   return None

  #  try:
  #      with open(operation_file_path, "r") as file:
  #          print("HELLO?")
  #          file_contents = file.read()
   #         if "init" in file_contents:
    #            print(f"Init found in file: {operation_file_path}")
     #           imported_file = importlib.import_module(file_total_name)
      #          print(f"Imported File: {imported_file}")
       #         init = imported_file.init
        #        return init
         #   else:
          #      print(f"No init found in file: {operation_file_path}")
           #     return None

#        spec = importlib.util.spec_from_file_location("module.name", operation_file_path)
 #       module = importlib.util.module_from_spec(spec)
  #      print("HAHAHA")
  #      if hasattr(module, "init"):
  #          print(f"Has attribute init in file: {operation_file_path}")
   #         return getattr(module, "init")
   #     else:
    #       print("No init found in file: ", operation_file_path)
  #  except Exception as error:
   #     print(f"Error 2: {error}")
    #    print(f"File Path 2: {operation_file_path}")
     #   print(f"File Name 2: {file_total_name}")
      #  pass

  #  if hasattr(file_Init, "__init__"):
  #      return getattr(file_Init, "__init__")
  #  else:
  #      return None '''

# -- Fetch Notes Operations --#
def fetch_note_operations():
    # Fetch all of the operations in the operations folder
    for operation in operations_path.iterdir():
        if operation.is_file() and operation.suffix == suffix:
            # Get the __init__ function from the file
            print("Operation: ", operation)
            fetch_init = fetch_file_init(operation)
            if fetch_init is None:
               print("FETCH INIT No __init__ found in file")
               break

           # Creates new operation class, and adds to operation list
 #           operation = operation_class(operation.stem, fetch_init)
 #           print(f"Number: {operation.call_function()}")
 #           Notes_Operations_List.append(operation)

# -- Notes Controller --#


# -- Init -- #
fetch_note_operations()

# -- Debugging -- #
print(f"Note Operations List: {Notes_Operations_List}")
print(f"Note Operations Lsit: {Notes_Operations_List[0].name}")    
print(f"Function: {Notes_Operations_List[0].function}")

print(f"Function called: {Notes_Operations_List[0].call_function()}")