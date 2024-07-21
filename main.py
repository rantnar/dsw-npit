import argparse
import json

parser = argparse.ArgumentParser(description='Program do konwersji danych.')
parser.add_argument('pathFile1', type=str, help='Ścieżka do pliku źródłowego')
parser.add_argument('pathFile2', type=str, help='Ścieżka do pliku docelowego')
args = parser.parse_args()

try:
    with open(args.pathFile1, 'r') as f:
        data = json.load(f)
except json.JSONDecodeError:
    print("Błąd składni w pliku .json")

try:
    with open(args.pathFile2, 'w') as f:
        json.dump(data, f)
except Exception as e:
    print(f"Błąd zapisu do pliku: {e}")

#test2