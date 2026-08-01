# Statistical Analysis of Background Radiation Using a Geiger–Müller Counter

## Overview

This repository contains an experimental study of the statistical
fluctuations in environmental background radiation recorded with a
Geiger–Müller counter.

A total of 75 independent measurements were taken, each over a fixed
counting interval of 60 seconds. The observed distribution was compared
with a theoretical Poisson distribution.

## Research Question

Are the fluctuations in the measured background radiation counts
consistent with Poisson counting statistics?

## Experimental Setup

| Parameter | Value |
|---|---:|
| Detector | Geiger–Müller counter and scaler unit |
| Manufacturer | Triode, India |
| GM-tube operating voltage | 750 V |
| Counting interval | 60 seconds |
| Number of trials | 75 |
| Measurement location | EMN Laboratory, Punjab Agricultural University, Ludhiana |
| Date of experiment | 16 July 2025 |

The operating voltage was selected within the plateau region of the GM
tube so that small voltage fluctuations would have minimal effect on the
recorded count rate.

![Experimental setup](figures/gm_counter_setup.jpg)

## Dataset

The raw dataset is available at:

```text
data/background_counts.csv
