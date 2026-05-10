from setuptools import find_packages, setup

package_name = 'tele_op'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hestia',
    maintainer_email='sammet.jan@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'tele_op_node = tele_op.tele_op:main',
            'wasd_command_sender = tele_op.wasd_command_sender:main',
        ],
    },
)
