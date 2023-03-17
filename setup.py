from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    with open("requirements.txt") as obj:
        return obj.readlines().remove("-e.")


setup(name="finance_complaint",
      author="Suhasini",
      version="0.0.1",
      packages=find_packages(),
      install_requires=get_requirements())