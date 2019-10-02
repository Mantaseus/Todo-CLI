"""
Usage:
    todo
        [ -a | --all-unfinished-tasks ]
        [ -t=<val> | --num-of-tasks-to-list=<val> ]
    todo 
        [ -a | --all-unfinished-tasks ]
        [ -c=<val> | --category-name=<val> ]
        [ -t=<val> | --num-of-tasks-to-list=<val> ]
    todo add
    todo add <category_name>
    todo done <task_id>
    todo done <category_name> <task_id>
    todo delete <task_id>
    todo delete <category_name> <task_id>
    todo edit
    todo edit <category_name>
    todo cats
    todo cats default <category_name>
    todo cats new <category_name>

Options:
    -a, --all-unfinished-tasks
        List out archived tasks
    -c=<val>, --category-name=<val>
        The name of the category to list tasks for
    -t=<val>, --num-of-tasks-to-list=<val>
        The number of the highest priority tickets to print out [default: 3]
"""

from __future__ import print_function
from __future__ import absolute_import
from pprint import pprint
import textwrap

from docopt import docopt
from tabulate import tabulate

from . import category_manager

# HELPERS -----------------------------------------------------------------------------------------

def wrap_text(text, width=category_manager.DEFAULT_TEXT_WIDTH):
    return '\n'.join([
        textwrap.fill(line, width=width)
        for line in text.split('\n')
    ])

def print_tasks(category, section_name, limit=0):
    try:
        tasks = category_manager.get_tasks_for_section(category, section_name)
    except Exception as e:
        print(e)
        return

    # If limit is not defined then show all tasks
    if not limit:
        limit = len(tasks)

    print("\n Showing {}/{} {} tasks for '{}'".format(
        limit,
        len(tasks),
        section_name,
        category
    ))

    # Generate the data to print
    data_to_print = []
    for task in tasks[:limit]:
        description = wrap_text(task.get('description', ''))
        data_to_print.append([task.get('id'), description])

    print(tabulate(
        data_to_print,
        ['ID', 'Description'],
        tablefmt='fancy_grid'
    ) + '\n')

def print_categories(categories):
    print(categories)

# ARGS HANDLERS -----------------------------------------------------------------------------------

def handle_default():
    category_name = args['--category-name']
    if not category_name:
        category_name = category_manager.get_default_category()

    # Do the formatting for the printout
    tasks_limit = 0
    if args['--all-unfinished-tasks']:
        tasks_limit = int(args['--num-of-tasks-to-list'])
    
    print_tasks(category_name, 'unfinished', tasks_limit)
    print_tasks(category_name, 'finished', tasks_limit)
    print_tasks(category_name, 'archived', tasks_limit)

def handle_add():
    category_name = args['<category_name>']
    if not category_name:
        category_name = category_manager.get_default_category()

    category_manager.add_tasks_to_category(category_name)

def handle_done():
    category_name = args['<category_name>']
    if not category_name:
        category_name = category_manager.get_default_category()

    task_id = int(args['<task_id>'])
    category_manager.move_task(category_name, task_id, 'unfinished', 'finished')

def handle_delete():
    category_name = args['<category_name>']
    if not category_name:
        category_name = category_manager.get_default_category()

    task_id = int(args['<task_id>'])
    category_manager.move_task(category_name, task_id, 'unfinished', 'archived')

def handle_edit():
    category_name = args['<category_name>']
    if not category_name:
        category_name = category_manager.get_default_category()

    category_manager.edit_category(category_name)

def handle_cats():
    if args['new']:
        category_manager.create_category(args['<category_name>'])
        return

    if args['default']:
        category_manager.set_default_category(args['<category_name>'])
        return

    # The default behavior is to just print out all the categories
    print_categories(category_manager.get_categories())

# MAIN --------------------------------------------------------------------------------------------

def run_main():
    global args
    args = docopt(__doc__)

    # Create the storage directories for the tasks files if they don't already exist
    category_manager.setup_storage_dir()

    if args['add']:
        handle_add()
        exit()

    if args['done']:
        handle_done()
        exit()

    if args['delete']:
        handle_delete()
        exit()

    if args['edit']:
        handle_edit()
        exit()

    if args['cats']:
        handle_cats()
        exit()

    # Default case
    handle_default()

if __name__ == '__main__':
    run_main()

