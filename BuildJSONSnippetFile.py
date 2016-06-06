# Converts a directory tree of sublime-snippet files to a single JSON snippets file for Atom
import os, untangle, json

data = {}
data['.source.papyrus.fallout4'] = {}

for root, dirs, files in os.walk('.'):
	for f in files:
		if f.endswith('.sublime-snippet'):
			filePath = os.path.join(root, f)
			print('Parsing ' + filePath)
			xml = untangle.parse(filePath)
			snippetName = xml.snippet.description.cdata
			if '.' not in snippetName: snippetName += '.' + xml.snippet.tabTrigger.cdata
			snippet = data['.source.papyrus.fallout4'][snippetName] = {}
			snippet['prefix'] = xml.snippet.tabTrigger.cdata
			snippet['body'] = xml.snippet.content.cdata.replace('    ', '\t')

json.dump(data, open('snippets.json', 'w'), indent='\t')
