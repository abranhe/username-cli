import setuptools
import sys

with open("README.md", "r") as readme:
    long_description = readme.read()

if sys.version_info < (3, 0, 0):
        sys.stderr.write('Python 3.0 or later required')
        exit(1)

setuptools.setup(
    name = "username_cli",
    packages = ["username_cli"],
		entry_points = {
        "console_scripts": [
					'username = username_cli.username_cli:user'
				]
    },
    long_description = long_description,
    long_description_content_type = "text/markdown",
    version = "0.0.4",
    description = "Get the current user name",
    author = "Carlos Abraham",
    author_email = "abraham@abranhe.com",
    url = "https://projects.abranhe.com/username-cli",
    classifiers=(
        'Programming Language :: Python',
        'Natural Language :: English',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
		    'Programming Language :: Python :: 3',
				'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
    project_urls={
        'Source': 'https://github.com/abranhe/username-cli',
    },
		install_requires=[
        'username',
    ],
)
