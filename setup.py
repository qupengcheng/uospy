from setuptools import setup, find_packages
import os

setup(name='uospy',
      #version=os.getenv('BUILD_VERSION', 'DEV'),
      version='1.1.5',
      description='Python library for the uosio REST API',
      author='deck',
      author_email='deck@uosnewyork.io',
      url='https://github.com/uosnewyork/uospy',
      packages=find_packages(),
      test_suite = 'nose.collector',
      install_requires=[
          'requests',
          'base58',
          'ecdsa',
          'colander',
          'pytz',
          'six'
      ],
      entry_points = {
          'console_scripts' :[
              'validate_chain = uospy.command_line:validate_chain',
              'pycluos = uospy.command_line:cluos'
          ],
      }
)
