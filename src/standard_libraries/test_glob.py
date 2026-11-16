
"""File Wildcards.

@see: https://docs.python.org/3/tutorial/stdlib.html#file-wildcards

The glob module provides a function for making file lists from directory wildcard searches:
"""

import glob
from pathlib import Path


def test_glob():
    """File Wildcards."""

    # Normalize paths so the test works on Windows, Linux, and macOS.
    actual_files = sorted(
        Path(path).as_posix()
        for path in glob.glob('src/standard_libraries/glob_files/*.txt')
    )

    expected_files = sorted([
        'src/standard_libraries/glob_files/first_file.txt',
        'src/standard_libraries/glob_files/second_file.txt'
    ])

    assert actual_files == expected_files
