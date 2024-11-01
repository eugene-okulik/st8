import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path_to_logs", help="Enter path to logs")
parser.add_argument("--find_word", help="Word for search")
#
args = parser.parse_args()
path_to_logs = args.path_to_logs
find_word = args.find_word

print(f"Start find in {path_to_logs}, word is {find_word}")
print(args.path_to_logs, args.find_word)