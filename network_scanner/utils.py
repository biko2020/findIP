import netifaces


def get_interface_details(interface):
  addrs = netifaces.ifaddresses(interface)
  ip_info = addrs[netifaces.AF_INET][0]
  return {
    'ip': ip_info['addr'],
    'netmask': ip_info['netmask'],
    'broadcast': ip_info.get('broadcast', '')
  }