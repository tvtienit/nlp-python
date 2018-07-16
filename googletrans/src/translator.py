from googletrans import Translator
import io

SRC_FILE  = '../data/trans.inp'
DEST_FILE = '../data/trans.out' 

def read_data(filename):
	data = None
	with io.open(filename, 'r', encoding='utf8') as f:
		data = f.readlines()
		f.close()
	return data

def write_data(filename, data):
	with io.open(filename, 'w', encoding='utf8') as f:
		for element in data:
			f.write(element + '\n')
		f.close()

def log_w(ctext):
	print('[INFO] ' + ctext, end='\n');

translator = Translator()

log_w("Reading file...")
srcText = read_data(SRC_FILE)

log_w("Translating...")
translations = translator.translate(srcText, src="vi", dest="en")

log_w("Writing new file...")
write_data(DEST_FILE, list(map(lambda x: x.text, translations)))
log_w("Done")