from setuptools import setup, find_packages

setup(
    name="gemini-content-generator",
    version="0.1.0",
    description="Generate content using Vertex AI Gemini model.",
    author="[Your Name]",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "Pillow>=9.0.0",
        "vertexai",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "gemini-generator=main:main",
        ],
    },
)
