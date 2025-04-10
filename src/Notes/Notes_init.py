'''
Notes_Module:
    -> Note_Operations_List
    -> Note_Controller
        -> Fetch_Notes_Operations
        -> Automatically handle all of the operations, and their related functions
        -> Init_Note_Operation
            -> Initiates the specific Operation
    -> Note_Operations
        -> Add_Note
        -> Delete_Note
        -> Edit_Note
        -> View_Notes
'''

'''
    Operation Name: 
    Operation Description:
    Operation Attached Function:
'''
# -- External Imports --#

# -- Local Imports --#
from Classes import operations_class
from Classes import note_class

# -- Constants --#
operations = []

# -- Operation Classes -- #
from Classes.operations_class import add_note
from Classes.operations_class import modify_note
from Classes.operations_class import delete_note


# -- Calling Functions -- #