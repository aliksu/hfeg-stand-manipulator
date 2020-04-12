from setuptools import setup, find_packages

setup(
    name='hsm',
    version='0.1',
    description='Scripts to emulate hfeg and stand manipulator',
    author='aliksu',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'hfeg-emul = src.hfeg_emulator.main:main',
        ]
    }
)
