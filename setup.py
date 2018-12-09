from setuptools import setup

setup(
    name='snapshot-anal-izer',
    version='0.1',
    author='Krzysztof Błaszczyński',
    author_email="krzysiek@nerity.com",
    description="Snapshot-anal-izer is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/avekiszka/snapshot-anal-izator",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:click
    ''',
)

