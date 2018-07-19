#!/usr/bin/env python3

from setuptools import setup

setup(
    name='download_youtube',
    version='1.0.0',
    description='Download a list of videos from youtube',
    long_description="""
    Download a list of videos from youtube. (Powered by PyTube [https://github.com/nficano/pytube])
    """,
    author='Alireza Davoudi',
    author_email='davoudialireza@gmail.com',
    url = 'https://github.com/adavoudi/download_youtube',
    license='MIT License',
    packages=['download_youtube'],
    entry_points={
        'console_scripts': [
            'youtubevideosdownload = youtube_videos_download.youtube_videos_download:main',
        ],
    },    
    install_requires=[
        'pytube',
        'tqdm'
    ],
    zip_safe=False
)
