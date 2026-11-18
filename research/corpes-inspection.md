# CORPES verb frequency inspection

Research date and user-confirmed download date: **18 November 2026**. Ticket: `app-vs7.11`. Worktree: `corpes-inspection-research`, branch `research/corpes-inspection`, base `5021892`. Research skill applied by delegated research agent. This supersedes the earlier blocked inspection; [candidate-source research](../../frequency-source-research/research/frequency-source.md) remains background, not the source of the measurements below.

## Result

**The actual CORPES frequency dictionary supports a broad, fully measured inventory.** It contains **10,399 distinct V lemma records**, all with positive counts. A conservative deterministic shape filter proposes **10,291 candidate verb entries**, including **285 native pronominal-style entries with their own recorded lemma totals**, while quarantining ambiguous grouped labels and non-infinitive labels. This is a corpus-defined candidate inventory, not a claim that every annotation is linguistically correct or that every modern Spanish verb is present.

The user selected one shared overall ranking: descending aggregate verb-lemma frequency, alphabetical ties; regional settings affect forms only. Retain each candidate's own native count. Do not split grouped counts, copy base counts to pronominal entries, or add unmeasured dictionary verbs. **`arrepentirse` has its own count, 1,451; `irse` has no lemma record and is ineligible under the user's rule.** No production inventory was generated. Permissions remain outside this task.

## Pinned input and schema

User-supplied original local file: `input/diccionario_frecuencias_corpes_alfa.tsv`, downloaded normally from the [current official RAE link](https://www.rae.es/corpes/assets/rae/files/corpes/diccionario_frecuencias_corpes_alfa.tsv). The [RAE CORPES page](https://www.rae.es/banco-de-datos/corpes-xxi) links directly to this resource.

- Size: **34,995,792 bytes**.
- SHA-256: `16203075050080abd4e5eabe35db5723bc74563707ea62244e48d94ba17d38cb`.
- Encoding: UTF-8, no BOM; CRLF endings; 620,865 physical lines; final DOS EOF character `0x1a`.
- First line explicitly states CC BY-SA 4.0. This corrects the earlier investigation's incomplete knowledge of the file header; no rights assessment or permission action is part of this task.
- Line 3 contains nine tab-separated column names: `Orden`, `Rango frec.`, `Lema`, `Forma`, `Etiqueta`, `Frec.`, `Frec. norm.`, `DP`, `Núm. países`.

Whitespace padding is presentation. A lemma row has nonempty `Orden`, `Rango frec.`, `Lema`, empty `Forma`, and a one-letter class. Following detail rows have empty first three fields, a form in `Forma`, and a longer morphological tag. **Use exact `Etiqueta == V` on lemma rows; never all tags starting V.** Count the lemma total once and use detail only for verification.

The file itself has no explicit publication/version/date field beyond its notice and header. Pin this exact artifact by download date/hash. RAE's general corpus is currently 1.5; that must not be used as this dictionary's data-release label. The [official guide](https://www.rae.es/corpes/assets/rae/files/corpes/guiaDiccionariosFrecuenciasLex.pdf) and [creator's account](https://revistas.udc.es/index.php/rlex/article/view/11847/g11847_pdf) identify the dictionary as press from CORPES 1.0 across 21 countries. Fresh totals confirm 116,707 lemma starts and 184,108,153 aggregate occurrences across all classes, matching the published scope.

There is an important format defect: **16 numeral (M) lemma records and associated detail have line wrapping or incomplete physical rows**. There are 48 malformed nonblank physical lines altogether; 116,691 lemma rows are complete, plus the 16 partial numeral lemma starters. Their available counts sum to 18; complete-row counts sum to 184,108,135. All verbal lemma rows are complete, and all their form sums verify. The script isolates malformed rows and permits malformed lemma starters only when explicitly M; it does not silently reconstruct them or treat continuations as verbs. Some unrelated complete form rows have blank form strings. The EOF marker is ignored, not parsed as a row.

## Measured verb coverage, ties and auxiliaries

| Measurement | Result |
|---|---:|
| Exact V lemma rows / distinct verbal lemma strings | 10,399 / 10,399 |
| Duplicate verbal identities | 0 |
| Nonpositive or missing V frequencies | 0 |
| Sum of native V lemma frequencies | 25,063,834 |
| Minimum / maximum count | 1 / 3,152,747 |
| Native V singletons / count-two entries | 2,333 / 873 |
| Distinct native V frequency values | 2,090 |
| Equal-count groups containing multiple V lemmas | 629 |
| V lemmas participating in those ties | 8,938 |
| V totals disagreeing with sum of detail rows | 0 |

The published frequency-rank column is an all-class rank and assigns different ranks even to equal counts: count-two entries `abacorar` and `abarajar`, for example, have ranks 77,240 and 87,535. **Recompute the user's verb-only order from integer `Frec.` and alphabetical ties**, rather than reusing the published rank. Alphabetical ordering is a secondary display key, not evidence of a frequency difference. A deterministic Unicode lexical key on the retained source strings is sufficient for a reproducible prototype; if Spanish locale collation is desired later, specify it explicitly rather than inheriting an operating-system default.

| Native V lemma | Absolute total | Detail rows | Detail sum | Input line |
|---|---:|---:|---:|---:|
| ser | 3,152,747 | 86 | 3,152,747 | 539045 |
| estar | 812,249 | 68 | 812,249 | 241352 |
| haber | 445,382 | 68 | 445,382 | 290111 |
| ir | 264,124 | 63 | 264,124 | 333120 |

Noun homographs also occur, including `ser`, `haber` and `ir`; the exact V class excludes them. The creator explicitly includes auxiliary uses in `ser` (paper footnote 14). The actual dictionary includes auxiliary-capable verbs under V; it does not provide separate UD-style AUX lemma totals. These are total frequencies for the source-defined verbal lemmas, not counts only of their auxiliary functions.

## Own pronominal records: available, but annotation is not sense validation

There are **285 single infinitive-shaped `-se` lemma records**, with combined frequency **25,866**; **72** are singletons. **24** have a separately recorded base spelling as well; the remaining 261 do not. These counts exclude three ambiguous pipe labels ending in `-se`.

| Native lemma | Own count | Detail rows / sum | Native base record |
|---|---:|---:|---|
| arrepentirse | 1,451 | 40 / 1,451 | arrepentir absent |
| adentrarse | 2,478 | 47 / 2,478 | adentrar absent |
| abrumarse | 559 | 21 / 559 | abrumar 25 |
| debatirse | 5,104 | 34 / 5,104 | debatir 199 |
| irse | absent | absent | ir 264,124 |

These are independently recorded native lemma totals, not aliases assigned the base's number. However, **the TSV does not establish that each total measures exclusively the semantic pronominal sense**. For example, `abrumarse` contains finite and participial forms such as `abruma` and `abrumado`, while `abrumar` has only two nonfinite detail records with enclitic-marked morphology. `debatirse` similarly contains ordinary finite/participle forms while `debatir` has two nonfinite detail records. Contexts and disambiguation decisions are absent. This can reflect source annotation conventions/errors; no semantic reclassification was attempted.

The concrete proposal is therefore to accept the source's explicitly named lemma identities and own measured totals, with this corpus-annotation limitation, then perform the already planned downstream content checks. Do not claim the pronominal records are independently validated sense frequencies. If the user requires semantic pronominal-only counts rather than native named-lemma counts, this file cannot prove that stronger property; a separate contextual analysis would be required. No shared-frequency fallback is proposed for missing entries.

## Exact proposed candidate filter and exclusions

Apply these deterministic rules to the pinned file:

1. Strip surrounding field padding, retain source spelling/accents; select structurally complete native lemma rows with empty `Forma`, exact class V and positive integer `Frec.`.
2. Retain a single lowercase infinitive spelling, optionally ending in `se`, matching this full regular expression: `(?:ir|[a-záéíóúüñ]+(?:-[a-záéíóúüñ]+)*(?:ar|er|ir|ír))(?:se)?`.
3. Quarantine every rejected source label rather than inventing, merging, splitting or reallocating counts. Preserve the one hyphenated candidate `post-producir` (count 6) as its source identity; do not silently normalize it to another spelling.
4. Keep rare/regional entries and count-one entries; no arbitrary frequency floor or learner cap. Sort by descending integer count, then the explicit alphabetical key. Keep pronominals only when their own native record passes the same filter.

This yields **10,291 candidates**: **10,006 nonpronominal spellings + 285 native `-se` spellings**, combined count **25,063,537**, including **2,247 singletons**. Shape is a conservative mechanical screen, not a dictionary correctness test.

The **108 excluded labels** consist of:

- **4 grouped alternatives**, each count 1: `debatir|debatirse`, `encallar|encallarse`, `enrocar|enrocarse`, `reverter|revertir`. Their aggregate count is not independently attributable to either alternative. Never split or copy it.
- **104 labels without single-infinitive shape**, combined count 293. Examples include `cf.` (80), `cfr.` (63), `verbo` (2), inflected `está` (1), participial `acaserados` (2), and multiword `háyase visto` (1). Do not infer their correct target lemma and inflate its measured total.

Rare accepted examples include `abalizar` and `abaluartar`, each count 1. Some rare items or annotations may be mistakes, but rarity itself is insufficient evidence to discard them. Form detail also contains suspicious strings under common lemmas (`aclara-es` under `ser`, for example), so exact corpus counts should not be presented as error-free language truth. The bounded inspection does not exhaustively validate 10,291 lexical entries.

## Reproduce and task status

Run from this worktree:

```bash
python research/inspect_corpes.py input/diccionario_frecuencias_corpes_alfa.tsv
```

The read-only script rejects an unexpected file hash/header, verifies unique positive V totals and every verbal form sum, then prints aggregate statistics and a few identity probes. It generates no production data. The original TSV remains a user-supplied untracked input; do not commit or publish it as part of this report.

Earlier automated download attempts received Cloudflare HTTP 403 browser challenges; the web reader rejected TSV/ZIP media types. The user's normal download resolved that technical blocker. No access controls were bypassed. The bounded investigation is now answered. The parent independently ran the script and verified header/raw counts, and will use source-assigned native lemma counts for the coverage policy without a semantic-purity guarantee. The 10,291 remain candidates requiring downstream linguistic validation, not an approved production lexicon. No remaining source-access question blocks that coverage review. No production code, external messages, commits, pushes or remote sync were performed.
