#!/bin/bash

pip install -qr requirements.txt

# make required directories.
mkdir -p fasta model

# retrieve fasta urls and compound files.
python download.py --dataset human
python download.py --dataset celegans

# retrieve fasta files.
wget -nc -i data/human.fasta -P fasta -q
wget -nc -i data/celegans.fasta -P fasta -q

# merge fasta and smiles
python main.py --dataset human
python main.py --dataset celegans
