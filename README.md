# Compound-Protein Interaction dataset for Machine Learning Prediction

## Introduction

In this repository, I provide Compound-Protein Interactions (CPI) dataset for Machine Learning, Deep Learning prediction.

## Dataset

This dataset is consists of human and C.elegans CPI datasets defined by *Liu et al*.

n input is the pair of a SMILES format of compound and an amino acid sequence of protein; an output is a binary label (1 for interaction and 0 for not).
The SMILES is converted with RDKit.

## Usage

- `download.py` downloads SDF files for compounds and creates a list of fasta URLs for proteins.

- `main.py` merges PubChem ID, Uniprot ID, fasta sequences and SMILES. See `data/human.tsv` and `data/celegans.tsv`.

```bash
bash run.sh
```

## Reference

- [Liu et al., *Improving compound–protein interaction prediction by building up highly credible negative samples*, **Bioinformatics**, 2015.](https://doi.org/10.1093/bioinformatics/btv256)
