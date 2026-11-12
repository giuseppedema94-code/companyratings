# Rating Aziende

Prototipo di un rating indipendente delle aziende italiane con almeno 100 dipendenti, con voti da **A+ a F**, costruito su dati oggettivi e verificabili. Le aziende non pagano per entrare.

## Il foglio di esempio

`rating_aziende_esempio.xlsx` contiene 3 fogli:

- **Riepilogo**: punteggio per pilastro, totale da 0 a 100 e voto finale.
- **Indicatori**: 19 indicatori, ciascuno con soglie, peso, fonte e valori per 3 aziende di esempio.
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
