from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()



setup(name='send-email-python',
      version='0.0.1',
      description='A package to simply send an email.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/pjaycorp/send-email-python',
      author='Puranjay Prashanth',
      author_email='puranjayprashanth@gmail.com',
      license='GNU',
      packages=['send_email'],
      zip_safe=False)