# Compound-Protein Interaction dataset for Machine Learning

## Introduction

Proteins are biomolecules that perform essential functions in living organisms and represent the majority of targets in drug discovery.
In small molecule drug discovery, where the interaction of a compound with a protein modifies the function of a disease-related protein,
a screening process is required in the initial stage to identify compounds that are likely to bind to the target protein from a large number of small molecule compounds.
This is done computationally through virtual screening.

This repository provides a script to prepare a dataset for virtual screening to predict compound-protein interactions.
The dataset includes the data proposed by *Liu et al*.
atasets for virtual screening based on literature have challenges such as lack of labels for non-interacting compound-protein combinations that interact,
and imbalance in the ratio of positives and negatives, which makes learning difficult.
This dataset attempts to improve on these points.

## Dataset

The dataset consists of two species, human and C. elegans.
Outcome labes are binary. 1 for interaction and 0 for none.

## Usage

- `download.py` downloads SDF files for compounds and creates a list of fasta URLs for proteins.

- `main.py` merges PubChem ID, Uniprot ID, fasta sequences and SMILES. See `data/human.tsv` and `data/celegans.tsv`.

```bash
bash run.sh
```

## Reference

- [Liu et al., *Improving compound–protein interaction prediction by building up highly credible negative samples*, **Bioinformatics**, 2015.](https://doi.org/10.1093/bioinformatics/btv256)
