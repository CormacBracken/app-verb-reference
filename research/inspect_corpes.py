#!/usr/bin/env python3
"""Read-only inspection of the original CORPES TSV; emits aggregate evidence, not data."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re

EXPECTED_SHA256 = "16203075050080abd4e5eabe35db5723bc74563707ea62244e48d94ba17d38cb"
HEADER = ["Orden", "Rango frec.", "Lema", "Forma", "Etiqueta", "Frec.", "Frec. norm.", "DP", "Núm. países"]
INFINITIVE = re.compile(r"(?:ir|[a-záéíóúüñ]+(?:-[a-záéíóúüñ]+)*(?:ar|er|ir|ír))(?:se)?")


def inspect(path):
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError(f"Unreviewed input hash: {digest}")
    lines = raw.decode("utf-8").splitlines()
    if lines[2].split("\t") != HEADER:
        raise ValueError("Unexpected header")
    lemmas, forms, malformed = [], defaultdict(list), []
    parent = None
    for line_number, line in enumerate(lines[3:], 4):
        if not line.strip() or line == "\x1a":
            continue
        cells = [cell.strip() for cell in line.split("\t")]
        if len(cells) != 9:
            malformed.append((line_number, cells))
            # A malformed lemma starts with its numeric ordinal. In this pinned
            # artifact all such rows are numerals; retain their M identity so
            # subsequent complete detail cannot be attached to a previous lemma.
            if re.fullmatch(r"\d+\.", cells[0]):
                if len(cells) < 5 or cells[4] != "M":
                    raise ValueError(f"Unexpected malformed lemma at {line_number}")
                parent = (cells[2], "M")
            continue
        if cells[2] and not cells[3]:
            parent = (cells[2], cells[4])
            lemmas.append((line_number, cells))
        elif cells[4] and not any(cells[:3]):
            if parent is None:
                raise ValueError(f"Unparented form at {line_number}")
            forms[parent].append(cells)
        else:
            raise ValueError(f"Unexpected row type at {line_number}")

    verbs = [(line, row) for line, row in lemmas if row[4] == "V"]
    identities = Counter(row[2] for _, row in verbs)
    frequency_groups = Counter(int(row[5]) for _, row in verbs)
    if any(value > 1 for value in identities.values()):
        raise ValueError("Duplicate verbal lemma identities")
    if any(int(row[5]) <= 0 for _, row in verbs):
        raise ValueError("Nonpositive verbal count")
    mismatches = [row[2] for _, row in verbs if int(row[5]) != sum(int(form[5]) for form in forms[(row[2], "V")])]
    if mismatches:
        raise ValueError(f"Verb/form totals disagree: {mismatches}")
    shaped = [(line, row) for line, row in verbs if INFINITIVE.fullmatch(row[2])]
    pronominals = [(line, row) for line, row in shaped if row[2].endswith("se")]
    lookup = {row[2]: (line, row) for line, row in verbs}
    samples = {}
    for lemma in ["ser", "estar", "haber", "ir", "irse", "arrepentirse", "adentrarse", "abrumar", "abrumarse", "debatir", "debatirse"]:
        found = lookup.get(lemma)
        if found is None:
            samples[lemma] = None
            continue
        line, row = found
        detail = forms[(lemma, "V")]
        samples[lemma] = {"line": line, "frequency": int(row[5]), "form_rows": len(detail), "form_sum": sum(int(form[5]) for form in detail)}
    return {
        "sha256": digest, "bytes": len(raw), "physical_lines": len(lines),
        "complete_lemma_rows_all_pos": len(lemmas),
        "malformed_nonblank_lines": len(malformed),
        "malformed_lemma_starters": sum(bool(re.fullmatch(r"\d+\.", row[0])) for _, row in malformed),
        "verb_lemma_rows": len(verbs), "unique_verbal_lemmas": len(identities),
        "verbal_frequency_sum": sum(int(row[5]) for _, row in verbs),
        "minimum_frequency": min(frequency_groups), "maximum_frequency": max(frequency_groups),
        "singletons": frequency_groups[1], "frequency_two": frequency_groups[2],
        "distinct_frequencies": len(frequency_groups),
        "tied_frequency_groups": sum(size > 1 for size in frequency_groups.values()),
        "lemmas_in_ties": sum(size for size in frequency_groups.values() if size > 1),
        "form_sum_mismatches": len(mismatches),
        "single_infinitive_shape_candidates": len(shaped),
        "shape_rejected": len(verbs) - len(shaped),
        "ambiguous_pipe_lemmas": sum("|" in row[2] for _, row in verbs),
        "candidate_frequency_sum": sum(int(row[5]) for _, row in shaped),
        "candidate_singletons": sum(int(row[5]) == 1 for _, row in shaped),
        "hyphenated_candidates": sum("-" in row[2] for _, row in shaped),
        "pronominal_shape_lemmas": len(pronominals),
        "pronominal_with_base_also_present": sum(row[2][:-2] in lookup for _, row in pronominals),
        "pronominal_frequency_sum": sum(int(row[5]) for _, row in pronominals),
        "pronominal_singletons": sum(int(row[5]) == 1 for _, row in pronominals),
        "samples": samples,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    print(json.dumps(inspect(args.file), ensure_ascii=False, indent=2))
