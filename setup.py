from importlib.metadata import entry_points

from setuptools import find_packages, setup

setup(
    name='curl-to-payload',
    version='0.0.1',
    description='Convert a curl post command to a payload dictionary.',
    package_dir={'': '.'},
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'curl-to-payload = curl_to_payload.curl_to_payload:main',
        ],
    },
    author='SpaceShaman',
    author_email='spaceshaman@tuta.io',
    url='https://github.com/SpaceShaman/curl_to_payload',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='curl payload',
    python_requires='>=3.6'
)
