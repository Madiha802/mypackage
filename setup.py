from setuptools import setup, find_packages

setup(
    name="mon_package",  
    version="0.1.0",  
    description="Un exemple de package Python",  
    long_description=open("README.md", encoding="utf-8").read(),  
    long_description_content_type="text/markdown",  
    author="madiha",
    author_email="madihaelkasri71@gmail.com",
    url="https://github.com/Madiha802/mypackage.git",  
    packages=find_packages(),  
    classifiers=[  
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6", 
    install_requires=[  
        
    ],
    extras_require={  
        "dev": ["pytest", "flake8"],
    },
)
