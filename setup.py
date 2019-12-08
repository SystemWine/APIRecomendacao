from setuptools import setup

setup(
    name='systemwine_api',
    packages=['api'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful', 
        'flask-sqlalchemy',
        'mysqclient'
    ],
)

#https://codeburst.io/jwt-authorization-in-flask-c63c1acf4eeb
#https://flask.palletsprojects.com/en/1.1.x/patterns/packages/