import argparse
import json
import sys

def locate_device(lat, lon, radius=10):
 
 
  return results

def main():
  parser = argparse.ArgumentParser(description='Locate devices by geographic coordonnates')
  
  parser.add_argument('--lat', type=float, required=True, help='Latitide')
  parser.add_argument('--lon', type=float, required=True, help='Longitude')
  parser.add_argument('--radius', type=int, default=10, help='Search radius in km')

  args = parser.parse_args()
  results = locate_device(args.lat, args.lon, args.radius)
  print(json.dumps(results))

if __name__ == '__main__':
  main()
