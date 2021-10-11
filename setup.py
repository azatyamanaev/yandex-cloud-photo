from setuptools import setup, find_packages
from io import open
from os import path

import pathlib
# Директория, в которой содержится этот файл
HERE = pathlib.Path(__file__).parent

# Текст README-файла
README = (HERE / "README.md").read_text()

# Автоматически собирает в requirements.txt все модули для install_requires, а также настраивает ссылки на зависимости
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]
                    
setup (
 name = 'cloudphoto',
 description = 'A simple commandline app for interacting with bucket in yandex cloud',
 version = '1.0.0',
 packages = find_packages(), # list of all packages
 include_package_data=True,
 install_requires = install_requires,
 python_requires='>=3.6', # any python greater than 3.6
 entry_points='''
        [console_scripts]
        cloudphoto=cloudphoto.__main__:main
    ''',
 author="Azat Yamanaev",
 long_description=README,
 long_description_content_type="text/markdown",
 url='https://github.com/azatyamanaev/yandex-cloud-photo',
  dependency_links=dependency_links,
  author_email='iamanaev2001@gmail.com'
)
