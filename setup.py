from setuptools import setup, find_packages


def load_requirements(filename='requirements.txt'):
    try:
        with open(filename) as f:
            lines = f.readlines()
        return lines
    except Exception:
        return []


setup(
    name='app',
    version="0.0.1",
    description='',
    url='',
    author='MPIB - Human and Machines',
    author_email='',
    license='',
    packages=[package for package in find_packages()
              if package.startswith('app')],
    zip_safe=False,
    install_requires=load_requirements(),
    extras_require={'dev': load_requirements('dev_requirements.txt')},
    scripts=[
    ]
)
