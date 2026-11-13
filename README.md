# Rating Aziende

Prototipo di un rating indipendente delle aziende italiane con almeno 100 dipendenti, con voti da **A+ a F**, costruito su dati oggettivi e verificabili. Le aziende non pagano per entrare.

## Il foglio di esempio

`rating_aziende_esempio.xlsx` contiene 3 fogli:

- **Riepilogo**: punteggio per pilastro, totale da 0 a 100 e voto finale.
- **Indicatori**: 19 indicatori, ciascuno con soglie, peso, fonte e valori per 3 aziende di esempio.

Nota: il foglio usa ancora la versione a 19 indicatori. Il sito usa il modello generale aggiornato a 20 indicatori, con la regola sulla cassa integrazione.
- **Parametri**: pesi dei pilastri, soglie dei voti e regole del modello.

Le celle gialle con testo blu si possono modificare, tutto il resto è calcolato. **Le aziende e i valori sono fittizi.**

## Metodo

Ogni indicatore vale da 0 a 100 punti, con interpolazione lineare tra un valore peggiore (0 punti) e uno migliore (100 punti).

| Pilastro | Peso |
|---|---|
| Solidità economica (fatturato, EBIT, debito) | 25% |
| Retribuzione e benefit (costo medio, buoni pasto, premio, welfare) | 25% |
| Stabilità del lavoro (contratti a termine, cassa integrazione, licenziamenti, turnover) | 20% |
| Flessibilità e sede (smart working, raggiungibilità) | 15% |
| Relazioni industriali e parità (contratto integrativo, vertenze, gap di genere) | 10% |
| Percezione dei dipendenti (Glassdoor, Indeed, minimo 30 recensioni) | 5% |

Voti: A+ ≥90 · A ≥80 · B ≥70 · C ≥60 · D ≥50 · E ≥40 · F <40

## Il sito

`index.html` è un unico file statico, senza dipendenze: classifica, card, scheda azienda, confronto e metodo. Contiene due modelli.

- **Banche, dati reali 2025**: 7 banche, 11 indicatori in 4 aree (Solidità 35%, Retribuzione 25%, Stabilità 20%, Crescita e parità 20%). Voto solo con almeno 8 indicatori su 11; i voti sono provvisori. Ogni numero ha la fonte con il link al documento ufficiale.
- **Aziende demo, dati fittizi**: modello generale con 20 indicatori in 6 aree. Cassa integrazione: 0 anni negli ultimi 3 valgono 100 punti, 1 anno 20, 2 anni 5, 3 anni 0; con almeno un anno la Stabilità del lavoro non supera 50 punti.

Dati e regole delle banche sono in `data/banche/`: `sito.json` è la fonte dei dati copiati nel sito, `SCHEMA.md` le regole di raccolta, `PUNTEGGI.md` le soglie.

Gestione crediti (doValue, AMCO, Intrum Italy, Cerved Group): solo dati da `data/npl/sito.json`, senza voto finché il modello non è definito.

`tools/aggiorna_dati.py` copia `data/banche/sito.json` e `data/npl/sito.json` dentro `index.html` (blocchi `DATI_BANCHE` e `DATI_NPL`): `python3 tools/aggiorna_dati.py`.
