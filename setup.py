from setuptools import setup

setup(
    name="ai-security-scanner",
    version="1.0.0",
    py_modules=["ai_scanner_pro"],
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "aicheck=ai_scanner_pro:main",
        ],
    },
)
