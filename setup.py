from setuptools import setup

REQUIRES = [
    'allure-pytest',
    'curlify',
    'sqlalchemy',
    'structlog',
    'records'
]

setup(
    name='orm_client',
    version='0.0.1',
    packages=['orm_client'],
    url='https://github.com/Amarillia31/orm_client.git',
    license='MIT',
    author='elena',
    author_email='-',
    install_requires=REQUIRES,
    description='orm client'
)
