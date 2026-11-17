# Spanish verb lemma frequency: usable sources and redistribution

Research date: 18 November 2026. Research ticket: `app-vs7.10`. Isolated branch/worktree: `research/frequency-source`, `frequency-source-research`, base `5021892`. This report supplements [the inventory investigation](../../spanish-inventory-research/research/spanish-inventory.md). No production inventory, code, or product coverage decision was made.

## Finding and recommendation

**No inspected source is verified to satisfy all of broad Spanish coverage, actual lemma/POS frequency, distinct pronominal-entry frequency, and clear redistribution permission.** There are practical paths, with materially different compromises:

* **CORPES frequency dictionary is the strongest broad, panhispanic candidate here, conditional on permission and direct file verification.** Its documented inventory includes rare observed lemmas rather than a learner cutoff. Ask RAE for explicit permission to distribute the selected verb lemma/count derivative in an offline app, and for the current file/schema and pronominal conventions. Do not treat download availability as permission.
* **ParlaMint.ana 5.0, Spanish national parliament, is the strongest larger open corpus candidate inspected here.** The official release and Spanish header explicitly license the corpus CC BY 4.0 and provide actual token lemmas/POS. It can produce a versioned inventory in which every retained verb has an observed count. Before selecting it, a full release extraction must establish how many valid verb lemmas survive annotation cleanup and whether that coverage is sufficiently broad. Its parliamentary Spanish ranking would remain a substantial product choice.
* **UD Spanish GSD is immediately inspectable and explicitly redistributable, but its 2,513 raw observed verbal lemmas are not evidence of a fairly comprehensive Spanish inventory.** Use it for evaluating extraction/join rules or as a supplemental source if its share-alike terms are acceptable. AnCora adds useful manual annotation but still has contradictory license descriptions.

The next decision belongs to the user: pursue RAE permission for the broader panhispanic source, or evaluate the full openly licensed parliamentary corpus while accepting a genre/geographic limitation. Neither path authorizes silently replacing the requested inventory with a narrow curated list. No source here supports an exhaustive all-modern-Spanish claim.

## Candidate comparison

| Source | Actual frequency unit and verified coverage | Redistribution evidence | Status |
|---|---|---|---|
| CORPES frequency dictionary | Published lemma/category totals, separate inflected-form detail; 116,707 all-POS lemmas from 184,108,153 grammatical elements of press from 21 countries | RAE general notice reserves rights; no dataset-specific open grant verified | Broad candidate, permission-dependent; live TSV not inspected |
| ParlaMint.ana 5.0 ES | Token-level automatic lemma + UD POS; Spanish header reports 19,645,025 words, 2015-01–2023-02; small official samples inspected | Release and Spanish header both CC BY 4.0 | Usable annotated corpus; full verb-lemma coverage still unmeasured |
| UD Spanish GSD r2.18 | Counted all three splits: 431,478 integer-ID syntactic words; 36,352 VERB + 10,754 AUX occurrences; 2,513 distinct raw lemmas | Release LICENSE explicitly CC BY-SA 4.0 | Verified extraction fallback, limited coverage and automatic lemmas |
| UD Spanish AnCora r2.18 | Counted all three splits: 560,137 integer-ID syntactic words; 48,181 VERB + 13,571 AUX occurrences; 2,370 distinct raw lemmas | LICENSE CC BY 4.0 contradicts README inherited GNU wording | Technically usable; license discrepancy remains unresolved |

CORPES counts and corpus composition are from [the resource creator's paper, §§2–3/table 6](https://revistas.udc.es/index.php/rlex/article/view/11847/g11847_pdf). ParlaMint facts are from [the official 5.0 deposit](https://www.clarin.si/repository/xmlui/handle/11356/2005), [release statistics](https://github.com/clarin-eric/ParlaMint/blob/v5.0/Build/Metadata/ParlaMint-overview-stats.tsv), and [Spanish corpus header](https://github.com/clarin-eric/ParlaMint/blob/v5.0/Samples/ParlaMint-ES/ParlaMint-ES.ana.xml). UD figures are fresh local counts of the linked release files below, not current website totals. They include raw annotation artifacts, not a cleaned set of legitimate Spanish verbs.

## CORPES: documented schema resolved, live bytes and permission unresolved

The [official frequency guide, §3](https://www.rae.es/corpes/assets/rae/files/corpes/guiaDiccionariosFrecuenciasLex.pdf) documents two structures:

* Dispersion list: dispersion rank, frequency rank, lemma, class, DP, frequency, normalized frequency, countries.
* Alphabetical dictionary: order, frequency rank, lemma/form, class, frequency, normalized frequency, DP, countries. Lemma rows are followed by indented form rows. Its examples have class `V` on lemma rows and longer morphological labels on their forms. Extracting every row beginning with V would therefore count lemma totals and their constituent forms twice.

The guide's `abalanzar` example puts clitic-associated forms under a base lemma; this supports a base-lemma interpretation for that example, not a verified universal rule for every pronominal verb. The creator explicitly says `ser` totals include auxiliary uses (paper footnote 14). That establishes that auxiliary usage is represented; this resource does not require a UD `AUX` filter.

The [official alphabetical TSV URL](https://www.rae.es/corpes/assets/rae/files/corpes/diccionario_frecuencias_corpes_alfa.tsv) was reachable only far enough for the web reader to reject its TSV content type. Direct Python HTTPS requests returned HTTP 403, including a browser user-agent/referer retry. Consequently **the current byte-level header, row count, exact verb lemma count, release identity/hash, and complete pronominal behavior remain unverified**. The PDF guide documents CSV names and must not be mistaken for inspection of today's TSV export.

[RAE's legal notice, §4](https://www.rae.es/aviso-legal) prohibits commercial reproduction, distribution, extraction and reuse without prior written authorization and disclaims an implied license. No overriding dataset permission was found. A permission request should specify a downloadable offline derived verb/count table, commercial/noncommercial distribution, retained attribution, updates, and whether base counts can be displayed against pronominal entries. This report does not infer that all factual counts are legally restricted in every jurisdiction; it records the absence of a verified redistribution grant for this artifact.

## ParlaMint: larger open option with a measurable but uncounted lexical boundary

The [5.0 release deposit](https://www.clarin.si/repository/xmlui/handle/11356/2005) provides annotated TEI, derived CoNLL-U and vertical formats. Its Spanish national-parliament archive is roughly a gigabyte, so only the small official samples/header and statistics were downloaded here. The header identifies UDPipe 2 with `spanish-ancora-ud-2.10-220711` for POS, lemmatization and dependencies. An automatic analyzer trained on AnCora is a different artifact from redistributing AnCora's original annotated texts; the corpus itself has explicit CC BY terms. This does not establish perfect annotation accuracy.

Three [official Spanish sample files](https://github.com/clarin-eric/ParlaMint/tree/v5.0/Samples/ParlaMint-ES) contain 70 VERB and 14 AUX nodes in total. Example: `reanuda` has lemma `reanudar`, POS `VERB`; a separate `se` node is a pronoun. XML `w` container nodes can lack POS and contain component nodes, so use terminal annotated words or integer-ID CoNLL-U rows rather than counting every XML `w`. The sample includes `estáis` with inconsistent singular metadata: a concrete reminder that automatic features are not ground truth. These samples demonstrate schema, not lexical breadth or independent pronominal counts.

**Implementation implication, not a selected policy:** derive counts from the full Spanish release using observed `(lemma, VERB/AUX)` tokens, retaining all valid observed lemmas without a top-N cutoff. Record the annotation cleanup rules and exclusions. Store per-POS subtotals and their sum; order by the combined count. Compute normalized rates against a documented denominator from those same files, not the rounded overview size. Do not add unobserved dictionary lemmas and call them ranked. Do not add multilingual regional corpora without checking language labels.

The [CC BY 4.0 terms](https://creativecommons.org/licenses/by/4.0/) permit redistribution and adaptations, including commercially, with appropriate credit, a license link and change indication, and no added restrictions on licensed material. Preserve release/header attribution in an offline notice alongside any derivative table. This is clear affirmative permission, unlike free access alone.

## UD inspection: auxiliaries, pronominal identity, noise, and licenses

Official sources: [GSD r2.18 README](https://github.com/UniversalDependencies/UD_Spanish-GSD/blob/r2.18/README.md), [GSD LICENSE](https://github.com/UniversalDependencies/UD_Spanish-GSD/blob/r2.18/LICENSE.txt), [AnCora r2.18 README](https://github.com/UniversalDependencies/UD_Spanish-AnCora/blob/r2.18/README.md), [AnCora LICENSE](https://github.com/UniversalDependencies/UD_Spanish-AnCora/blob/r2.18/LICENSE.txt). The [GSD owner page](https://universaldependencies.org/treebanks/es_gsd/index.html) labels its lemmas automatically assigned and not manually checked. The [AnCora page](https://universaldependencies.org/treebanks/es_ancora/index.html) describes manual non-UD annotation converted to UD. r2.18 was deliberately pinned for reproducibility; current website pages already link UD 2.19 and are not the source of these measured counts.

| Pinned release | ser VERB / AUX | estar VERB / AUX | haber VERB / AUX | Raw singleton lemmas |
|---|---:|---:|---:|---:|
| GSD r2.18 | 938 / 6,951 | 420 / 861 | 426 / 1,821 | 968 |
| AnCora r2.18 | 0 / 6,223 | 318 / 1,333 | 693 / 4,183 | 682 |

A VERB-only filter would entirely lose `ser` from this AnCora release. Aggregate both tags by lemma; retain their provenance. Raw GSD contains foreign/noisy verb labels, so the number 2,513 must not be presented as a verified Spanish dictionary count. Ending-in-infinitive filtering alone is not a sufficient quality policy.

Both inspected releases have **zero VERB/AUX lemmas ending in `se`**. GSD has `arrepentir` 3 times and `ir` 320; AnCora has `arrepentir` 8 and `ir` 577. AnCora's changelog explicitly records removing reflexive `se` from lemmas in v2.18. A concrete AnCora sentence has `se` as a separate `PRON`, `expl:pv` dependent of `arrepiente`, lemma `arrepentir`.

**Join conclusion:** corpus base-lemma counts can be attached to a lexical record such as `arrepentirse` through an explicit alias (`arrepentirse → arrepentir`), with frequency scope marked “base lemma.” The count for `ir` is not an independently measured frequency for `irse`; copying it to two separate ranked entries would invent evidence and duplicate totals. A distinct pronominal frequency would require a separately specified construction count based on dependency/clitic annotation, validated against ordinary reflexive, passive and impersonal uses. No inspected source establishes distinct counts for every such entry.

GSD's release license is unambiguous CC BY-SA 4.0. [Those terms](https://creativecommons.org/licenses/by-sa/4.0/) require attribution/change notices and share-alike for adaptations; preserve an appropriate licensed derivative-data artifact and avoid assuming this automatically licenses unrelated app code. AnCora's release LICENSE is affirmatively CC BY 4.0, but its same-release README still says inherited GNU and refers questions to the University of Barcelona. Attempts to retrieve the original provider page timed out. **The contradiction is confirmed at artifact level, not resolved by preferring GitHub's license badge.** Obtain provider clarification before making it the chosen redistribution basis.

## Reproducibility and limits

Real shell and web tools were verified. Sandbox network DNS failed; approved read-only network calls downloaded files into `/tmp/frequency-inspection`. No raw corpus was added to the worktree. UD counts read train/dev/test for both repos at tag `r2.18`, with URLs of the form `https://raw.githubusercontent.com/UniversalDependencies/UD_Spanish-GSD/r2.18/es_gsd-ud-train.conllu` (likewise dev/test and `UD_Spanish-AnCora/es_ancora`). Count rule:

```python
from collections import Counter
counts = Counter()
for line in corpus_text.splitlines():
    if not line or line.startswith('#'):
        continue
    fields = line.split('\t')
    if fields[0].isdigit() and fields[3] in {'VERB', 'AUX'}:
        counts[fields[2]] += 1
```

Integer IDs exclude multiword container rows and empty nodes. Counts use raw lemma spelling without lowercasing or lexical cleanup. Train/dev/test were pooled for descriptive frequency, not model evaluation. SHA-256 of downloaded UD files:

| File | SHA-256 |
|---|---|
| GSD train | `9e527de0e45dca4a8ef00105a3ebd102da941964b35f01916a6baa6288130f7b` |
| GSD dev | `704fb19afc0a34cff476e1a70351b7026c4364f862e8e8388b02873852567c22` |
| GSD test | `ecce253f44bffaa9803ae7ec0c10911c13e4f1fc3cb439dbd1db2cebe0a12741` |
| AnCora train | `47b6fc49d6ed48a016e7fa5ad9f5c7ecf3ec21e9db005df3ea14d10f07c6deb6` |
| AnCora dev | `1a132068062edf2654fb45b41cd4c59ba7e5c18e7c5f642ed5a9cc351fd9f0fe` |
| AnCora test | `679f1c05ca654aa26801c80319df45f8f97606718fb534b91755b48f3e67fa6f` |

ParlaMint samples were from tag `v5.0`, paths `Samples/ParlaMint-ES/{2017,2020,2023}/ParlaMint-ES_{2017-11-28-CD171128,2020-11-12-CD201112,2023-02-23-CD230223}.ana.xml`. Their SHA-256 values respectively are `b3b4ff1691625937fd08bdc8277bca4796c743eb3c9192dc08cd4acdeb22a5ca`, `729d38b5835fca41b7739db60744fe95c40ff7c30cc0260699587c738d731918`, and `71c9dd8303741c44fdaf764c44c81c5154ecc0658f6df635654e7bc908060a77`.

This was a small candidate comparison, not an exhaustive source or verb search. Full ParlaMint extraction and CORPES permission/file verification remain concrete follow-on work after the product/source decision. Surface-infinitive lookups in word-frequency lists would not resolve these gaps: they do not disambiguate and aggregate a verb's inflections. No external permission request was sent.
