from setuptools import setup


def get_dependencies():
    with open("requirements.txt") as requirements:
        return requirements.read().splitlines()


setup(
    name="taskboard",
    version="1.0.0",
    packages=["api", "api.task", "api.user", "taskboard", "taskboard_app"],
    url="",
    license="",
    author="piotrf230",
    author_email="",
    description="taskboard project",
    install_requires=get_dependencies(),
)
