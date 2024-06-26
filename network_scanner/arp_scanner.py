from scapy.all import ARP, Ether, srp

def arp_scan(ip_range):
  arp = ARP(pdst=ip_range)
  ether = Ether(dst="ff:ff:ff:ff:ff:ff")
  packet = ether/arp
  result = srp(packet, timeout=3, verbose=0)[0]
  devices = []
  for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})
  return devices