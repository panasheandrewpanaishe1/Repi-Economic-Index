"""
REPI API layer — Layer 6 of the architecture (see docs/architecture.png).

Exposes the index and briefing endpoints consumed by the dashboard and downstream
StrucLeaf agents (CARBON, CAPITAL, RISK, POLICY) and the AFRIVIEW broadcast network.

Status: stub — full implementation tracked under milestone M3-M4, see Appendix B of
REPI-01_AI4I_Proposal_Development.pdf.
"""

from fastapi import FastAPI

app = FastAPI(title="REPI API", version="0.1.0")


@app.get("/index/current")
def get_current_index():
    """Return the latest computed REPI value and component breakdown."""
    # TODO: replace with a real call to the index computation engine
    return {"index_value": 53.2, "as_of": "2026-06-30T09:00:00+02:00", "status": "stub"}


@app.get("/index/history")
def get_index_history():
    """Return the historical REPI time series."""
    # TODO: query the time-series store
    return {"status": "stub", "message": "History endpoint not yet implemented"}


@app.get("/index/forecast")
def get_index_forecast():
    """Return the 30/60/90-day REPI forecast."""
    # TODO: call the forecast module (milestone M2)
    return {"status": "stub", "message": "Forecast endpoint not yet implemented"}


@app.get("/index/briefing")
def get_index_briefing():
    """Return the latest plain-language narrative briefing."""
    # TODO: call the narrative synthesis layer (milestone M3)
    return {"status": "stub", "message": "Briefing endpoint not yet implemented"}


@app.get("/components")
def get_components():
    """Return the current component weights driving the index."""
    # TODO: expose live weights from the composite index model
    return {"status": "stub", "message": "Components endpoint not yet implemented"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
