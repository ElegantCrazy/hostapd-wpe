def log2hashcat():
	hashes = {}
	with open('hostapd-wpe.log', 'r') as f:
		while True:
			line = f.readline()
			if line == '':
				break
			if line.startswith('mschapv2:'):
				username = ''
				hashcatvalue = ''
				while True:
					line = f.readline().strip()
					if line == '':
						break
					elif line.startswith('username:'):
						username = line[len('username:'):].strip()
					elif line.startswith('hashcat NETNTLM:'):
						hashcatvalue = line[len('hashcat NETNTLM:'):].strip()
				if username not in hashes:
					hashes[username] = hashcatvalue
	with open('hashes.txt', 'w') as f:
		for value in hashes.values():
			f.write(value + '\n')

if __name__ == '__main__':
	log2hashcat()