"""
Usage:
    todo
    todo <category_name>
        [ -a | --all-unfinished-tasks ]
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
    -d=<val>, --set-default=<val>
        Set the provided <val> as the default category for all the
        relevant commands
    -n=<val>, --create-new-cat=<val>
        Create a new category to group todo tasks in
"""

from __future__ import print_function
from pprint import pprint

from docopt import docopt

# MAIN --------------------------------------------------------------------------------------------

def run_main():
    global args
    args = docopt(__doc__)

    pprint(args)

if __name__ == '__main__':
    run_main()
