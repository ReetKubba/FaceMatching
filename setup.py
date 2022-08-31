from setuptools import setuptools 
from setuptools import setup
setup(
    num="src",
    version="0.0.1",
    author="Reet Kubba",
    description="A small package for to whom does your face match",
    author_email="rkubba_be20@thapar.edu",
    packages="src",
    python_requires=">3.7",
    install_requires=[
            'mtcnn==0.1.1',
            'tensorflow==2.9.1',
            'keras==2.9.0',
            'keras-vggface==0.6',
            'keras_applications==1.0.8',
            'PyYAML',
            'tqdm',
            'scikit-learn',
            'streamlit',
            'bing-image-downloader'
    ]
)