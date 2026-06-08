#!/usr/bin/env python
import os
import sys


def main():
    sys.path.insert(0, os.path.abspath('src'))
    from IPython import start_ipython  # noqa: PLC0415
    start_ipython(argv=[])


if __name__ == '__main__':
    sys.exit(main())
