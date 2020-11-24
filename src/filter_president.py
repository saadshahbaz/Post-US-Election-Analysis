import json
import argparse
import pandas as pd


def filter_president(file, output_file):
    """
    only consider reddit posts with Trump or  Biden mentions

    """

    table = {'title': []}
    with open(file) as f:
        for line in f:
            data = json.loads(line)
            if "trump" in data['title'].lower() or "biden" in data['title'].lower():
                table['title'].append(data['title'])
    df = pd.DataFrame(table)
    df['coding'] = ''
    df.to_csv(output_file, sep='\t', encoding='utf-8', index=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-o', help="Alternative Output File Name. Defaults to stdout", default='data.tsv')
    parser.add_argument('json_file')
    args = parser.parse_args()

    input_file = args.json_file
    output_file = args.o

    filter_president(input_file, output_file)


if __name__ == '__main__':
    main()
