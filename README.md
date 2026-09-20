# Awesome Licensed Video Datasets

A curated directory of video datasets with transparent license, access,
training, and redistribution information.

## What this catalog covers

This catalog collects video, video-frame, and multimodal video datasets for
computer vision, video understanding, robotics, autonomous driving, and AI
data workflows.

Each entry separates the following questions:

- Can the dataset be viewed or downloaded?
- Is research use allowed?
- Is model training or fine-tuning allowed?
- Is commercial use allowed?
- Are frame extraction and derived data allowed?
- Is redistribution allowed?

An accessible URL does not by itself grant permission to train models or
redistribute data. Read the upstream terms before using any dataset.

## Entry status

- `verified`: the license source and the relevant usage permissions have been
  checked against an authoritative source.
- `pending-confirmation`: the dataset is a candidate, but one or more rights
  fields still require confirmation.
- `not-verified`: the source or usage terms could not be verified.

Only entries with `verified` status should appear in the main recommended list.

## Repository structure

- `datasets/verified/`: datasets with verified license and usage information.
- `datasets/pending/`: candidates awaiting rights or source verification.
- `schema/`: the machine-readable entry schema.
- `docs/`: review policy and field definitions.

## Scope

This repository stores catalog metadata and links. It does not mirror or
redistribute the listed video files.

The license for catalog text does not change the license of any upstream
dataset. Every dataset keeps its own license and usage conditions.

## Current candidates

- [Thordata First-Person Perspective Driving Video Collection](datasets/pending/thordata-first-person-driving.yml)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) before adding an entry.
