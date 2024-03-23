import os
from glob import glob
from setuptools import setup

package_name = 'px4_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name), glob('resource/*rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='victor',
    maintainer_email='vigaravictor99@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'offboard_control = px4_control.offboard_control:main',
            'visualizer = px4_control.visualizer:main', 
            'simulation = px4_control.simulation:main'
        ],
    },
)
