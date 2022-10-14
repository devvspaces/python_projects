# basic configuration
config setup
        charondebug="all"
        uniqueids=yes
        strictcrlpolicy=no

# connection to providus datacenter
conn spacepen-to-providus
        authby=psk
        left=%defaultroute
        leftid=139.162.251.79
        leftsubnet=192.168.150.143/24s
        right=154.113.16.42
        rightsubnet=192.168.156.27/32
        ike=aes256-sha2_256-modp1024!
        esp=aes256-sha2_256!
        keyingtries=3
        ikelifetime=1h
        lifetime=8h
        dpddelay=30
        dpdtimeout=120
        dpdaction=restart
        auto=start
        keyexchange=ikev1


	auto=start
	salifetime=1h
	keyexchange=ike
	ikelifetime=24h
	aggrmode=no
	authby=secret
	leftid=139.162.251.79
	left=139.162.251.79
	leftsubnet=192.168.150.1/17
	rightid=154.113.16.42
	right=154.113.16.42
	rightsubnet=192.168.156.27/32
	phase2=esp
	ike=aes-sha2_256
	phase2alg=aes-sha2_256
	compress=no
	ikev2=permit
	pfs=no
	rekey=yes
	type=tunnel


iptables -t nat -A POSTROUTING -s 192.168.156.27/32 -d 192.168.150.143/17 -j MASQUERADE


kTsJlWbV5syWS2FZz8Sf2lmjp


# source       destination
139.162.251.79 154.113.16.42 : PSK "kTsJlWbV5syWS2FZz8Sf2lmjp"



sudo nano /etc/ufw/before.rules
*nat
-A POSTROUTING -s 192.168.156.27/32 -o eth0 -m policy --pol ipsec --dir out -j ACCEPT
-A POSTROUTING -s 192.168.156.27/32 -o eth0 -j MASQUERADE
COMMIT

*mangle
-A FORWARD --match policy --pol ipsec --dir in -s 192.168.156.1/32 -o eth0 -p tcp -m tcp --tcp-flags SYN,RST SYN -m tcpmss --mss 1361:1536 -j TCPMSS --set-mss 1360
COMMIT


-A ufw-before-forward --match policy --pol ipsec --dir in --proto esp -s 192.168.156.1/32 -j ACCEPT
-A ufw-before-forward --match policy --pol ipsec --dir out --proto esp -d 192.168.156.1/32 -j ACCEPT