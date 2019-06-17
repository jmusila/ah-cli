from setuptools import setup, find_packages

setup(
        name="a-haven",
        version="0.1",
        py_modules=find_packages(),
        include_package_data=True,
        install_requires=[
            "Click",
            "requests",
            "halo",
            ],
        entry_points="""
        [console_scripts]
        ah=app:cli
        """,
        )