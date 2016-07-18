#!/usr/bin/python3

import sys
f = open(sys.argv[1], 'r')

def main():
  print(f.read()) 

if __name__ == '__main__':
  main()