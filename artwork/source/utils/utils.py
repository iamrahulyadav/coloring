"""
Useful routines
"""

import os
import shutil
import utils.path as path


def copy(src, dst):
    """
    Calls shutil.copy2 with printing a message
    """
    print('copy {} to {}'.format(os.path.relpath(src, path.root), os.path.relpath(dst, path.root)))
    shutil.copy2(src, dst)


def read_text(file):
    """
    Reads a whole text file (UTF-8 encoded).
    """
    with open(file, mode='r', encoding='utf-8') as f:
        text = f.read()
    return text
