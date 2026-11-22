# Creating the Wikidata item for CIP

Step-by-step guide for creating a Wikidata item for the Belgian Catholic news agency `org.ent.pressagency.cip` (Centre d'information de presse), which currently has no Wikidata item. All QIDs and property IDs below were checked against Wikidata.

## 0. Before you start

1. Log in at <https://www.wikidata.org>.
2. Search once more for duplicates: `Centre d'information de presse`, `Centrum voor Informatie aan de Pers`, `CIP vzw`, `agence de presse CIP`. A search in November 2026 found nothing.
3. Do not confuse CIP with the *Centre d'Information de Presse francophone*, a separate non-profit association registered in 1991 (enterprise number 0444.853.777). Its relationship to CIP has not been established.
4. Keep the source URLs from step 4 open in a tab.

## 1. Create the item

Open <https://www.wikidata.org/wiki/Special:NewItem> and fill in:

| Field | Value |
|---|---|
| Language | `en` |
| Label | `Centre d'Information de Presse` |
| Description | `Belgian Catholic news agency (1944–2001)` |
| Aliases | `CIP` |

Click **Create**. Note the new QID (`Q…`).

## 2. Add labels in other languages

On the new item page, click **edit** in the labels box. If a language row is missing, click **All entered languages**.

| Language | Label | Description | Also known as |
|---|---|---|---|
| fr | `Centre d'Information de Presse` | `agence de presse catholique belge` | `CIP`, `agence CIP` |
| nl | `Centrum voor Informatie aan de Pers` | `Belgisch katholiek persagentschap` | `CIP`, `CIP vzw` |
| de | `Centre d'Information de Presse` | `belgische katholische Nachrichtenagentur` | `CIP` |

Click **publish**.

The English and German labels keep the French institutional name on purpose; don't invent a translated official name. Corpus-only spellings from our seed file (OCR variants, `Agentur CIP`) don't belong on Wikidata.

## 3. Add statements

For each row, scroll to **Statements**, click **+ add statement**, type the property ID, choose the value, and click **publish**.

| # | Property | Value | Qualifier |
|---|---|---|---|
| 1 | `P31` instance of | `Q192283` news agency | — |
| 2 | `P17` country | `Q31` Belgium | — |
| 3 | `P159` headquarters location | `Q239` Brussels | — |
| 4 | `P571` inception | `1944` (precision: year) | — |
| 5 | `P140` religion or worldview | `Q9592` Catholic Church | — |
| 6 | `P1448` official name | `Centre d'Information de Presse` (language `fr`) | — |
| 7 | `P1448` official name | `Centrum voor Informatie aan de Pers` (language `nl`) | — |
| 8 | `P1813` short name | `CIP` (language `fr`) | — |
| 9 | `P576` dissolved, abolished or demolished date | `31 December 2001` (precision: day) | — |

The December 2001 APIC report states that an extraordinary general assembly on 12 December 2001 decided to dissolve the association on 31 December 2001. A Moniteur belge entry would be stronger evidence if you find one.

**Do not add yet:** `P1454` legal form (association sans but lucratif / vzw). Both APIC reports call CIP an asbl, but the matching Wikidata value item has not been identified.

## 4. Add references

Under each statement, click **+ add reference** and enter these properties:
- `P854` reference URL
- `P813` retrieved: today's date
- `P1476` title (optional): language `fr` and the article title

Which source supports which statement:

| Statements | Reference URL |
|---|---|
| 1, 2, 3, 4, 5, 9 | <https://cath.ch/newsf/bruxelles-disparition-de-l-agence-de-presse-catholique-francophone-cip-a-bruxelles> (APIC, 17 December 2001: founding in 1944 after the Liberation, dissolution) |
| 1, 3, 4, 5 | <https://cath.ch/newsf/bruxelles-l-agence-de-presse-catholique-cip-a-50-ans-050694/> (APIC, 5 June 1994: founding, activities) |
| 6, 7, 8 | <https://kadoc.kuleuven.be/db/inv/927.pdf> (KADOC inventory 927, *Het Volk* management archive, p. 26, no. 256: both names and "CIP vzw") |

Before saving, open each article and check that it really states the fact you're citing.

## 5. Optional extras

- Add authority identifiers if you find records: VIAF (`P214`), ISNI (`P213`), KBR. These should be searched first; none have been confirmed.
- Link people associated with CIP from their own items (for example `P108` employer) only after confirming their QIDs: Gaston Claes, Louis Meerts, Mark Heirman, Tommy Scholtès.

## 6. Update the workbench seed

Done: the item is [Q142245483](https://www.wikidata.org/wiki/Q142245483), and the `cip` entry in `resources/newsagency_seeds.json` has its `wikidata_url`. Its status is `metadata_enriched_no_wikipedia_article`, which lets the validator accept `wikipedia_url: null`.

After a Wikipedia article is published, set `wikipedia_url`, change the status to `metadata_enriched`, add the sitelink on Wikidata, and run:

```bash
make validate-labels
```
