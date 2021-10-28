from distutils.core import setup, Extension


sfc_module = Extension('pypode', sources=['pypode_module.cpp'])

setup(name='pypode', version='0.1',
      description='Pyhton partial and ordinary differential equation solver',
      ext_modules=[sfc_module]
      )
