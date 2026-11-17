# Spanish verb inventory and frequency sources

Research date: 17 November 2026. Scope: evidence for a complete modern-Spanish verb reference, including regional and rare forms; this report does not select product coverage or a dataset license policy. The requested result is a complete lemma inventory ordered by frequency, not a selected learner vocabulary. Generation independently checked by two LLMs remains the user's stated content policy; consulting the sources below does not introduce a requirement for reference-by-reference validation.

Reproducibility: isolated worktree `spanish-inventory-research`, branch `research/spanish-inventory`, base commit `5021892`; report is uncommitted. Web sources were inspected on the research date. Exact dataset revisions were not pinned and no dataset was selected or imported.

## What “complete” can mean

**Analytical distinction:** paradigm completeness means accounting for a verb's grammatical slots and permitted alternatives, including genuinely unavailable slots. Lexical completeness means accounting for the verb lemmas within a defined language boundary. Neither implies the other. A resource can generate every supported form of a small lemario, while a large dictionary can omit whole inflection tables. An unqualified claim to contain every possible modern Spanish verb is not established by any source inspected here.

**Source fact:** the current DLE preamble identifies its remit as the general lexicon and describes the 24th edition as designed originally for electronic publication. This is a stronger current-edition source than older pages still describing the 23rd edition. It does not claim an exhaustive inventory of all productive, specialized, regional, and newly coined verbs. [RAE–ASALE, 24th-edition preamble](https://www.asale.org/sites/default/files/2026-10/Pre%C3%A1mbulo.pdf).

**Inference:** an operationally complete list requires a declared, versioned lemma boundary, retention of every lemma within it, and an explicit account of additions and exclusions. Frequency cannot supply the missing boundary: a finite corpus can leave legitimate lemmas unattested. Zero measured occurrences and absence from a frequency table must remain distinguishable from nonexistence.

## The grammatical inventory

### Finite simple and compound tenses

The following compact inventory follows the academic model tables; examples use first-person singular. There are **10 indicative and 6 subjunctive tense categories**. The -ra/-se series are alternatives within one tense. [RAE–ASALE, conjugation models](https://www.rae.es/dpd/ayuda/modelos-de-conjugacion-verbal). Conditional belongs to indicative. [RAE–ASALE, GTG *condicional simple*](https://www.rae.es/gtg/condicional-simple).

| Mood | Simple tense | Example | Compound counterpart | Example |
|---|---|---|---|---|
| Indicative | Presente | amo | Pretérito perfecto compuesto | he amado |
| Indicative | Pretérito imperfecto | amaba | Pretérito pluscuamperfecto | había amado |
| Indicative | Pretérito perfecto simple | amé | Pretérito anterior | hube amado |
| Indicative | Futuro simple | amaré | Futuro compuesto | habré amado |
| Indicative | Condicional simple | amaría | Condicional compuesto | habría amado |
| Subjunctive | Presente | ame | Pretérito perfecto compuesto | haya amado |
| Subjunctive | Pretérito imperfecto | amara / amase | Pretérito pluscuamperfecto | hubiera / hubiese amado |
| Subjunctive | Futuro simple | amare | Futuro compuesto | hubiere amado |

Nonfinite inventory: infinitive **amar**, compound infinitive **haber amado**; gerund **amando**, compound gerund **habiendo amado**; participle **amado**. [RAE–ASALE, GTG *forma no personal*](https://www.rae.es/gtg/forma-no-personal). Affirmative imperative: **ama / amá; amad**. [RAE–ASALE, conjugation models](https://www.rae.es/dpd/ayuda/modelos-de-conjugacion-verbal).

**Counting inference:** this gives 16 finite tense categories before imperative, with six grammatical person/number slots each for an ordinary personal verb. This is a category count, not a claim of 96 different strings: syncretism, alternatives, regional systems and defectivity change string counts. There is no personal infinitive paradigm comparable to Portuguese, nor a separate modern synthetic passive paradigm in this inventory.

Academic/Bello aliases include copretérito, pospretérito and antepresente; they do not add categories. [RAE–ASALE, conjugation models](https://www.rae.es/dpd/ayuda/modelos-de-conjugacion-verbal).

### Subject systems and imperatives

**Source facts:** usted and ustedes refer to addressees but govern third-person singular and plural verb agreement. Thus **usted habla**, **ustedes hablan**; addressee role and morphological person are different dimensions. [RAE–ASALE, *usted*](https://www.rae.es/dpd/usted).

**Synthesis:** the ordinary subject mapping to consider is yo; tú; vos; él/ella/usted; nosotros/nosotras; vosotros/vosotras; ellos/ellas/ustedes. Feminine and masculine subject labels do not create different ordinary finite verb endings. [RAE–ASALE, tonic personal pronouns](https://www.rae.es/dpd/pronombres%20personales%20t%C3%B3nicos). The ustedes system serves familiar as well as respectful plural address in America, the Canaries and part of Andalusia. [RAE–ASALE, *usted*, §4](https://www.rae.es/dpd/usted).

Commands require polarity and addressee/exhortation coverage, even where their forms are borrowed from subjunctive:

| Target | Affirmative example | Negative example |
|---|---|---|
| tú | habla | no hables |
| vos | hablá | no hables / no hablés, depending on variety |
| usted | hable | no hable |
| nosotros/as, exhortation | hablemos | no hablemos |
| vosotros/as | hablad | no habléis |
| ustedes | hablen | no hablen |

UCM explicitly identifies present-subjunctive first-person plural and third-person forms used imperatively, and subjunctive forms in negative commands. There is no ordinary first-person singular command cell. The command table is a synthesis of that account and the regional evidence below. [Universidad Complutense, personal forms and uses](https://www.ucm.es/plataformaele/formas-personales-usos-mas-importantes).

### Voseo is a family of paradigms

The DPD distinguishes **vos + voseo**, **tú + voseo**, and **vos + tuteo**. American vos uses clitic **te**; reverential vos takes plural agreement. Representative contrasts follow, not national universals. [RAE–ASALE, *voseo*, §§1–2](https://www.rae.es/dpd/voseo).

| Pattern to account for | Concrete forms |
|---|---|
| Rioplatense and much Central American present/imperative | cantás, comés, vivís; cantá, comé, viví |
| Subjunctive variation | cantes / cantés; comas / comás; vivas / vivás |
| Chilean present/subjunctive | cantái(s), comí(s), viví(s); cantí(s), comái(s), vivái(s) |
| Chilean additional tenses | cantabai(s), cantaríai(s), cantarai(s); less frequent future cantarí(s) |
| Diphthong-preserving varieties, including Zulia/Panama patterns | cantáis, coméis; cantaréis alongside regional cantarés |
| Attested preterite alternatives | cantaste / cantastes; Colombian cantates |

The DPD marks register/prestige differences, declining/rural forms, and generally disfavored **-s** preterites. Non-Chilean voseo usually shares imperfect/conditional tuteo forms. Its geographic table and notes provide the finer distributions. [RAE–ASALE, *voseo*, country table and notes](https://www.rae.es/dpd/voseo).

**Inference:** a locale flag cannot reliably imply one national paradigm. Regional location, social/register label, pronoun choice and tense-specific verb pattern may vary independently. The table is an evidence map, not an exhaustive sociolinguistic atlas; exact local distributions remain a question for any chosen coverage boundary.

### Rare modern, archaizing, and historical forms

**Pretérito anterior** remains a modern written, especially literary, tense; it is rare outside that register. It often occurs after immediate-sequence expressions, and can alternate with the simple preterite. Constructed contrast: **Apenas hubo terminado, salió** / **Apenas terminó, salió**. It should not be silently equated with a historical-only form. [RAE–ASALE, GTG *pretérito anterior*](https://www.rae.es/gtg/pret%C3%A9rito-anterior).

**Simple future subjunctive** survives as archaizing legal/administrative language and in fixed expressions, ritual formulas and proverbs. Depending on construction, present subjunctive, imperfect subjunctive, or present indicative commonly replaces it. Constructed contrast: **quien quisiere** / **quien quiera**. [RAE–ASALE, GTG *futuro simple de subjuntivo*](https://www.rae.es/gtg/futuro-simple-de-subjuntivo).

**Compound future subjunctive** has fallen out of general use; the GTG restricts current attestations to legal/administrative documents and illustrates replacement by pluscuamperfecto subjunctive. Constructed contrast: **si hubiere presentado** / **si hubiera presentado**. [RAE–ASALE, GTG *futuro compuesto de subjuntivo*](https://www.rae.es/gtg/futuro-compuesto-de-subjuntivo).

Historical or archaizing possibilities must not become unlabelled ordinary cells. For example, auxiliary **habemos** is archaic outside special uses, and historical possessive **haber** and imperative **habe/habed** do not have ordinary contemporary use. Impersonal present **hay** is distinct from auxiliary **ha**. [RAE–ASALE, *haber*, §§1–3](https://www.rae.es/dpd/haber).

### Alternatives, clitics and pronominal lemmas

Some verbs have genuine alternate realizations: **adecuo / adecúo** are both valid accentuation patterns. Such variation needs a set of alternatives, not an arbitrary replacement of one accepted form by another. [RAE–ASALE, *adecuar(se)*](https://www.rae.es/dpd/adecuar).

**Freír, imprimir, proveer** have the participle pairs **freído/frito**, **imprimido/impreso**, **proveído/provisto**; both members can serve in compound tenses and passives, while adjectival preferences differ. An apparently related adjective is not automatically a verbal participle. [FundéuRAE, double-participle guidance](https://www.fundeu.es/recomendacion/dobles-participios-frito-freido-etc-claves-de-redaccion/).

**Ir(se)** supplies a useful exception cluster: **idos / iros** are accepted plural pronominal commands; **vamos / vayamos** differ in current exhortative frequency; voseante commands use **andá / andate** rather than mechanically generating an imperative from *ir*. These are context-sensitive alternatives. [RAE–ASALE, *ir(se)*, §§1–2](https://www.rae.es/dpd/ir).

The DPD distinguishes obligatory pronominal verbs such as **arrepentirse**, pronominal senses of verbs such as **irse**, ordinary reflexive/reciprocal constructions, expressive **se**, impersonal **se**, and passive **se**. The last two are constructions, not additional lemma-wide inflection paradigms: **se trabaja** versus **se venden casas** illustrates the agreement distinction. [RAE–ASALE, *se*, §§1–2](https://www.rae.es/dpd/se).

Clitic placement affects displayed strings: **me arrepiento**, **arrepentirse**, **arrepintiéndose**, **arrepiéntete**, **no te arrepientas**. Affirmative commands attach clitics; negative commands put them before the verb. Infinitives and gerunds attach them; many periphrases permit placement on either verb. Orthographic adjustments include **sentemos + nos → sentémonos** and **sentad + os → sentaos**. [RAE–ASALE, *pronombres personales átonos*, §§2–3](https://www.rae.es/dpd/pronombres%20personales%20%C3%A1tonos).

**Inference:** pronominal lemma identity, nonpronominal lemma identity, and a freely added object clitic cannot be conflated when constructing either a complete lemario or frequency joins. The six-person ordinary reflexive sequence is **me, te, se, nos, os, se**, with vos using te and ustedes se. A compound pronominal example is **me he arrepentido**, not an enclitic attached to the participle.

### Defective and impersonal paradigms

**Balbucir** lacks first-person singular present indicative and present subjunctive; **balbucear** supplies those meanings. This is an unavailable-form case, not a reason to invent regular-looking cells. [RAE–ASALE, *balbucir*](https://www.rae.es/dpd/balbucir).

**Soler** has a restricted tense distribution: present and imperfect forms are most common; compound forms are rare; future, conditional and imperative are not used. [RAE–ASALE, *soler*](https://www.rae.es/dpd/soler).

**Abolir** illustrates the opposite problem: it was traditionally called defective, but the current DPD accepts its full regular paradigm, including **abolo, aboles**. Old defectivity lists can therefore be wrong for current coverage. [RAE–ASALE, *abolir*](https://www.rae.es/dpd/abolir).

**Llover** normally has third-singular and nonfinite weather uses, but personal uses exist, including plural figurative subjects. Missing-person claims depend on sense and construction. [RAE–ASALE, *llover*](https://www.rae.es/dpd/llover). Similarly, impersonal existential haber and fully personal auxiliary haber require separate usage constraints. [RAE–ASALE, *haber*](https://www.rae.es/dpd/haber).

**Inference:** distinguish grammatical absence, ordinary-use restriction, rare attestation, historical-only form, and missing data. A dash cannot communicate all five reliably. Neither an all-slots regular generator nor an old defective-verb whitelist alone establishes completeness.

### Full paradigms, constructions, and English glosses

**Source-grounded distinction:** haber + participle creates the compound tenses; haber de / haber que + infinitive are periphrases. [RAE–ASALE, *haber*, §3](https://www.rae.es/dpd/haber). **Ir + gerund** is also explicitly treated as a periphrasis, expressing development. [RAE–ASALE, *ir(se)*, §4](https://www.rae.es/dpd/ir). Passive **ser + participle** and passive **se** have their own constructional behavior. [RAE–ASALE, *se*, §2](https://www.rae.es/dpd/se).

**Analytical consequence:** progressive **estar hablando**, prospective **ir a hablar**, obligation **tener que hablar**, habitual **soler hablar**, and passive **ser amado** are not additional synthetic tense labels. They can themselves be inflected or combined, so “all verb phrases” is not a finite table equivalent to the tense inventory. Their inclusion is a separate coverage decision.

English glosses need context. UCM documents habitual/historical/future uses of present, probability uses of future and conditional, and temporal flexibility in subjunctive forms. [UCM, personal forms and uses](https://www.ucm.es/plataformaele/formas-personales-usos-mas-importantes).

**Illustrative translations, not exclusive equivalences:** *hablo* can be “I speak” or contextual “I am speaking”; *hablaba*, “I was speaking” or “I used to speak”; *serán las seis*, “it must be about six”; *dijo que vendría*, “said they would come”; *cuando venga*, “when they come,” without an English subjunctive-looking form. *Fui* also needs lemma context (ser/ir), and *hablamos* needs tense context (present/preterite). A complete list of English glosses cannot be derived by matching tense names one-to-one; subject, sense, construction, dialect and surrounding time expressions matter.

## Sources for the complete lemma inventory and ordering

### RAE DLE, CORPES and CREA

| Source | What it establishes | What it does not establish |
|---|---|---|
| DLE | Versioned general-lexicon dictionary, with grammatical information | Every possible modern verb; bulk redistribution permission; corpus frequency rank |
| CORPES | Contemporary panhispanic corpus, lemma/category search, downloadable result inventories | Exhaustive lexical universe; automatic permission to republish source data |
| CREA | Late-20th-century comparative corpus | A current-usage ordering by itself |

DLE's general-lexicon remit is explicit in the current preamble. No verified current count of **verb lemmas** or verified open bulk lemario license was found; total dictionary entry counts would not answer the verb question. [RAE–ASALE, DLE preamble](https://www.asale.org/sites/default/files/2026-10/Pre%C3%A1mbulo.pdf).

CORPES version **1.5, June 2026**, has nearly **420,000 documents** and **455 million orthographic forms**, according to its owner. It covers written and transcribed oral material; the interface offers inventories by lemma, form and category with absolute/normalized frequency and download support. These figures describe the current corpus, not the frequency-dictionary subset. [RAE, CORPES XXI](https://www.rae.es/banco-de-datos/corpes-xxi).

The downloadable frequency dictionary released with CORPES 1.1 is based on **press texts from 21 countries in CORPES 1.0**, after exclusions, totaling **184,108,153 grammatical elements** and **116,707 lemmas across word classes**. Its creator describes lemma/POS information, absolute/normalized frequency and dispersion; those counts are not Spanish-verb counts. This is a substantial full observed inventory rather than merely a top-N learner list, but its press-only sampling is material. [Guillermo Rojo, first-party account, §§2–3 and table 6](https://revistas.udc.es/index.php/rlex/article/view/11847/g11847_pdf).

The current CORPES page links directly to an [alphabetical frequency TSV](https://www.rae.es/corpes/assets/rae/files/corpes/diccionario_frecuencias_corpes_alfa.tsv). The web reader rejected its tab-separated content type, so its actual header, current row count, verb filtering and pronominal-lemma treatment were **not inspected**. The JavaScript [country-lemma page](https://www.rae.es/corpes/contenidos/lemas-pais) returned no readable content. A prose description or an old table cannot verify the current downloadable file's exact schema.

CORPES's guide distinguishes orthographic words from grammatical elements (clitics can be separate elements), supports lemma and grammatical-category queries, and specifies that canonical-lemma search retrieves morphological/flexive/graphical variants. This makes category and tokenization choices essential when interpreting a rank. [RAE, basic query guide](https://www.rae.es/corpes/assets/rae/files/Gu%C3%ADa_de_uso.pdf).

CREA's official page identifies version 3.2 (June 2008), over 160 million forms, and texts from **1975–2004**. Its older period is useful for comparison but should remain visible in any frequency provenance. [RAE, CREA](https://www.rae.es/banco-de-datos/crea).

**Permission facts, not legal advice:** RAE's general notice reserves rights, says no license is implied, and requires prior written authorization for commercial reproduction, distribution, extraction and reuse of its content. Downloadability and free consultation therefore do not establish an open redistribution grant for the DLE or CORPES outputs. No dataset-specific permission overriding that notice was verified in this research. Whether a particular intended use is permitted remains unresolved. [RAE, legal notice, §4](https://www.rae.es/aviso-legal).

### Open lexical and morphological resources

| Resource | Verified scope/provenance | License evidence and limitations |
|---|---|---|
| FreeLing Spanish morphological dictionary | Owner reports over 555,000 forms and over 76,000 lemma–POS combinations, all categories; affix analysis recognizes further forms | Dictionary rights differ from program rights; counts are not verb counts. [Owner's data description](https://nlp.lsi.upc.edu/freeling/index.php/node/12) |
| FreeLing dictionary family | Main Spanish data derives from UPF's Spanish Resource Grammar; separate Argentine and Chilean resources exist | COPYING identifies main Spanish LGPL-LR, Argentine Apache 2.0, Chilean AGPL 3.0. Check the exact selected artifact's notices; do not apply the program license indiscriminately. [FreeLing COPYING §§12–15](https://github.com/TALP-UPC/FreeLing/blob/master/COPYING) |
| Apertium Spanish | Monolingual package provides morphology analysis/generation and POS tagging, with a monolingual dictionary file | Repository COPYING is GPL v2; no verified verb-lemma count or exhaustive-modern-Spanish claim. [README](https://raw.githubusercontent.com/apertium/apertium-spa/master/README), [COPYING](https://raw.githubusercontent.com/apertium/apertium-spa/master/COPYING) |
| UniMorph Spanish | README reports **6,812 verb lemmas**, alongside nouns/adjectives, derived from English Wiktionary | README states CC BY-SA 3.0. Count is a published dataset statistic, not a fresh recount or a claim of language completeness. No frequency ordering is documented there. [UniMorph Spanish](https://github.com/unimorph/spa) |

**Inference:** these resources are credible candidates for a versioned verb-lemma set or cross-resource comparison; none inspected claims every verb in all modern Spanish varieties. Morphological dictionary entries may represent homographs, POS distinctions, variants and pronominal uses differently. A union increases coverage but requires a recorded identity/normalization policy; it does not prove exhaustiveness or remove each source's license terms.

### Frequency alternatives and their limits

**EsPal** offers separate written and subtitle sources and queries for lemma/POS properties. Its owner describes written material from web, government, newspapers and literature, and subtitles from OpenSubtitles; subtitle contextual diversity measures the number/percentage of movies, not token frequency. No clear redistribution grant was verified from its FAQ, so accessibility must not be called an open-data license. [BCBL, EsPal FAQ](https://www.bcbl.eu/databases/espal/FAQ.php).

The creators' processing paper documents word–lemma–POS ambiguity and distinguishes maximum-lemma information from lemma frequencies based on aggregated associated forms. This is relevant because a surface spelling such as **caso** has multiple analyses. [Duchon et al., EsPal processing paper](https://www.bcbl.eu/databases/espal/img/2013_Duchon_EsPal_Processing_BRM_in_press.pdf).

**wordfreq** is a multi-source word-frequency library, with data described as a snapshot through approximately 2021. It is not documented as a Spanish verb-lemma-frequency inventory. Its README distinguishes Apache-licensed code from CC BY-SA 4.0 data and additional source attribution. The creator rejects data-only CSV exports because attribution/license information could be lost; this records the project's stated requirements and guidance, not an independent legal conclusion that CSV as a format is prohibited. An infinitive lookup would measure that spelling, not automatically every inflection of a verb. [wordfreq README, usage/license sections](https://github.com/rspeer/wordfreq).

**UD Spanish AnCora** supplies manually annotated lemmas converted to UD and news text. Its page gives **547,558 tokens / 560,138 syntactic words**, so it is a useful inspectable annotated corpus, not a complete lexicon. Its current metadata says **CC BY 4.0**, while descriptive text on the same page says an inherited **GNU license** and directs licensing questions to Barcelona. This conflict is unresolved here; the exact intended release and original provider terms need examination before redistribution claims. [UD Spanish AnCora](https://universaldependencies.org/treebanks/es_ancora/index.html).

**Analytical implications for “complete list sorted by frequency”:**

1. Keep the entire declared lemma set, including lemmas without measured corpus frequency. A top-N export cannot substitute for completeness.
2. Specify the frequency unit: lemma plus verb POS, token count, normalized rate, or dispersion. Include AUX as well as VERB if the chosen annotation splits these categories; otherwise ser, estar or haber could be lost by a mechanical POS filter.
3. Record corpus/release, date span, countries, genre balance, tokenization and lemma conventions. A press rank, subtitle rank and panhispanic mixed-corpus rank answer different questions.
4. A surface-form frequency cannot safely be summed without disambiguation: **fui** serves ser/ir, while noun/verb homographs and clitic segmentation create further ambiguity. Aggregating a compound phrase must not silently count auxiliary occurrences as lexical-verb occurrences.
5. Preserve “not measured,” “unattested in selected corpus,” and measured zero as separate states. A deterministic tail ordering can make a complete display sortable, but it is not evidence of relative frequency among those lemmas.
6. Record join behavior for *ir/irse*, obligatory pronominal verbs, spelling alternatives and homonymous lemmas. Otherwise merging sources can create duplicate entries or silently collapse senses and ranks.

These are consequences of the evidence, not a selection of source, ranking metric, product coverage, or permissions policy.

## Access, verification and open boundaries

Shell tools worked in the isolated worktree; the shell printed a nonfatal pyenv rehash warning. Web search/open tools successfully retrieved primary RAE/ASALE pages, academic-owner descriptions, original project READMEs/COPYING files and creator papers. No corpus was scraped, no bulk dictionary was imported, and no large dataset was downloaded. An attempted web open of Apertium's dictionary exceeded the reader's size limit; no local copy was obtained.

The CORPES application and country inventories had no readable server-rendered content in this tool; the linked TSV was rejected by the parser. Several guessed RAE grammar URLs were inaccessible or lacked entries and were not used as evidence. The Cervantes C1–C2 curriculum URL redirected to maintenance; it was not used to fill the gaps. Corpus sizes and UniMorph statistics above are owner/creator-published figures, not new independent counts. Dataset revisions can change them.

Unresolved boundaries are the operational definition of “all modern verbs”; the exact downloadable frequency schema and pronominal treatment; redistribution rights for any RAE-derived dataset or EsPal output; the AnCora license discrepancy; exact regional/register coverage beyond representative voseo patterns; and the treatment of productive new verbs and specialist vocabulary. The sources establish why these questions matter without deciding them for the product.
