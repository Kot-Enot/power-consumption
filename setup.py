import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

build_exe_options = {
    'optimize': 2,
    'excludes': ['email', 'tkinter', 'html', 'http', 'xml']
}

setup(
    name='PowerConsumption',
    version='1',
    packages=[''],
    url='',
    license='',
    author='Виртенбергер В.А.',
    author_email='',
    description='Программа «Расход электроэнергии»',
    options={"build_exe": build_exe_options},
    executables=[Executable("power_consumption.py", base=base)]
)