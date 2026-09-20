# Contributing

## What belongs here

Add datasets that have a stable source page and an authoritative license or
usage-terms page. The catalog can include academic, research-only, commercial,
and public-preview datasets, but the access and rights conditions must be
described accurately.

## Required checks

Before adding an entry:

1. Open the official dataset or publisher page.
2. Locate the authoritative license or terms page.
3. Record the access method and whether login, application, or purchase is required.
4. Check training, fine-tuning, commercial use, frame extraction, and redistribution separately.
5. Record the date of the check and at least one evidence URL.
6. Check the dataset name and source URL for an existing entry.

If a permission is unclear, use `pending` or `unknown`. Do not infer permission
from a public download link.

## Entry format

Create one YAML file under the most appropriate directory:

- `datasets/verified/` when the relevant rights are verified;
- `datasets/pending/` when any material rights or source detail is unresolved.

Validate the entry against `schema/dataset-entry.schema.json` before opening a
pull request.

## Editorial rules

- Keep descriptions factual and concise.
- Do not use the catalog as an advertisement for a commercial product.
- Link directly to the dataset or repository when possible.
- Do not copy video files, frames, credentials, private links, or confidential terms.
- Keep upstream attribution and license names unchanged.
- Mark stale, unavailable, gated, or purchase-only access clearly.

## Pull requests

Use a title such as `catalog: add <dataset name>` or `catalog: update <dataset name>`.
Explain the source checked, the license source, the access status, and any
remaining uncertainty.
