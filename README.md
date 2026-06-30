# Zero-Gap Modular Artificial Photosynthesis Stack

An end-to-end multi-physics simulation and techno-economic framework for a scalable, point-source carbon recycling platform. This project models the direct conversion of industrial flue-gas CO₂ and solar power into high-value wholesale commodities (Methanol, Ethanol, and Ethylene gas) using a zero-gap Proton Exchange Membrane (PEM) bipolar stack architecture.

## 🚀 Executive Summary

The platform provides a highly scalable, economically viable alternative to traditional ambient Direct Air Capture (DAC) systems by bypassing the extreme energy penalties of atmospheric dilution. By co-locating the system directly at industrial emission sites and pairing it with dedicated solar PV, the architecture eliminates raw utility bills. It operates as a self-funding infrastructure asset financed by a localized municipal "Green Cess" tax levied on participating manufacturing facilities.

### Core Architecture Highlights
* **Zero-Gap PEM Configuration:** Replaced open fluidic dome gas traps with a compact membrane electrode assembly (MEA) sandwich, eliminating bubble overpotential, dropping cell resistance by > 1.0V, and unlocking a 10.4× increase in volumetric power density.
* **Cross-Flow Sweep Hydrodynamics:** Implemented an aggressive microfluidic cross-flow sweep velocity profile that rapidly flushes generated liquid products from the catalyst surface, successfully mitigating back-diffusion crossover and re-oxidation at the anode.
* **In-Situ Electrochemical Regeneration:** Programmed a automated 5-minute anodic polarity inversion pulse every 200 operational hours to strip carbonaceous surface fouling and reset catalyst morphology, permanently preventing long-term decay below the 45% thermodynamic profitability limit.

---

## 📁 Repository Structure

```text
├── simulations/
│   ├── 01_baseline_kinetics.ipynb        # Initial gas trap kinetics & fluid velocity limits
│   ├── 02_integrated_master.ipynb        # 1,000-hr sawtooth lifetime model with automated flush cycles
│   ├── 03_advanced_multiphysics.ipynb     # Multi-product split (Ethylene gas) & 4.08 kW thermal balance
│   └── 04_techno_economic_model.ipynb    # Green Cess policy finance engine & capital payback simulation
├── hardware_specs/
│   ├── mechanical_blueprint.md           # CNC plate milling coordinates, EPDM torque specs, and weight bills
│   └── /cad_step_files/                  # (Placeholder for physical 3D modeling assets)
├── docs/
│   ├── Artificial_Photosynthesis_Project_Report.pdf  # Full validated engineering and policy report
│   └── Completed_Artificial_Photosynthesis_Report.pdf
└── README.md                             # Repository landing page and system documentation
