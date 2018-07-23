import bleu
import helper
from progressbar import ProgressBar

ORIG_FILE  = '../data/HarryPotterPart/Part1/part1.en'
SIMI_FILE_SRC_LANG  = '../data/HarryPotterPart/Part1/translate.vi-en.en'
SIMI_FILE_TAR_LANG  = '../data/HarryPotterPart/Part1/part1.vi'
DEST_FILE  = '../data/HarryPotterPart/Part1/output.vi'

# ORIG_FILE  = '../data/inp1'
# SIMI_FILE_SRC_LANG  = '../data/inp2'
# SIMI_FILE_TAR_LANG  = '../data/inp3'
# DEST_FILE  = '../data/output_vi'



def get_max_bleu(src_sent, tgt_arr):
	max_bleu = -1
	max_bleu_i = 0
	curr_bleu = -1
	for i in range(len(tgt_arr)):
		curr_bleu = bleu.compute(src_sent, tgt_arr[i])
		if curr_bleu > max_bleu:
			max_bleu = curr_bleu
			max_bleu_i = i

	return (max_bleu, max_bleu_i)

def print_result(src_results, tgt_results):
	for i in range(len(src_results)):
		print('------' + str(i + 1) + '------\n')
		print(src_results[i] + '\n' + tgt_results[i] + '\n')


def similarize(orig_data, simi_src_data, simi_tar_data, batch_size = 1000):
	tgt_results = []
	bleu = [-1, 0] #[max_bleu, index]
	en_point = 0
	de_point = 0
	pbar = ProgressBar()
	for i in pbar(range(len(orig_data))):
		en_point = i - batch_size
		de_point = i + batch_size
		if en_point < 0:
			en_point = 0
		if de_point > len(simi_src_data) - 1:
			de_point = len(simi_src_data) - 1
		bleu[0], bleu[1] = get_max_bleu(orig_data[i], simi_src_data[en_point:de_point])
		tgt_results.append(simi_tar_data[en_point + bleu[1]])

	return tgt_results


helper.log_w("Reading data. Please wait...")
orig_data = helper.read_data(ORIG_FILE)
simi_src_data = helper.read_data(SIMI_FILE_SRC_LANG)
simi_tar_data = helper.read_data(SIMI_FILE_TAR_LANG)

helper.log_w("Compute similarity...")
out_tgt_data = similarize(orig_data, simi_src_data, simi_tar_data, 750)

helper.log_w("Writing new data...")
helper.write_data(DEST_FILE, out_tgt_data)

helper.log_w("Done.")