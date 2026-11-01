# genpark-personal-agent-metabolic-visceral-adipose-tissue-vat-dexa-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

DEXA visceral adipose tissue area (VAT, cm2) and android-to-gynoid ratio cardiometabolic hazard predictor.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `evaluate_visceral_adipose_tissue_hazard`
- **Category**: `personal_agent`

### Method Documentation
Quantify deep intra-abdominal visceral adipose tissue area (VAT, cm2 / grams) and Android-to-Gynoid (A/G) fat ratio from DXA full-body scans.
Visceral adiposity drains directly into portal circulation, releasing pro-inflammatory adipokines (IL-6, TNF-alpha) and free fatty acids driving hepatic steatosis and cardiovascular risk.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "evaluate_visceral_adipose_tissue_hazard",
    "arguments": {
    "vat_area_cm2": 118.0,
    "android_fat_pct": 32.5,
    "gynoid_fat_pct": 28.0,
    "sex": "MALE",
    "bmi": 24.2
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
