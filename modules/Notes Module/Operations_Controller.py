# -- External Imports --#
from pathlib import Path 

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

# -- Check for Init -- #
def fetch_file_init(file):
    if "__init__" in dir(file):
        # Return the __init__ function
        return file.__init__
    else:
        return None

# -- Fetch Notes Operations --#
def fetch_note_operations():
    # Fetch all of the operations in the operations folder
    for operation in operations_path.iterdir():
        if operation.is_file() and operation.suffix == suffix:
            # Get the __init__ function from the file
            fetch_init = fetch_file_init(operation)
            if fetch_init is None:
                print("No __init__ found in file")
                break

           # Creates new operation class, and adds to operation list
            operation = operation_class(operation.stem, fetch_init)
            Notes_Operations_List.append(operation)

# -- Notes Controller --#


# -- Init -- #
fetch_note_operations()

# -- Debugging -- #
print(f"Note Operations List: {Notes_Operations_List}")
print(f"Note Operations Lsit: {Notes_Operations_List[0].name}")    
print(f"Function: {Notes_Operations_List[0].function}")

print(Notes_Operations_List[0].function())