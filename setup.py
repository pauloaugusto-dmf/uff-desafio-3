from setuptools import setup, find_packages

setup(
    name="calculadora_cr",
    version="0.1.0",
    description="Sistema para calcular o cr e media de cr por turma",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pandas", "pytest"],
)