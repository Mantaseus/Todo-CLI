"""
Usage:
    todo
        [ -n=<val> | --num-of-tasks=<val> ]
    todo <category_name>
        [ -a | --all-unfinished-tasks ]
        [ -t=<val> | --num-of-tasks=<val> ]
    todo add
    todo add <category_name>
    todo done <task_id>
    todo done <category_name> <task_id>
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
    -r, --raw
        Edit the raw todo logs
    -l, --list-all
        List all categories resistered with the todo CLI
    -t=<val>, --num-of-tasks=<val>
        The number of the highest priority tickets to print out [default: 3]
    -d=<val>, --set-default=<val>
        Set the provided <val> as the default category for all the
        relevant commands
    -n=<val>, --create-new-cat=<val>
        Create a new category to group todo tasks in
"""

from __future__ import print_function
from __future__ import absolute_import
from pprint import pprint

from docopt import docopt

import category_manager

# HELPERS -----------------------------------------------------------------------------------------

def print_tasks(tasks):
    print(tasks)

# ARGS HANDLERS -----------------------------------------------------------------------------------

def handle_default():
    category_name = args['<category_name>']
    if not category_name:
        category_name = category_manager.get_default_category()

    unfinished_tasks = category_manager.get_tasks_for_section(category_name, 'Unfinished')

    # Do the formatting for the printout
    if args['--all-unfinished-tasks']:
        print_tasks(unfinished_tasks)
    else:
        print_tasks(unfinished_tasks[:int(args['--num-of-tasks'])])

def handle_add():
    pass

def handle_done():
    pass

def handle_edit():
    pass

def handle_cats():
    pass

# MAIN --------------------------------------------------------------------------------------------

def run_main():
    global args
    args = docopt(__doc__)

    pprint(args)

    if args['add']:
        handle_add()
        exit()

    if args['done']:
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
