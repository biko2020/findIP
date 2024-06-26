import nmap

def nmap_scan(ip_range):
  nm = nmap.PortScanner()
  nm.scan(hosts=ip_range, arguments='-sn')
  devices = []
  for host in nm.all_hosts():
    if 'mac' in nm[host]['addresses']:
      devices.append({
        'ip': nm[host]['addresses']['ipv4'],
        'mac': nm[host]['addresses']['mac'],
        'status' :nm[host]['addresse']['state']
      })
  return devices