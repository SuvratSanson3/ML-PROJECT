from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]

    return requirements


setup(
name = "ML_Project",
version = "0.0.1",
author = "Suvrat Sanson",
author_email = "suvratsharma.333@gmail.com",
packages = find_packages(),
# package_dir={"": "src"},
install_requires = get_requirements('requirements.txt'),
)