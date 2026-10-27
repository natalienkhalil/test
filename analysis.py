import csv
import json
from pathlib import Path

with (Path(__file__).parent / 'data' / 'values.csv').open() as source:
    values = [float(row['value']) for row in csv.DictReader(source)]
print(json.dumps({'count': len(values), 'mean': sum(values) / len(values)}))
