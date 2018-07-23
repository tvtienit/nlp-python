import io

def log_w(ctext):
	print('[INFO] ' + ctext, end='\n');

def read_data(filename):
	data = None
	with io.open(filename, 'r', encoding='utf8') as f:
		data = f.readlines()
		f.close()
	return data

def write_data(filename, data):
	with io.open(filename, 'w', encoding='utf8') as f:
		for element in data:
			f.write(element)
		f.close()

def enquiry(arr):
    if not arr:
        return 1
    else:
        return 0

def list_pop(list, entry, dest):
	new_list = list[entry:dest]
	del list[entry:dest]
	return new_list