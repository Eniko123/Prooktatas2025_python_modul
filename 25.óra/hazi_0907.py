import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str, help='input file')
parser.add_argument('filter', type=str, help='filter out words from text')

args = parser.parse_args()
try:
    with open(args.input, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f'File {args.input} not found.')

filtered_lines = [line.strip() for line in lines if args.filter in line]

if filtered_lines:
    print(filtered_lines)
else:
    print('None of the lines contain filter')



