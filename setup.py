import setuptools

with open('README.md','r',encoding='utf-8') as f:
    long_description=f.read()

__version__="0.0.0"
REPO_NAME="NLP_Text_Summarization"
SRC_REPO="NLP_PROJECT"
AUTHOR_USER_NAME="girish12ns"
AUTHOR_EMAIL:"girish12n@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    long_description=long_description,
    author=AUTHOR_USER_NAME,
    url=f"https://github.com/{AUTHOR_USER_NAME}{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}{REPO_NAME}/issues"

    },
    package_dir= {"" :"src"},
    packages=setuptools.find_packages(where="src")
)