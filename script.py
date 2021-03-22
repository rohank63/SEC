import infer_organism

import subprocess as sp



print(infer_organism.infer(
	file_1="./first_mate.fastq",
	min_match=2,factor=1,
	transcript_fasta="transcripts.fasta.zip"
	))

print(infer_organism.infer(
	file_1="./SRR13496438.fastq.gz",
	min_match=2,factor=1,
	transcript_fasta="transcripts.fasta.zip"
	))

'''
print(infer_read_orientation.infer(
	file_1="./files/SRR13496438.fastq.gz",
	fasta="transcripts.fasta.zip",
	organism="oaries"
	))



import subprocess as sp

file_1 = "./files/SRR13496438.fastq.gz"
quant_single = "kallisto quant -i transcripts.idx -o output" + \
        " -l 100 -s 300 --single " + file_1

result = sp.run(quant_single, shell=True,capture_output=True, text=True)


print(result.stderr)
print(result.returncode)
'''
