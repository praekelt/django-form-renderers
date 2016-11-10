#!/usr/bin/env python

# manage.py needs to be here and not in tests. In the tests directory we create
# a form_renderers Python module and that seems to confuse manage.py into
# thinking that the actual app is within tests.

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
