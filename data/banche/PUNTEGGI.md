# Punteggi banche: modello provvisorio

Stato: applicato sul sito dal 12/11/2026, con voti marcati "provvisorio". I dati usati dal sito sono in `sito.json`.

Formula uguale al resto del progetto: ogni indicatore vale da 0 a 100 punti in proporzione tra le due soglie; il punteggio di un'area è la media dei suoi indicatori; il totale è la media pesata delle aree con dati. Voto solo se sono presenti almeno 8 indicatori su 11.

| Area (peso) | Indicatore | 0 punti | 100 punti |
|---|---|---|---|
| Solidità (35%) | Crescita media annua dei proventi 2023-2025 | -5% | +10% |
| | Crescita media annua dell'utile 2023-2025 | -10% | +20% |
| | Andamento del costo del personale, media annua 2023-2025 (un calo indica tagli) | -5% | +5% |
| | Cost/income 2025 | 65% | 40% |
| | CET1 2025 | 11% | 17% |
| Retribuzione (25%) | Costo medio per dipendente (spese per il personale / dipendenti) | 60.000 € | 100.000 € |
| | Buono pasto | 4 € | 10 € |
| Stabilità (20%) | Dipendenti a tempo indeterminato | 90% | 100% |
| | Turnover | 15% | 3% |
| Crescita e parità (20%) | Ore di formazione per dipendente | 20 | 70 |
| | Divario retributivo di genere | 35% | 5% |

## Limiti noti

- Le soglie sono una scelta di progetto, non vengono da una fonte.
- MPS: la crescita è calcolata a perimetro costante (2025 escluso Mediobanca: proventi 4.073,9, utile 2.749,9). Anche costo medio per dipendente e andamento del costo del personale usano i dati 2025 senza Mediobanca (spese 1.281,2, dipendenti 16.546). Il turnover pubblicato esclude Mediobanca.
- BPER: le spese per il personale 2023 includono costi straordinari per le uscite e il 2025 include la Popolare di Sondrio; l'andamento 2023-2025 (-5,15% l'anno) non indica da solo tagli al personale.
- Il costo medio per dipendente comprende contributi e incentivi all'uscita: non è lo stipendio.
- UniCredit: circa metà del personale è all'estero.
- Credem: i proventi sono il margine di intermediazione; il cost/income viene da una tabella UILCA, non dal comunicato della banca; mancano i dati del rendiconto di sostenibilità.
- Lavoro agile, premio aziendale, previdenza, uscite e assunzioni, recensioni: dati troppo incompleti, esclusi dal punteggio.
