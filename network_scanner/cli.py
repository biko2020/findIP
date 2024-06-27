import argparse
from network_scanner.arp_scanner import arp_scan
from network_scanner.nmap_scanner import nmap_scan
from network_scanner.utils import get_interface_details

def main():
  parser = argparse.ArgumentParser(description="** Find Network Host IP *** ")
  parser.add_argument('--interface', type=str, required=True, help="Network interface to scan")
  parser.add_argument('--method', type=str, choices=['arp', 'nmap'], default='arp', help='Scanning method: arp or namp')
  args = parser.parse_args()

  interface_details = get_interface_details(args.interface)
  ip_range = f"{interface_details['ip']}/{interface_details['netmask']}"

  if args.method == 'arp':
    devices = arp_scan(ip_range)
  else:
    devices = nmap_scan(ip_range)

  for device in devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}" + (f", Status: {device.get('status', '')}" if 'status' in device else ''))

if __name__ == "__main__":
  main()