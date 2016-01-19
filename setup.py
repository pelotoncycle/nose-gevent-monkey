from setuptools import find_packages, setup


setup_args = dict(
    name='nose-gevent-monkey',
    version='0.0.1',
    maintainer='Kevin Frommelt',
    maintainer_email='kevin.frommelt@gmail.com',
    description=(
        'A nose plugin for monkey patching modules for use with gevent.'
    ),
    url='https://github.com/kevinfrommelt/nose-gevent-monkey',
    py_modules=['nose_gevent_monkey'],
    install_requires=["nose"],
    entry_points={
        'nose.plugins.0.10': [
            'nose-gevent-monkey=nose_gevent_monkey:GeventMonkey',
        ]
    },
)


if __name__ == '__main__':
    setup(**setup_args)
