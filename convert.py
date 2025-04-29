import subprocess
from pathlib import Path
import argparse
import sys
import re

def check_pandoc():
    try:
        subprocess.run(["pandoc", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("Pandoc non è installato")
        sys.exit(1)

check_pandoc()

parser = argparse.ArgumentParser()
parser.add_argument("--nome", nargs="?", default="Appunti", help="Nome file output")
parser.add_argument("--export", nargs="?", default="standard", help="standard, pc, stampa")
args = parser.parse_args()

match args.export:
    case "standard":
        export_settings = "config.yaml"
    case "pc":
        export_settings = "configPcVersion.yaml"
    case "stampa":
        export_settings = "configPrintVersion.yaml"
    case _:
        print("Export non valido.")
        sys.exit(1)


def extract_number(file):
    match = re.match(r"(\d+)", file.stem)
    return int(match.group(1)) if match else float('inf')

md_files = sorted(Path('./Appunti').rglob('*.md'), key=extract_number)

if not md_files:
    print("Nessun file .md trovato.")
    sys.exit(1)
else:
    cmd = [
        "pandoc", 
        "-s", *map(str, md_files),
        "-o", f"{args.nome}.pdf",
        "--metadata-file=" + export_settings,
        "--mathml"
    ]
    subprocess.run(cmd)
