# Scheda dati banche (esercizio 2025)

Stessa scheda, stesse fonti e stesso anno per ogni banca. Ogni dato ha fonte, link e citazione. Se un dato non si trova in una fonte verificabile resta `null` ("non disponibile"): nessuna stima.

Perimetro: gruppo consolidato, esercizio chiuso nel 2025.

| id | Dato | Unità | Fonte ammessa |
|---|---|---|---|
| proventi_2023, proventi_2024, proventi_2025 | Proventi operativi netti (o margine di intermediazione) | mln € | Comunicato risultati annuali / bilancio consolidato |
| utile_2023, utile_2024, utile_2025 | Utile netto di gruppo | mln € | idem |
| cost_income_2025 | Cost/income | % | idem |
| cet1_2025 | CET1 ratio a fine anno | % | idem |
| spese_personale_2025 | Spese per il personale | mln € | idem |
| dipendenti_2025 | Dipendenti del gruppo a fine anno | n. | Bilancio / rendiconto di sostenibilità |
| dipendenti_italia_2025 | Dipendenti in Italia | n. | idem |
| tempo_indeterminato_2025 | Quota dipendenti a tempo indeterminato | % | Rendiconto di sostenibilità |
| turnover_2025 | Tasso di turnover (uscite / organico) | % | idem |
| gender_pay_gap_2025 | Divario retributivo di genere (ESRS S1-16) | % | idem |
| donne_dirigenti_2025 | Donne tra i dirigenti | % | idem |
| formazione_2025 | Ore di formazione per dipendente | ore | idem |
| buono_pasto | Valore del buono pasto giornaliero | € | Accordo sindacale / contratto integrativo |
| smart_working | Giorni massimi di lavoro agile | giorni (per settimana o mese: specificare) | idem |
| premio_aziendale_2025 | Premio aziendale (VAP/PVR), importo di riferimento | € | idem |
| previdenza_azienda | Contributo dell'azienda alla previdenza complementare | % | idem |
| uscite_accordo | Uscite volontarie previste da accordi degli ultimi 3 anni | n. | Accordo sindacale / comunicato |
| assunzioni_accordo | Assunzioni previste dagli stessi accordi | n. | idem |
| glassdoor | Valutazione media e numero recensioni | stelle, n. | Glassdoor |
| indeed | Valutazione media e numero recensioni | stelle, n. | Indeed |
| sede | Indirizzo della sede centrale | testo | Sito aziendale |

## Regole uniche (valgono per tutte le banche)

1. **Fonti.** Solo sito ufficiale del gruppo (comunicati, bilancio, rendiconto di sostenibilità) e comunicati dei sindacati del credito. Giornali e siti di notizie non sono ammessi: un valore preso da lì va ricercato sulla fonte ufficiale o messo a `null`.
2. **Proventi.** Proventi operativi netti del conto economico riclassificato, come pubblicati nel comunicato sui risultati annuali. Se il perimetro cambia tra un anno e l'altro (acquisizioni), scriverlo in `note`.
3. **Utile.** Utile netto dichiarato di pertinenza della capogruppo, non rettificato. Le voci straordinarie rilevanti vanno in `note`.
4. **Cost/income.** Quello del conto economico riclassificato, con i decimali della tabella se presenti.
5. **CET1.** Versione a regime ("fully loaded" o "fully phased"). Se esiste solo una versione, usarla e scriverlo in `note`.
6. **Spese per il personale.** Conto economico riclassificato.
7. **Dati sul personale.** Dal rendiconto di sostenibilità 2025 (ESRS S1), perimetro di gruppo. `tempo_indeterminato_2025` si può calcolare se numeratore e denominatore sono nella stessa tabella: riportarli entrambi nella citazione o in `note`.
8. **Dati contrattuali** (buono pasto, lavoro agile, previdenza, premio). Vale l'accordo firmato in vigore al 31/12/2026, anche se decorre nel 2026. Accordi che decorrono dal 2027 no. Scrivere la decorrenza in `note`.
9. **Lavoro agile.** In giorni al mese, per le strutture centrali. Giorni l'anno ÷ 12; giorni la settimana × 4. Scrivere in `note` il dato originale e l'eventuale regola diversa per la rete.
10. **Premio aziendale.** Importo lordo in denaro per l'esercizio 2025, figura media o livello di riferimento indicato dall'accordo. L'eventuale maggiorazione welfare va in `note`.
11. **Uscite e assunzioni.** Somma degli accordi firmati dal 1/1/2024 al 31/12/2026; elencare gli accordi in `note`.
12. **Recensioni.** Media e numero di recensioni della pagina italiana dell'azienda, con data di lettura in `note`.
13. **Somme.** Oltre ai calcoli delle regole 7 e 9 sono ammesse le somme tra righe della stessa tabella o tra accordi (regola 11), con gli addendi in `note`.
14. **Lavoro agile da giornali.** Solo per il lavoro agile, se manca un documento ufficiale o sindacale è ammesso un articolo di giornale. In scheda il dato porta la dicitura "fonte giornalistica" e `verifica` vale "fonte giornalistica".

Formato di ogni dato nel file `<slug>.json`:

```json
{"id": "cet1_2025", "valore": 13.2, "unita": "%", "anno": 2025,
 "fonte_titolo": "...", "fonte_url": "https://...",
 "citazione": "breve frase della fonte che contiene il numero",
 "note": ""}
```
