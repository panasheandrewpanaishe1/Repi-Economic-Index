# REPI — Real-Time Economic Power Index

**POTRAZ AI for Impact Challenge 2026 — Track 3: Development**
Project ID: REPI-01 · Team: StrucLeaf REPI Team

## Problem

Zimbabwean policymakers, investors and businesses currently assess economic and energy
conditions using fragmented, lagging sources — monthly or quarterly bulletins from RBZ and
ZIMSTAT, informal market signals, and sector-specific reports that rarely speak to one another.
There is no single, continuously updated reference point that synthesises monetary, energy and
infrastructure signals into one number decision-makers can track week to week.

**Target users:** government planning units, financial institutions and investors, and
StrucLeaf's own downstream AI agents (CAPITAL, RISK, POLICY) and the AFRIVIEW broadcast network.

## Solution

REPI is a live, AI-computed composite index that fuses public economic data (RBZ, ZIMSTAT,
World Bank, FX/fuel reference feeds) with StrucLeaf's own platform telemetry (AEOS/Crystal Solar
energy data, Wazi Infra infrastructure signals, AFRIVIEW network activity) into a single tracked
score, updated continuously and accompanied by a plain-language briefing explaining what is
driving the current reading.

## Demo

- **Live dashboard:** [repi-dashboard.netlify.app](https://repi-dashboard.netlify.app)
- Video walkthrough: _to be added_

## Architecture

REPI is a seven-layer pipeline: data ingestion → storage → index computation → narrative
synthesis → API layer → application surfaces (public dashboard + downstream StrucLeaf agents).
Full diagram: [`docs/architecture.png`](docs/architecture.png)

**Core AI components:**
- **Composite Index Model** — gradient-boosted regression for dynamic component weighting, plus
  seasonal-trend decomposition for drift/anomaly detection. This isn't a fixed-weight formula:
  the relative influence of each input (energy output, FX signals, infrastructure activity)
  shifts over time, and a static formula would drift out of calibration as the underlying
  economic structure changes.
- **Forecast Module** — short-horizon time-series forecast (Prophet/ARIMA-class) producing the
  30/60/90-day REPI outlook.
- **Narrative Synthesis Layer** — a quantized Llama-3-8B-Instruct model converts the index's
  numeric output and component drivers into a short plain-language briefing. This is strictly
  grounded: it generates text only from computed index values and pre-defined driver templates,
  not open-ended generation, to keep output auditable and limit hallucination risk.

## Data

| Source | Type | Status |
|---|---|---|
| RBZ, ZIMSTAT, World Bank | Public economic data | Live via scheduled ingestion |
| FX / fuel reference feeds | Public market data | Live via scheduled ingestion |
| AEOS/Crystal Solar telemetry | StrucLeaf platform data | Early integration in progress |
| Wazi Infra IoT signals | StrucLeaf platform data | Roadmap (not yet integrated) |
| AFRIVIEW network activity | StrucLeaf platform data | Roadmap (not yet integrated) |

Full integration of all StrucLeaf platform data sources is a near-term roadmap item, not complete
today — this is disclosed rather than presented as fully live across every source. See
`sample_data/` for a schema mock of the ingested indicator format.

## AI Method

See **Architecture** above for model rationale. Validation approach: the composite index model is
backtested against historical public indicators before each release; the narrative layer is
covered by a prompt-regression test suite checking briefing outputs against a fixed set of index
scenarios (see `/tests`). Any index reading that triggers the anomaly-detection threshold is held
for manual review before publication.

## Setup

```bash
git clone https://github.com/<org>/repi-economic-index.git
cd repi-economic-index
pip install -r requirements.txt
cp .env.example .env   # fill in your own local values, never commit .env
python src/ingest.py   # run a manual ingestion cycle
python src/api.py      # start the local API server
```

## Environment Variables

See [`.env.example`](.env.example) for the full list of required variables and what each one
configures. No real credentials are committed to this repository.

## Tests

```bash
pytest tests/
```

Covers: index output range/monotonicity checks, missing-input-field handling, and narrative
briefing regression tests against fixed index scenarios.

## Deployment

- **Pilot/testing:** ZCHPC Cloud Compute Environment (CCE) — GPU instance for LLM inference, CPU
  instances for ingestion/storage/API.
- **Current live surface:** dashboard hosted on Netlify, consuming the API layer.
- Full deployment plan (hosting, operator, pilot site, monitoring, scale pathway): see Appendix B
  of `REPI-01_AI4I_Proposal_Development.pdf`.

## Known Limitations

- StrucLeaf platform data sources (Wazi Infra, AFRIVIEW) are not yet fully integrated — the live
  index currently weights more heavily on public data sources.
- No dedicated data engineer or ML specialist on the team yet; model validation work is being
  supported through POTRAZ bootcamp mentorship.
- Narrative layer has not yet been tested at scale against adversarial or ambiguous index
  scenarios beyond the initial fixed test-case set.

## Team

| Name | Role |
|---|---|
| Panashe Andrew Banda | Lead Innovator, Founder & CEO, StrucLeaf Holdings |
| Wesly Gaba | Banking |
| Blessing Wutete | Software Engineering |

## License

Restricted access — submitted for POTRAZ AI for Impact Challenge 2026 evaluation. Contact the
team for reuse or collaboration enquiries.
