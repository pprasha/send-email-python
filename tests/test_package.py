import pytest
import os
os.system("python setup.py sdist bdist_wheel")
os.system("pip install .")
os.system("pip install -e .")
import send_email
def test_setup():
    assert send_email.setup() == "Done"

