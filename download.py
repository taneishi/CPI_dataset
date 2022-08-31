import pandas as pd
import pubchempy as pcp
import argparse
import os

def main(args):
    if args.dataset == 'human':
        positive = 'data0/homo_positive.csv'
        negative = 'data2/human/samples_with_high_quality_negative_samples.csv'
    elif args.dataset == 'celegans':
        positive = 'data0/celegan_positive.csv'
        negative = 'data2/elegans/samples_with_high_quality_negative_samples.csv'

    positive = pd.read_csv('%s/%s' % (args.data_dir, positive), names=['cid', 'uniprot'], skiprows=1)
    positive['interaction'] = 1
    negative = pd.read_csv('%s/%s' % (args.data_dir, negative), names=['cid', 'uniprot'])
    negative['interaction'] = 0
    
    df = pd.concat([positive, negative]) 
    df.to_csv('data/%s.tsv' % (args.dataset), sep='\t', index=False)
    print(df)
    print(df.groupby('interaction').size().to_dict())

    with open('data/%s.fasta' % (args.dataset), 'w') as out:
        for i, row in df.iterrows():
            out.write('https://www.uniprot.org/uniprot/%s.fasta\n' % (row['uniprot']))

    os.makedirs('sdf', exist_ok=True)
    for index, (i, row) in enumerate(df.iterrows(), 1):
        if not os.path.exists('sdf/%d.sdf' % (row['cid'])):
            pcp.download('SDF', 'sdf/%d.sdf' % (row['cid']), row['cid'])
        print('\r%4d/%4d compounds downloaded' % (index, df.shape[0]), end='')
    print('')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default='data/Liu', type=str)
    parser.add_argument('--dataset', default='human', choices=['human', 'celegans'])
    args = parser.parse_args()
    print(vars(args))

    main(args)
