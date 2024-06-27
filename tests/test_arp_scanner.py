import unittest
from network_scanner.arp_scanner import arp_scan

class TestArpScanner(unittest.TestCase):
  def test_arp_scan(self):
    devices = arp_scan('ip_range')
    self.assertIsInstance(devices, list)

if __name__ == '__main__':
  unittest.main()