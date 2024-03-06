from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
    name="xmlriver",
    version="0.11",
    author="Ivan Sharkov",
    author_email="admin@kurshub.ru",
    description="Пакет для работы с поисковой выдачей Google и Yandex по API через сервис XMLRiver / Package for working with Google and Yandex search results via API via XMLRiver service.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/KursHub-ru/xmlriver",
    packages=find_packages(),
    install_requires=[
      'requests >= 2.25',
       'xmltodict >= 0.12'
    ],
    keywords='google, yandex, xmlriver, xmlriver.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    project_urls={
    'Documentation': 'https://github.com/KursHub-ru/xmlriver',
    'GitHub': 'https://github.com/KursHub-ru/xmlriver',
    'Homepage': 'https://0pl.ru',
    'Organization': 'https://kurshub.ru',
    'Telegram': "https://t.me/sharkovseo",
  },
)