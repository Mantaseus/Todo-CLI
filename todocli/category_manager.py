from __future__ import print_function
from pprint import pprint
import os
import shelve
import tempfile
import subprocess

# CONSTANTS ---------------------------------------------------------------------------------------

CATEGORY_FILE_DIR = os.path.expanduser('~/.todocli/cats')
DEFAULT_CATEGORY_FILE = os.path.expanduser('~/.todocli/default_cat')

# PRIVATE: TEMP FILE MANAGEMENT -------------------------------------------------------------------
# Copied from https://stackoverflow.com/a/48466593

def _raw_input_editor(default=None, editor=None):
    ''' like the built-in raw_input(), except that it uses a visual
    text editor for ease of editing. Unlike raw_input() it can also
    take a default value. '''
    with tempfile.NamedTemporaryFile(mode='r+') as tmpfile:
        if default:
            tmpfile.write(default)
            tmpfile.flush()
        subprocess.check_call([editor or _get_editor(), tmpfile.name])
        tmpfile.seek(0)
        return tmpfile.read().strip()

def _get_editor():
    return (os.environ.get('VISUAL')
        or os.environ.get('EDITOR')
        or 'vi')

# PRIVATE FUNCTIONS -------------------------------------------------------------------------------

def _append_tasks_to_category_section(category_file_path, section_name, tasks):
    # Get tasks for all the sections in the category file and put it in a dict (key is section_name,
    #   value is list of tasks in that section)

    # Append the tasks to the appropriate section list

    # Write all the sections to the category file
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

def setup_storage_dir():
    if not os.path.exists(CATEGORY_FILE_DIR):
        os.makedirs(CATEGORY_FILE_DIR)

def get_categories():
    return os.listdir(CATEGORY_FILE_DIR)

def get_category_file_path(category):
    return os.path.join(CATEGORY_FILE_DIR, category)

def check_category_exists(category):
    return os.path.isfile(get_category_file_path(category))

def get_default_category():
    try:
        with open(DEFAULT_CATEGORY_FILE, 'r') as default_cat_file:
            return default_cat_file
    except:
        pass
    return ''

def set_default_category(category):
    # Check that the category exists. Throw error if it does not exist
    if not check_category_exists(category):
        print("Can not set a nonexistent category '{}' as the default category".format(category))
        return

    # Write the category name to default_cat file
    with open(DEFAULT_CATEGORY_FILE, 'w') as default_cat_file:
        default_cat_file.write(category)

def create_category(category):
    # Check that the category exists. If it does then exit
    if check_category_exists(category):
        print("The category '{}' already exists. No need to create a new one".format(category))
        return
    
    # Write the text for the unfinished and finished sections of the categorys to the 
    # category_file_path
    with shelve.open(get_category_file_path(category)) as category_file:
        category_file['Unfinished'] = []
        category_file['Finished'] = []

    # If the default category file is empty then set this category as the default category for now
    if not get_default_category():
        set_default_category(category)

def get_tasks_for_section(category, section_name):
    if not check_category_exists(category):
        raise Exception("The category '{}' does not exist".format(category))

    with shelve.open(get_category_file_path(category)) as category_file:
        return category_file.get(section_name, [])

def add_tasks_to_category(category):
    help_text = "# Add tasks as bullet points using the markdown syntax ('-'). The tasks can\n" + \
                "# be multiline. You can also add multiple tasks at the same time using the\n" + \
                "# bullet point syntax. Any line starting with a '#' will be ignored. Any\n" + \
                "# lines between 2 lines starting with '-' are considered a part of the\n" + \
                "# the previous task.\n" + \
                "#\n" + \
                "# For example, the following would add 2 new tasks\n" + \
                "# - This is my first task\n" + \
                "#     - Some details about the first task\n" + \
                "# - This is the second task\n\n"

    user_input = _raw_input_editor(default=help_text)
    print(user_input)

    # After use is done, read the temp file
        # Parse the tasks out of the temp file
    # Append the tasks to unfinished section of the categorys

def set_task_as_done(category, task_id):
    # Get the category file path
    # Get tasks for all the sections
    # Find the appropriate task_id from the unfinished section
        # If not found then throw error
    # If an appropriate task is found then take it out of the unfinished section and put in into
    #   the finished section
    pass

def edit_category(category, raw=False):
    # Get the category file name
    # Get the tasks for the category
    # Create a temporary file
        # Generate the text to display in the file
        # Write the text to the file
    # Open the temp file in the default editor
    # After the user is done editing open the temp file again
        # For each section look at the task id, the done state (i.e. '[ ]' or '[X]') and the task
        #   text

    # TODO description not fully defined
    # Update the 

    pass

