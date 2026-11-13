# Scheda dati imprese (tech, moda, alimentare, bevande, grande distribuzione), esercizio 2025

Valgono le "Regole uniche" di `../banche/SCHEMA.md`: solo documenti ufficiali della società o del gruppo e comunicati sindacali; ogni numero ha fonte, link e citazione; se un dato non si trova resta `null`. Nessuna stima, nessuna conversione di valuta.

**Esercizio.** "2025" è l'esercizio chiuso tra il 1° luglio 2025 e il 30 giugno 2026; "2024" e "2023" i due precedenti. Scrivere in `note` la data di chiusura se non è il 31 dicembre. Esempio: un bilancio chiuso il 31 dicembre 2025 È l'esercizio 2025 (caso normale); uno chiuso il 30 aprile 2026 anche.

**Divieti.** Usare solo ricerca web, curl, lettura e scrittura di file. Non creare attività programmate, promemoria, eventi o messaggi.

**Perimetro.** Gruppo consolidato se la capogruppo è italiana. Per la filiale italiana di un gruppo estero: solo i dati della società italiana. Scrivere il perimetro in `perimetro` e, per ogni dato che ne usa uno diverso, in `note`.

| id | Dato | Unità |
|---|---|---|
| ricavi_2023, ricavi_2024, ricavi_2025 | Ricavi consolidati | mln (valuta del bilancio) |
| ebitda_2023, ebitda_2024, ebitda_2025 | EBITDA come pubblicato (se c'è la versione rettificata, usarla e dirlo in note) | mln |
| ebit_2025 | EBIT / risultato operativo come pubblicato | mln |
| utile_2023, utile_2024, utile_2025 | Utile netto di pertinenza della capogruppo, dichiarato | mln |
| debito_netto_2025 | Posizione finanziaria netta a fine anno (debito positivo, cassa netta negativa), come pubblicata | mln |
| spese_personale_2023, spese_personale_2024, spese_personale_2025 | Costo del personale | mln |
| dipendenti_2023, dipendenti_2024, dipendenti_2025 | Dipendenti a fine anno (persone, non FTE; se solo FTE o media, dirlo in note) | n. |
| dipendenti_italia_2025 | Dipendenti in Italia | n. |
| tempo_indeterminato_2025 | Quota a tempo indeterminato (calcolo ammesso se numeratore e denominatore sono nella stessa tabella) | % |
| turnover_2025 | Tasso di turnover (uscite / organico) come pubblicato | % |
| gender_pay_gap_2025 | Divario retributivo di genere (ESRS S1-16) | % |
| formazione_2025 | Ore di formazione per dipendente | ore |
| ccnl | Contratto collettivo applicato in Italia | testo |
| buono_pasto | Buono pasto giornaliero o mensa | € o testo |
| smart_working | Lavoro agile, come scritto nella fonte (giorni al mese, a settimana, %) | testo |
| premio_aziendale_2025 | Premio di risultato lordo, esercizio 2025 | € |
| cassa_integrazione | Anni con cassa integrazione o contratti di solidarietà in Italia tra 2023 e 2025 (0 solo se la fonte lo dice) | n. |
| licenziamenti_collettivi | Persone in procedure di licenziamento collettivo o esuberi dichiarati in Italia dal 1/1/2024 al 31/12/2026 | n. |
| sede | Indirizzo della sede in Italia | testo |

## Istruzioni per chi raccoglie i dati

Fonti ammesse: sito ufficiale della società o del gruppo (comunicato sui risultati annuali, relazione finanziaria annuale con rendiconto di sostenibilità, bilancio di sostenibilità, documenti dei due anni precedenti per le colonne di confronto); comunicati dei sindacati (Filcams, Fisascat, Uiltucs, Flai, Fai, Uila, Filctem, Femca, Uiltec, Fiom, Fim, Uilm, Slc, Fistel, Uilcom) per contratto, buono pasto, lavoro agile, premio, cassa integrazione, esuberi. Per il solo lavoro agile è ammesso un articolo di giornale, con `"verifica": "fonte giornalistica"`. Niente altre fonti.

Metodo obbligatorio (serve al controllo automatico):
1. Crea `/tmp/fonti/<slug>/` e scarica ogni fonte con `curl -sSL -A "Mozilla/5.0" <url> -o file`.
2. Converti in testo: `pdftotext -layout file file.txt`; per HTML togli i tag con `python3 -I`.
3. Trova i numeri con `grep -n -i` sulle parole chiave (EBITDA, "costo del personale", "personnel", "S1-6", turnover, "S1-16", "ore di formazione", "posizione finanziaria netta") e leggi solo le righe attorno. Non leggere i file interi.
4. Per ogni id dello schema scrivi `{id, valore, unita, anno, fonte_titolo, fonte_url, fonte_file, citazione, note}`. `citazione` è una stringa copiata identica dal .txt, una sola riga, massimo 12 parole, che contiene il numero. `fonte_file` è il percorso del .txt, oppure `null` se curl era bloccato e hai letto con WebFetch.
5. Dato assente, o con anno o definizione diversa: `"valore": null` e in `note` cosa hai trovato. Mai memoria, mai stime, mai calcoli tranne quello di `tempo_indeterminato_2025` (con i due numeri in `note`).
6. Massimo 14 chiamate web tra ricerche, curl e letture.
7. Scrivi `/home/claude/companyratings/data/imprese/<slug>.json`: `{"azienda", "slug", "settore", "perimetro", "valuta", "chiusura_esercizio", "raccolto_il": "2026-11-13", "dati": [...tutti gli id, nell'ordine dello schema...]}`. Valida con `python3 -I -m json.tool`. Nessun altro file del progetto, niente git.
8. Risposta finale in 5 righe al massimo: dati trovati su quanti, id rimasti null, dubbi.
