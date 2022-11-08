from setuptools import find_packages, setup

setup(
    name="cereal_project",
    packages=find_packages(exclude=["cereal_project_tests"]),
    install_requires=[
        "dagster",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
