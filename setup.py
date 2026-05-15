from setuptools import setup, find_packages

setup(
    name="linkd",
    version="1.0.1",
    py_modules=["main", "github_api", "reddit_api", "utils"], 
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "linkd=main:main"
        ]
    },
)
