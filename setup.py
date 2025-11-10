"""
Setup script for ByteChan cryptocurrency
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bytechan",
    version="0.1.0",
    author="ByteChan Development Team",
    author_email="dev@bytechan.org",
    description="Privacy-first cryptocurrency with advanced cryptographic features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/bytechan",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "cryptography>=41.0.0",
        "pycryptodome>=3.18.0",
        "ecdsa>=0.18.0",
        "base58>=2.1.1",
        "aiohttp>=3.8.0",
        "pytest>=7.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "bytechan=bytechan.cli:main",
        ],
    },
)
