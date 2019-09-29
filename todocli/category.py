
# CONSTANTS ---------------------------------------------------------------------------------------

CATERORY_TASK_FILE_DIR = '~/.todocli/cats'
DEFAULT_CATEGORY_FILE = '~/.todocli/default_cat'

# PRIVATE FUNCTIONS -------------------------------------------------------------------------------

def _get_category_file_path(category):
    return ''

def _check_category_exists(category):
    # Get the file name for the category
    # Check if the file exists
    return False

def _create_category(category_file_path):
    # Check that the category exists. If it does then exit
    
    # Write the text for the unfinished and finished sections of the categorys to the category_file_path
    #   use _write_sections function
    pass

def _append_tasks_to_category_section(category_file_path, section_name, tasks):
    # Get tasks for all the sections in the category file and put it in a dict (key is section_name,
    #   value is list of tasks in that section)

    # Append the tasks to the appropriate section list

    # Write all the sections to the category file
    pass

def _write_sections_to_category_file(category_file_path, sections):
    pass

def _get_sections_data_for_category(category_file_path):
    # Read the category_file_path file line by line
        # If line starts with '#' then it is a section heading
        # Ignore any blank lines
        # Each line that starts with a '\d\. ?[X?]/i' regex is a task
            # Read the comment with the create and write times and convert them to datetime objs
            # Get the ID from the number at the front of the task
        # Any line between two tasks is part of the task that came before
    pass

def _get_tasks_from_user(category_file_path):
    # Create a temp file
    # Open the temp file in the default editor
    # Extract the data from the temp file and return it
    return ''

def _add_bulleted_tasks_to_category(category_file_path):
    # Extract Each main bullet point

    # Read the current max task ID from the category

    # For each bullet point
        # Assign an ID to it higher than the highest ID in the existing category
        # Given each task a create time
        # Store the data in a dict

    # Write the data to the unfinished section
    _append_tasks_to_category_section(category_file_path, 'Unfinished', [])
    pass

# PUBLIC FUNCTIONS --------------------------------------------------------------------------------

def get_default_category():
    # Read the value in default_cat file
    return ''

def set_default_category(category):
    # Check that the category exists. Throw error if it does not exist
    # Write the category name to default_cat file
    pass

def add_to_category(category=''):
    if not category:
        category = get_default_category()

    # Get the new tasks from the user
    # Append the tasks to unfinished section of the categorys

    pass
