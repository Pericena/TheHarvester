# -*- coding: utf-8 -*-
#powerhell python setup.py py2exe

import sys
from distutils.core import setup

kwargs = {}
if 'py2exe' in sys.argv:
    import py2exe
    kwargs = {
        'console' : [{
            'script'         : 'theHarvester.py',
            'description'    : 'Descripcion del programa.',
           'icon_resources' : [(0, 'icon.ico')]
            }],
        'zipfile' : None,
        'options' : { 'py2exe' : {
            'dll_excludes'   : ['w9xpopen.exe'],
            'bundle_files'   : 1,
            'compressed'     : True,
            'optimize'       : 2
            }},
         }

setup(
    name='theHarvester',
    author='Luishiño Pericena Choque',
    author_email='pericena12@gmail.com',
    **kwargs)