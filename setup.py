import pathlib

from setuptools import setup
from thumb_gen_x  import __version__

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="thumb_gen_x",
    version=__version__,
    description="Python application that can be used to generate video thumbnail for mp4 and mkv file types.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tharindu.dev",
    author_email="tharindu.nm@yahoo.com",
    url="https://github.com/truethari/thumb-gen-x",
    keywords="thumbnails video screenshot",
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/truethari/thumb-gen-x/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    packages=['thumb_gen_x'],
    include_package_data=True,
    package_data = {'' : ['fonts/*.ttf', 'images/*.jpg, images/*.png']},
    install_requires=["Pillow", "infomedia", "opencv-python", "tk"],
    entry_points={
        "console_scripts": [
            "thumb-gen-x=thumb_gen_x.__main__:main",
        ]
    },
)
