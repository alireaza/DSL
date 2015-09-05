#!/usr/bin/env python
import sys
import telnetlib

modem_ip = "192.168.1.1"
username = "admin"
password = "admin"

if len(sys.argv) < 2:
	sys.exit()

_command = sys.argv[1]

tn = telnetlib.Telnet(modem_ip)

tn.read_until("Username: ", 1)
tn.write(username.encode("ascii") + b"\r")

tn.read_until("Password: ")
tn.write(password.encode("ascii") + b"\r")

if _command == "reboot":
	tn.write(b"sys reboot\n")

if _command == "wan":
	if len(sys.argv) < 4:
		sys.exit()

	Sub_command = sys.argv[2]
	VPC_Index = sys.argv[3]

	if Sub_command == "on":
		tn.write(b"wan node index "+ VPC_Index +"\n")
		tn.write(b"wan node enable\n")
		tn.write(b"wan node save\n")

	if Sub_command == "off":
		tn.write(b"wan node index "+ VPC_Index +"\n")
		tn.write(b"wan node disable\n")
		tn.write(b"wan node save\n")


if _command == "wlan":
	if len(sys.argv) < 3:
		sys.exit()

	Sub_command = sys.argv[2]

	if Sub_command == "on":
		tn.write(b"rtwlan enableap\n")

	if Sub_command == "off":
		tn.write(b"rtwlan disableap\n")

tn.write(b"exit\n")
