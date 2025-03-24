# -- External Imports --#
from pathlib import Path 

# -- Internal Imports --#

# -- Constants --#
base_path = Path(__file__).parent
operations_path = base_path / "Operations"

# -- Notes Operations --#
Notes_Operations_List = []

# -- Check for Init -- #
def fetch_file_init(file):
    if "__init__" in dir(file):
        return file.__init__
    else:
        return None

# -- Fetch Notes Operations --#
def fetch_note_operations():
    for operation in operations_path.iterdir():
        if operation.is_file() and operation.suffix == ".py":
            fetch_init = fetch_file_init(operation)
            if fetch_init is None:
                print("No __init__ found in file")
                break
            
            operation = []
            operation.append(operation.stem)
            operation.append(fetch_init())
            Notes_Operations_List.append(operation)

# -- Notes Controller --#


# -- Init -- #