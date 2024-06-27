import unittest
from network_scanner.nmap_scanner import nmap_scan

class TestNmapScanner(unittest.TestCase):
  def test_nmap_scan(self):
    devices = nmap_scan('ip_range')
    self.assertIsInstance(devices, list)

if __name__ == '__main__':
  unittest.main()