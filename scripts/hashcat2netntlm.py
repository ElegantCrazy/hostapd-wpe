def hashcat2netntlm():
	with open('hashes.txt', 'r') as fin:
		with open('netntlm.txt', 'w') as fout:
			for line in fin:
				hashvalue = line.strip()
				split = hashvalue.split(':')
				ntresp = split[-2]
				challenge = split[-1]
				fout.write('$NETNTLM$' + challenge + '$' + ntresp + '\n')

if __name__ == '__main__':
	hashcat2netntlm()