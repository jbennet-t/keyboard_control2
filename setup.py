import os
from glob import glob
from setuptools import setup

package_name = 'keyboard_control2'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jordan',
    maintainer_email='sinowaj1@tcnj.edu',
    description='basic teleop/control for ros2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'keyboard_input2 = keyboard_control2.keyboard_input2:main',
        ],
    },
)
