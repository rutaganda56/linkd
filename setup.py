from setuptools import setup, find_packages

setup(
    name="linkd",
    version="1.0.1",
    author="Rutaganda Jean Valentin",
    py_modules=["main", "github_api", "reddit_api", "utils"], 
    packages=find_packages(),
    install_requires=[
        "rich",
        "requests"
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "linkd=linkd.main:main"
        ]
    },
)
