# Appunti di Data & Techniques for e-health

Appunti del corso data techniques for e-health A.A. 2023/2024

## Conversione di un singolo file

Per convertire con Pandoc:

`pandoc -s input.md -o output.pdf --mathml`

Documentazione Pandoc: <https://pandoc.org/MANUAL.html>

Nella repo è presente un file `.yaml` per personalizzare le esportazioni.
`pandoc -s input.md -o output.pdf --metadata-file=config.yaml --mathml`

## Creazione di un file unico 

Creazione di un file unico tramite comando manuale:

- `pandoc -s 'elenco_dei_files'.pdf -o Appunti --metadata-file=config.yaml --mathml`

Creazione di un file unico tramite script Python:

- `python3 convert.py  --nome Appunti  --export opzione_per_esportare`

Le opzioni di esportazione sono:

- `standard`
- `pc`
- `stampa`

Sono presenti più file per i metadati, ognuno è ottimizzato per un uso specifico:

- `config.yaml`: file di configurazione basico
- `configPcVersion.yaml`: versione ottimizza l'uso su computer
- `configPrintVersion.yaml`: versione ottimizzata per la stampa e la rilegatura
