import pandas as pd
import numpy as np
from Bio import SeqIO
from rdkit import Chem, RDLogger
import argparse
import os

RDLogger.DisableLog('rdApp.*')

def main(args):
    df = pd.read_csv('data/%s.tsv' % (args.dataset), sep='\t')

    fasta = dict()
    for uniprot in os.listdir('fasta'):
        for seq in SeqIO.parse('fasta/%s' % (uniprot), 'fasta'):
            fasta[uniprot[:-len('.fasta')]] = str(seq.seq)

    smiles = dict()
    for sdf in os.listdir('sdf'):
        for mol in Chem.SDMolSupplier('sdf/%s' % (sdf)):
            if mol:
                cid = mol.GetIntProp('PUBCHEM_COMPOUND_CID')
                smi = mol.GetProp('PUBCHEM_OPENEYE_ISO_SMILES')
                smiles[cid] = smi

    df['seq'] = df['uniprot'].map(lambda x: fasta.get(x, None)) 
    df['smi'] = df['cid'].map(lambda x: smiles.get(x, None)) 

    # Exclude missing sequences and compounds
    df = df.dropna()

    df.to_csv('data/%s.tsv' % (args.dataset), sep='\t', index=False)
    print(df)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', default='human', choices=['human', 'celegans'])
    args = parser.parse_args()
    print(vars(args))
    
    main(args)
