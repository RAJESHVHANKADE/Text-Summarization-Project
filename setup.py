import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()


__version__ = "1.0.0"

REPO_NAME = "Text-Summarization-Project"
AUTHOR_USER_NAME = "RAJESHVHANKADE"
SRC_REPO ="textSummarizer"
AUTHOR_EMAIL = "vhankadenrajesh@gmail.com"


setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
        },
    package_dir= {"":"src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"

)