import bleu
import helper
from progressbar import ProgressBar

ORIG_FILE  = '../data/harry_potter.eng.tkn'
SIMI_FILE_SRC_LANG  = '../data/harry_potter.gtrans.eng'
SIMI_FILE_TAR_LANG  = '../data/harry_potter.tkn.vi'
DEST_FILE  = '../data/harry_potter.similarity'

ORIG_FILE  = '../data/inp1'
SIMI_FILE_SRC_LANG  = '../data/inp2'
SIMI_FILE_TAR_LANG  = '../data/inp3'
DEST_FILE  = '../data/output_vi'

def get_max_bleu(src_sent, tgt_arr):
	max_bleu = -1.0
	bleu_index = [0, 0]
	curr_bleu = -1.0
	for i in range(len(tgt_arr)):
		j = i
		while j < len(tgt_arr):
			curr_bleu = bleu.compute(src_sent, ' '.join(tgt_arr[i:j]))
			if curr_bleu > max_bleu:
				max_bleu = curr_bleu
				bleu_index[0] = i
				bleu_index[1] = j
			j = j + 1

	return (max_bleu, bleu_index[0], bleu_index[1])

def print_result(src_results, tgt_results):
	for i in range(len(src_results)):
		print('------' + str(i) + '------\n')
		print(src_results[i] + '\n' + tgt_results[i] + '\n')


def similarize(orig_data, simi_src_data, simi_tar_data, batch_size = 50):
	max_bleu = -1.0
	bleu = [0, 0]
	en_point = 0
	de_point = 0
	tgt_results = []
	pbar = ProgressBar()
	for i in pbar(range(len(orig_data))):
		en_point = i - batch_size
		de_point = i + batch_size
		if en_point < 0:
			en_point = 0
		if de_point > len(simi_src_data) - 1:
			de_point = len(simi_src_data) - 1
		max_bleu, bleu[0], bleu[1] = get_max_bleu(orig_data[i], simi_src_data[en_point:de_point])
		tgt_results.append(' '.join(simi_tar_data[(en_point + bleu[0]):(en_point + bleu[1])]))

	print_result(orig_data, tgt_results)

	return tgt_results



helper.log_w("Reading data. Please wait...")
orig_data = helper.read_data(ORIG_FILE)
simi_src_data = helper.read_data(SIMI_FILE_SRC_LANG)
simi_tar_data = helper.read_data(SIMI_FILE_TAR_LANG)

helper.log_w("Compute similarity...")
out_tgt_data = similarize(orig_data, simi_src_data, simi_tar_data, 10)

helper.log_w("Writing new data...")
helper.write_data(DEST_FILE, out_tgt_data)

helper.log_w("Done.")