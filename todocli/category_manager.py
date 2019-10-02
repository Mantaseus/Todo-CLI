from __future__ import print_function
from pprint import pprint
from datetime import datetime
import os
import shelve
import tempfile
import subprocess
import re

# CONSTANTS ---------------------------------------------------------------------------------------

CATEGORY_FILE_DIR = os.path.expanduser('~/.todocli/cats')
DEFAULT_CATEGORY_FILE = os.path.expanduser('~/.todocli/default_cat')

DEFAULT_TEXT_WIDTH = 70

ADD_HELP_TEXT = """

# Adding tasks to category '{category_name}'
# 
# Rules:
# - Add tasks as bullet points using the markdown syntax ('-'). 
# - The tasks can be multiline. 
# - You can add multiple tasks at the same time using the bullet point syntax. 
# - Any line starting with a '#' will be ignored. 
# - Any lines between 2 lines starting with '-' are considered a part of the
#   the previous task.
# - Try to keep the line character width less than 70 to make the tasks look
#   nicer when printed
#
# For example, the following would add 2 new tasks
# - This is my first task
#     - Some details about the first task
# - This is the second task
"""

EDIT_HELP_TEXT = """
# Editing tasks for category '{category_name}'
# 
# Rules:
# - The numbers in front of the task descriptions are the task IDs. Do not
#   mess with them or it could lead to erratic behavior
# - You can move the tasks up or down to "prioritize" them relative to each other
# - You can move a task from one section to another and that task will
#   actually get moved over to that section. For example: If you move a task
#   from the "Unfinished" section to the "Finished" section then that task
#   will not appear in the list of unfinished tasks when you run `todo`
# - If you delete a task from this list then it will be deleted permanently
#   and will not be recoverable
"""

# PRIVATE: TEMP FILE MANAGEMENT -------------------------------------------------------------------
# Copied from https://stackoverflow.com/a/48466593 with some modifications

def _raw_input_editor(default=None, editor=None):
    with tempfile.NamedTemporaryFile(mode='r+') as tmpfile:
        # Write the default text to the temp file
        if default:
            tmpfile.write(default)
            tmpfile.flush()

        # Get the available editor
        editor = editor or _get_editor()

        # Build the command to open the file in the editor
        command = [editor, tmpfile.name]
        if editor in ['vi', 'vim']:
            # Setup vi editor to enforce auto wrapping after 80 lines
            command.append('-c')
            command.append('set textwidth={}'.format(DEFAULT_TEXT_WIDTH))
            command.append('-c')
            command.append('set ft=markdown')
            command.append('-c')
            command.append('set smartindent')

        # Run the command
        try:
            subprocess.check_call(command)
        except Exception as e:
            # Some error happened. Do nothing
            print(e)
            print('Add operation canceled')
            return ''

        # Get the output from the temp file
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
            return default_cat_file.read()
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
        category_file['unfinished'] = []
        category_file['finished'] = []
        category_file['archived'] = []
        category_file['next_task_id'] = 0

    # If the default category file is empty then set this category as the default category for now
    if not get_default_category():
        set_default_category(category)

def get_tasks_for_section(category, section_name):
    if not check_category_exists(category):
        raise Exception("The category '{}' does not exist".format(category))

    with shelve.open(get_category_file_path(category)) as category_file:
        return category_file.get(section_name, [])

def add_tasks_to_category(category):
    user_input = _raw_input_editor(ADD_HELP_TEXT.format(category_name=category))

    # Parse the tasks out of the temp file
    raw_tasks = []
    user_lines = user_input.split('\n')
    for line in user_lines:
        # Ignore lines with '#'
        if line.startswith('#'):
            continue
        
        # If a valid markdown bullet point is found in the text then create a new empty entry
        # in the raw_tasks list
        if line.startswith('-'):
            raw_tasks.append('')

            # Remove the bullet point from the line
            line = re.sub(r'^- *', '', line) 

        # If there is no entry in the raw_tasks list yet then skip
        # This will make sure that any text before the first bullet point will be ignored
        if not raw_tasks:
            continue

        # Append any line
        raw_tasks[-1] += line + '\n'

    # Append the tasks to unfinished section of the categories
    with shelve.open(get_category_file_path(category)) as category_file:
        unfinished_tasks = category_file['unfinished']
        for task in raw_tasks:
            unfinished_tasks.append({
                'id': category_file['next_task_id'],
                'created': datetime.now(),
                'edited': datetime.now(),
                'description': task
            })
            category_file['next_task_id'] += 1
        category_file['unfinished'] = unfinished_tasks

def move_task(category, task_id, from_section, to_section):
    with shelve.open(get_category_file_path(category)) as category_file:
        from_tasks = category_file[from_section]
        to_tasks = category_file[to_section]

        try:
            task_index = next(
                i
                for i, task in enumerate(from_tasks)
                if task['id'] == task_id
            )
        except StopIteration:
            print("Task ID '{}' not found in section '{}' of category '{}'".format(
                task_id, 
                from_section,
                category
            ))
            return

        task_to_move = from_tasks.pop(task_index)
        to_tasks.append(task_to_move)

        category_file[from_section] = from_tasks
        category_file[to_section] = to_tasks

def edit_category(category, raw=False):
    old_tasks_text = '# You can move '

    with shelve.open(get_category_file_path(category)) as category_file:
        for category in ['unfinished', 'finished', 'archived']:
            current_tasks_text += '# {}\n\n'.format(category.capitalize())

            for task in category_file[category]:
                old_tasks_text += '{}. {}'.format(
                    task['id'], 
                    task['description']
                )
    
    new_tasks_text = _raw_input_editor(current_tasks_text)
    print(new_tasks_text)

