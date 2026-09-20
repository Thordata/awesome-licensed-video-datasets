# License And Access Fields

## Access fields

- `access_type`: the access route for the listed preview or dataset.
- `download_requires_login`: whether downloading requires an account.
- `purchase_required`: whether purchase or a commercial agreement is required.
- `data_access_url`: the page where a user can obtain or request the data.
- `sample_media_url`: a specific public sample file when one has been verified.

## Permission fields

Each `permissions` value should be one of:

- `allowed`: explicitly allowed by the authoritative terms;
- `not-allowed`: explicitly prohibited;
- `conditional`: allowed only under stated conditions;
- `pending`: requires rights-holder confirmation;
- `unknown`: the terms do not answer the question.

Do not infer permission from a public download link or from a repository code
license.
