from googletrans import Translator
import io
import time

SRC_FILE  = '../data/harry_potter.tkn.vi'
DEST_FILE = '../data/harry_potter.gtrans.eng' 

# -------------------------------------#
def log_w(ctext):
	print('[INFO] ' + ctext, end='\n');

def run_translation(data, sleep, limit_per_sleep):
	translations = []
	if sleep is not None and sleep == True:
		if limit_per_sleep is None:
			limit_per_sleep = 100
		sleep_times = 1
		for text in data:
			translations.append(translator.translate(text, src="vi", dest="en"))
			if sleep_times == limit_per_sleep:
				sleep_times = 1
				log_w('Waiting for 10 seconds to continue...')
				time.sleep(10)
			else:
				sleep_times = sleep_times + 1
	else:
		translations = translator.translate(data, src="vi", dest="en")
	return translations

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

translator = Translator()

log_w("Reading file...")
src_data = read_data(SRC_FILE)

log_w("Translating...")
translations = run_translation(src_data, sleep = True, limit_per_sleep = 1000)

log_w("Writing new file...")
write_data(DEST_FILE, list(map(lambda x: x.text, translations)))
log_w("Done")