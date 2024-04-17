import argparse

parser = argparse.ArgumentParser()

# Add the arguments
parser.add_argument('--name', type=str, help='Name', default='default_name')
parser.add_argument('--value', type=int, help='Value', default=0)

# Parse the arguments
args = parser.parse_args()

print(f"Name: {args.name}")
print(f"Value: {args.value}")