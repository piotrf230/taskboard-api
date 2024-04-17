from setuptools import setup


def get_dependencies():
    with open("requirements.txt") as requirements:
        return requirements.read().splitlines()


setup(
    name="taskboard_app",
    version="1.0.0",
    packages=["taskboard_app", "taskboard_app.users", "taskboard_app.tasks"],
    url="",
    license="",
    author="piotrf230",
    author_email="",
    description="taskboard_app project",
    install_requires=get_dependencies(),
)
