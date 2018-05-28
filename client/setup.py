from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('lmst.py', base=base)
]

setup(name='LMST',
      version = '1.0',
      description = 'The client component of the LMST streaming app',
      options = dict(build_exe = buildOptions),
      executables = executables)
