#!/opt/python3/bin/python3

import argparse
import socket
import struct
import sys

#we'll want to change these to output choices
flags = argparse.ArgumentParser(description="It's a cunt about syntax.")
flags.add_argument('data', nargs = '+', help='What you want to decode.')
flags.add_argument('-b', '--binary', help='Converts the input to binary.  Currently only takes decimal input.', action='store_true')
flags.add_argument('-d', '--decimal', help='Input is decimal or dotted decimal.', action='store_true')
flags.add_argument('-i', '--ip', help='Specifically for converting IP addresses - currently requires ":" between each 8 (2x4) bit pair.', action='store_true')
flags.add_argument('-l', '--longip', help='Convert dotted decimal IP to iplong.  CIDR notation is allowed.', action='store_true')
flags.add_argument('-x', '--hex', help='Input is hex, (see -i for IP address conversion)', action='store_true')
flags.add_argument('-V', '--Version', help='Displays the version and then exits', action='version', version='kXconvert 0.5: suberbeta snek tool')

# Let's start with some basic conversion functions - that loop shit is sloppy.

# Maybe we take input and break it down - that 0x and/or : thing is still not quite right, but fuck it for now.
def ipbreak(input):
	if "." in str(input):
		octet = input.split(".")
		return octet
	else:
		return input

def hexbreak(input):
	if ":" in str(input):
		byte = input.split(":")
		return byte
	elif "0x" in str(input):
		byte = [input[i:i+2] for i in range (0, len(input), 2)][1:]
		return byte
	else:
		return input

def cleanout(output):
	cleaned = (ipbreak(hexbreak(output)))
	return cleaned

# Now for the converters
def tohex(stuff):
	hexd = []
	for member in stuff:
		x = str(hex(int(member)))
		#if len(x) < 2:
		#	hexd.append("0")
		#	hexd.append(x[2:])
		#else:
		hexd.append(x[2:])
	return hexd

#begin testing vardumpything
flag = flags.parse_args()
ourvar = ''.join(flag.data)

fun = cleanout(ourvar)
print (fun)
# end testing vardumpything

if flag.hex:
	hexd = tohex(fun)
	print (hexd)
	print(' '.join(hexd))