# -- External Imports --#
from pathlib import Path 
import importlib.util

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
        self.function = function # Function attached to operation

    def call_function(self):
        # Call the function attached to the operation
        return self.function()

# -- Check for Init -- #
def fetch_file_init(file_path):
    file_name = {str(file_path.stem + suffix)}
    print(f"File Name Thing: {str(file_name)}")
    file_name = str(file_name).replace("'" , "")
    print(f"File Name Thing 2: {str(file_name)}")
    file_name = str(file_name).replace("{" , "")
    file_name = str(file_name).replace("}" , "")

    print(f"File Name: {file_name}")
    file_total_name = str(file_name)
    print("File Total Name: ", file_total_name)
    
    try:
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, "__init__"):
            return getattr(module, "__init__")
        else:
            return None
    except Exception as error:
        print(f"Error: {error}")
        return None

  #  if hasattr(file_Init, "__init__"):
  #      return getattr(file_Init, "__init__")
  #  else:
  #      return None

# -- Fetch Notes Operations --#
def fetch_note_operations():
    # Fetch all of the operations in the operations folder
    for operation in operations_path.iterdir():
        if operation.is_file() and operation.suffix == suffix:
            # Get the __init__ function from the file
            fetch_init = fetch_file_init(operation)
            print(f"Fetch Init: {fetch_init}")
            print(f"Fetch Init Function: {fetch_init()}")
            if fetch_init is None:
                print("No __init__ found in file")
                break

           # Creates new operation class, and adds to operation list
            operation = operation_class(operation.stem, fetch_init)
            print(f"Number: {operation.call_function()}")
            Notes_Operations_List.append(operation)

# -- Notes Controller --#


# -- Init -- #
fetch_note_operations()

# -- Debugging -- #
print(f"Note Operations List: {Notes_Operations_List}")
print(f"Note Operations Lsit: {Notes_Operations_List[0].name}")    
print(f"Function: {Notes_Operations_List[0].function}")

print(f"Function called: {Notes_Operations_List[0].call_function()}")