import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="Redbubble-Price-Calculator-Redbubble-Applicant",
    version="0.0.1",
    author="Redbubble Applicant",
    author_email="me@example.com",
    description="Redbubble CLI Price Calculator Coding Test Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/namanj123in/rb-price-calculator",
    packages=setuptools.find_packages(),
    python_requires='>=3.2.5',
)