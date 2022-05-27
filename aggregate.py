import os
import pandas as pd
import datetime

DIR = "./Info files/"

CSV_RESULT_FILE_PATH = DIR + "results.csv"
QUARTER_RESULT_FILE_PATH = DIR + "quarter_results.xlsx"

OUTPUT_DIR = "./output/"
BROKEN_FILE_PATH = DIR + "broken_outputs.txt"

def what_quartet(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4

output_files = sorted(os.listdir(OUTPUT_DIR), key=lambda name: int(name.split('_')[0]))
broken_files = list(map(lambda x: x[:-1], open(BROKEN_FILE_PATH, "r").readlines()))

simple_count = 0
separable_count = 0
ambiguous_count = 0
intractable_count = 0

start_date = datetime.datetime.fromisoformat("2009-01-03 18:15")

open(CSV_RESULT_FILE_PATH, "w").write("Date,Separable,Ambiguous,Intractable,Simple\n")

for file in output_files:
    if file in broken_files:
        continue

    block_lines = open(OUTPUT_DIR + file, "r").readlines()

    if block_lines[0] == '\n':
        continue

    block_date = datetime.datetime.fromtimestamp(int(block_lines[0]))
    verdicts = list(filter(lambda x: x.startswith("#") , block_lines))

    if block_date.month != start_date.month:
        res_str = f"{start_date.year} {start_date.month},{separable_count},{ambiguous_count},{intractable_count},{simple_count}\n"
        open(CSV_RESULT_FILE_PATH, "a+").write(res_str)
        start_date = block_date
        simple_count = 0
        separable_count = 0
        ambiguous_count = 0
        intractable_count = 0

    for verdict in verdicts:
        last_word = verdict.split()[-1]

        if last_word == "SIMPLE":
            simple_count += 1
        elif last_word == "SEPARABLE":
            separable_count += 1
        elif last_word == "AMBIGUOUS":
            ambiguous_count += 1
        else:
            intractable_count += 1

res_str = f"{start_date.year} {start_date.month},{separable_count},{ambiguous_count},{intractable_count},{simple_count}\n"
open(CSV_RESULT_FILE_PATH, "a+").write(res_str)

read_file = pd.read_csv(CSV_RESULT_FILE_PATH)

read_file["Year"] = read_file["Date"].apply(lambda x: int(x.split()[0]))
read_file["Month"] = read_file["Date"].apply(lambda x: int(x.split()[1]))
read_file["Quarter"] = read_file["Month"].apply(what_quartet)

read_file = read_file.drop(["Month"], axis=1).groupby(["Year", "Quarter"]).sum().reset_index()
read_file.insert(loc=0, column="Date", value=(read_file["Year"].apply(lambda x: str(x)) + read_file["Quarter"].apply(lambda x: " " + str(x) + "q")))

read_file.drop(["Year", "Quarter"], axis=1).to_excel(QUARTER_RESULT_FILE_PATH, index = None, header=True, sheet_name="Quarters")

os.remove(CSV_RESULT_FILE_PATH)