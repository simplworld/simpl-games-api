# pylint: disable=undefined-name

import os
HOME = os.environ['HOME']


c.InteractiveShell.deep_reload = True
c.TerminalIPythonApp.exec_files = [
    '{}/.pythonrc'.format(HOME),
]

c.TerminalInteractiveShell.editing_mode = 'vi'
c.TerminalInteractiveShell.display_completions = 'readlinelike'

