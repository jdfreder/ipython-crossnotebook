# -*- coding: utf-8 -*-

try:
    from setuptools import setup
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup
    from distutils.core.command.install import install

class InstallCommand(install):
    """Install as noteboook extension"""
    develop = False

    def install_extension(self):
        from os.path import dirname, abspath, join
        from IPython.html.nbextensions import install_nbextension
        from IPython.html.services.config import ConfigManager

        print("Installing nbextension ...")
        crossnotebook = join(dirname(abspath(__file__)), 'crossnotebook', 'js')
        install_nbextension(crossnotebook, destination='crossnotebook', symlink=self.develop, user=True)

        print("Enabling the extension ...")
        cm = ConfigManager()
        cm.update('notebook', {"load_extensions": {"crossnotebook/init": True}})

    def run(self):
        print "Installing Python module..."
        install.run(self)

        # Install Notebook extension
        self.install_extension()

class DevelopCommand(InstallCommand):
    """Install as noteboook extension"""
    develop = True

from glob import glob 
setup(
    name='crossnotebook',
    version='0.1',
    description='Plugin that enables multicell selection and copying and pasting cells between notebooks.',
    author='Jonathan Frederic',
    author_email='jon.freder@gmail.com',
    license='New BSD License',
    url='https://github.com/jdfreder/ipython-crossnotebook',
    keywords='data visualization interactive interaction python ipython widgets widget',
    classifiers=['Development Status :: 4 - Beta',
                 'Programming Language :: Python',
                 'License :: OSI Approved :: MIT License'],
    cmdclass={
        'install': InstallCommand,
        'develop': DevelopCommand,
    }
)