from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    README = f.read()

setup(
    name="ai4free",
    version="0.1", 
    description="collection of free AI provides",
    long_description=README,
    long_description_content_type="text/markdown",
    author="OEvortex",
    author_email="helpingai5@gmail.com",
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
        'Documentation': 'https://github.com/OE-LUCIFER/Webscout/wiki',
        'Source': 'https://github.com/OE-LUCIFER/Webscout',
        'Tracker': 'https://github.com/OE-LUCIFER/Webscout/issues',
        'YouTube': 'https://youtube.com/@OEvortex',
    },
)