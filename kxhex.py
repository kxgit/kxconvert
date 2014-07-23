#!/opt/python3/bin/python3

import argparse
import socket
import struct
import sys

flags = argparse.ArgumentParser(description='I got sick of trying to Google for converters.')
flags.add_argument('data', nargs = '+', help='What you want to decode.')
flags.add_argument('-b', '--binary', help='Converts the input to binary.  Currently only takes decimal input.', action='store_true')
flags.add_argument('-d', '--decimal', help='Input is decimal or dotted decimal.', action='store_true')
flags.add_argument('-i', '--ip', help='Specifically for converting IP addresses - currently requires ":" between each 8 (2x4) bit pair.', action='store_true')
flags.add_argument('-l', '--longip', help='Convert dotted decimal IP to iplong.  CIDR notation is allowed.', action='store_true')
flags.add_argument('-x', '--hex', help='Input is hex, (see -i for IP address conversion)', action='store_true')
flags.add_argument('-V', '--Version', help='Displays the version and then exits', action='version', version='kXconvert 0.5: suberbeta snek tool')

# maybe a decode to Ascii or something?
# Want to add an option to include binary - but make sure the number of bits accurately matches input
# I should add colors....
# hmm...maybe not sys.exit to allow for multiple conversions - :/ that can get messy though
# -q quiet or some sort of raw output
# add "-" for wandows and stuff

num = flags.parse_args()
print (''.join(num.data) + " converts to:")

if num.decimal:
	if "." in str(num.data):
		num = ''.join(num.data)
		fuckthis = num.split(".")
		for member in fuckthis:
			x = str(hex(int(member)))[2:]
			if len(x) <2:
				print ("0"+x, end=' ')
			else:
				print (x, end=' ')
		print ('')
		sys.exit()
	else:
		#see the swearing - want to make leading 0x optional, as well as always make it display a offset/leading zero for a 2 char pair.
		goddamnit = ''.join(num.data)
		hmm = (hex(int(goddamnit)))
		print (hmm)
		math = (" ".join(hmm[i:i+2] for i in range(0, len(hmm), 2)))
		print (math)
		sys.exit()

if num.ip:
	if ":" in str(num.data):
		num = ''.join(num.data)
		a = num.split(":")
		dot = 0
		for member in a:
			dot = dot+1
			x = int(member, 16)
			if dot < 4:
				print (str(x), end=".")
			else:
				print (str(x), end='')
		print ('')
		sys.exit()
	else:
		print ("Need the colon (:) for now or it won't work correctly.")
		sys.exit()
#	else:
# having trouble wrapping brain on this one :/ around
#		a = ' '.join(num.data)
#		print (int(a, 16))
#		sys.exit()

if num.hex:
	if ":" in str(num.data):
		num = ''.join(num.data)
		blah = num.split(":")
		yay = ''.join(blah)
		print (int(yay, 16))
		sys.exit()
	else:
		srsly = ''.join(num.data)
		print (int(srsly, 16))
		sys.exit()

# a last minute addition - want to make this as an 'also' option.
if num.binary:
	num = ''.join(num.data)
	omgwtf = bin(int(num))
	#debgish output - wtf is that returning that is ruining my day? Why.the.fuk can't I one line it like an adult?
	print (omgwtf)
	#nvm the above - but remember that was a silly thing
	sys.exit()

def maskpart(m):
	bit = 32
	while bit > 0:
		bit = (bit - int(m))
	return bit

# What the eff...hardcoded 3x255?  I need to fix that - note to self

def cidrmask(m):
	k = maskpart(m)
	q = "255.255.255." + str(255 - int(k))
	sk = struct.unpack('!L',socket.inet_aton(q))[0]
#	else:
#		sk = "FUCK THIS AND YOU!"
	return sk

if num.longip:
	num = ''.join(num.data)
	if "/" in str(num):
		ip = list(num.split('/'))
		mask = cidrmask(ip[1])
		print (str(mask))
		print (struct.unpack('!L',socket.inet_aton(ip[0]))[0])
		sys.exit()	
	else:
		long = struct.unpack('!L',socket.inet_aton(num))[0]
		print (long)

else:
	print ("NOTHING - use a flag")

