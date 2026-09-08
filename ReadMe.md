# MIND4.OT

### Industrial Intelligence & Smart Manufacturing Platform

MIND4.OT is a simulation-based Industry 4.0 project that demonstrates an end-to-end smart manufacturing architecture from PLC control to MES, industrial data, analytics, and AI-assisted optimization.

The project combines multi-vendor PLC platforms with a vendor-neutral software layer.

> **PLC controls the machine. MES4.OT manages production. MIND4.OT analyzes, predicts, and recommends.**

---

## Architecture

```text
Production Order
      ↓
    MES4.OT
      ↓
 Python OT Gateway
      ↓
    OPC UA
      ↓
┌───────────┬───────────────┬───────────┐
│  Siemens  │ CODESYS/WAGO  │ Beckhoff  │
│Production │    Filling    │  Quality  │
└───────────┴───────────────┴───────────┘
      ↓
 PostgreSQL
      ↓
Analytics / Vision / ML
      ↓
   MIND4.OT
```

The system is designed to run without physical PLC hardware using simulated PLC environments.

---

## Production Line

| Station    | Platform       | Function                               |
|------------|----------------|----------------------------------------|
| Station 01 | Siemens        | Plastic container production           |
| Station 02 | CODESYS / WAGO | Recipe-based filling                   |
| Station 03 | Beckhoff       | Quality control, reject, and packaging |

An Arduino-based condition monitoring node is also planned for sensor data acquisition.

---

## Technology Stack

### Currently Used

- Siemens TIA Portal / PLCSIM Advanced
- Git / GitHub

### Planned

- CODESYS / WAGO SoftPLC
- Beckhoff TwinCAT 3
- OPC UA
- Python
- PostgreSQL / TimescaleDB
- Streamlit
- Power BI
- OpenCV
- Machine Learning
- Docker Compose

---

## MES4.OT

MES4.OT is the manufacturing execution layer responsible for:

- Order management
- Recipe management
- Production tracking
- Traceability
- Alarm and status monitoring
- Quality results
- PLC communication

Each manufactured product will be tracked using a unique `UnitID` across the production line.

---

## MIND4.OT

MIND4.OT extends the manufacturing system with:

- Manufacturing analytics
- Quality prediction
- Anomaly detection
- Computer vision inspection
- Condition monitoring
- Parameter recommendations
- Controlled optimization

AI-generated recommendations do not directly control PLC outputs.

PLC interlocks remain the final control and safety layer.

---

## Roadmap

| Phase | Goal |
|-------|------|
| M0    | Factory & process design |
| M1    | PLC development          |
| M2    | Industrial connectivity  |
| M3    | MES4.OT                  |
| M4    | PostgreSQL data layer    |
| M5    | Visualization            |
| M6    | Manufacturing analytics  |
| M7    | Computer vision          |
| M8    | ML / AI                  |
| M9    | Controlled optimization  |

---

## Current Status

🚧 **Under Development**

### Current Focus

**M1 — Siemens Production Station**

The production PLC is being developed using a state-machine-based architecture and will later be integrated with MES4.OT through OPC UA.