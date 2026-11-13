#!/usr/bin/env python3
"""Copia data/banche/sito.json, data/npl/sito.json e data/imprese/sito.json dentro index.html.

Sostituisce i blocchi delimitati da /*DATI_BANCHE_INIZIO*/ ... /*DATI_BANCHE_FINE*/,
/*DATI_NPL_INIZIO*/ ... /*DATI_NPL_FINE*/ e /*DATI_IMPRESE_INIZIO*/ ... /*DATI_IMPRESE_FINE*/.
Solo libreria standard.
Uso: python3 tools/aggiorna_dati.py
"""
import json
import pathlib
import re
import sys

RADICE = pathlib.Path(__file__).resolve().parent.parent
SITO = RADICE / "index.html"
BLOCCHI = [
    ("DATI_BANCHE", RADICE / "data" / "banche" / "sito.json"),
    ("DATI_NPL", RADICE / "data" / "npl" / "sito.json"),
    ("DATI_IMPRESE", RADICE / "data" / "imprese" / "sito.json"),
]


def blocco(nome, percorso):
    testo = percorso.read_text(encoding="utf-8").strip()
    json.loads(testo)  # si ferma se il JSON non è valido
    # dentro <script> la sequenza "</" chiuderebbe il tag: "<\/" è equivalente in JSON e JS
    testo = testo.replace("</", "<\\/")
    return f"/*{nome}_INIZIO*/ const {nome} = {testo}; /*{nome}_FINE*/"


def main():
    html = SITO.read_text(encoding="utf-8")
    for nome, percorso in BLOCCHI:
        regola = re.compile(r"/\*" + nome + r"_INIZIO\*/.*?/\*" + nome + r"_FINE\*/", re.S)
        if len(regola.findall(html)) != 1:
            sys.exit(f"{nome}: blocco non trovato o ripetuto in index.html")
        nuovo = blocco(nome, percorso)
        html = regola.sub(lambda m: nuovo, html)
        print(f"{nome}: aggiornato da {percorso.relative_to(RADICE)}")
    SITO.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
