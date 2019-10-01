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
        [ -r | --raw ]
    todo edit <category_name>
        [ -r | --raw ]
    todo cats
        [ -l | --list-all ]
        [ -d=<val> | --set-default-cat=<val> ]
        [ -n=<val> | --create-new-cat=<val> ]

Options:
    -a, --all-unfinished-tasks
        Lists out all the unfinished tasks instead of just the top 3
    -l, --list-all
        List all categories resistered with the todo CLI
    -r, --raw 
        Edit the raw todo logs 
    -c=<val>, --category-name=<val>
        The name of the category to list tasks for
    -t=<val>, --num-of-tasks-to-list=<val>
        The number of the highest priority tickets to print out [default: 3]
    -d=<val>, --set-default-cat=<val>
        Set the provided <val> as the default category for all the
        relevant commands
    -n=<val>, --create-new-cat=<val>
        Create a new category to group todo tasks in
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

def print_tasks(category, tasks):
    print("\n {} unfinished tasks for '{}'".format(len(tasks), category))

    # Generate the data to print
    data_to_print = []
    for task in tasks:
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

    try:
        unfinished_tasks = category_manager.get_tasks_for_section(category_name, 'unfinished')
    except Exception as e:
        print(e)
        return

    # Do the formatting for the printout
    if args['--all-unfinished-tasks']:
        print_tasks(category_name, unfinished_tasks)
    else:
        print_tasks(category_name, unfinished_tasks[:int(args['--num-of-tasks-to-list'])])

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
    pass

def handle_cats():
    if args['--create-new-cat']:
        category_manager.create_category(args['--create-new-cat'])
        return

    if args['--set-default-cat']:
        category_manager.set_default_category(args['--set-default-cat'])
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
        handle_done()
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

