# /home/ubuntu/my_django_project/src/manage.py
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_django_project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Could not import Django. Are you sure it's installed and available on your PYTHONPATH?"
        )
    execute_from_command_line(sys.argv)

