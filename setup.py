from setuptools import setup, find_packages
import os

version = open(os.path.join("cellml", "theme", "version.txt")).read()

setup(name='cellml.theme',
      version=version,
      description="CellML Theme",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme',
      author='CellML Web Working Group',
      author_email='team@cellml.org',
      url='http://www.cellml.org/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cellml'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'z3c.form',
          'plone.app.z3cform>=0.4',
          'plone.z3cform>=0.5',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
