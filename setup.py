from setuptools import setup, find_packages

setup(
  name="network_scanner",
  version="0.1",
  packages=find_packages(),
  install_requires=[
    "scapy",
    "python-nmap",
    "netifaces"
  ],
  entry_points={
    'console_scripts': [
      'network_scanner=network_scanner.cli:main',
    ],
  },
)