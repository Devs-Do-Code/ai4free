from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    README = f.read()

setup(
    name="ai4free",
    version="0.5", 
    description="collection of free AI provides",
    long_description=README,
    long_description_content_type="text/markdown",
    author="OEvortex, Sree",  # List both authors here
    author_email="helpingai5@gmail.com",  # Specify the email for the first author
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        "tls_client",
        "webscout",
    ],
    license='HelpingAI Simplified Universal License',
    project_urls={
        'Source': 'https://github.com/Devs-Do-Code/ai4free',
        'Tracker': 'https://github.com/Devs-Do-Code/ai4free/issues',
        'YouTube': 'https://youtube.com/@OEvortex',
        'Youtube': 'https://www.youtube.com/@DevsDoCode'
    },
)