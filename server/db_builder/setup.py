from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('dbbuilder.py', base=base)
]

setup(name='LMST-dbbuilder',
      version = '1.0',
      description = 'Database builder for LMST',
      options = dict(build_exe = buildOptions),
      executables = executables)
