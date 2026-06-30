# Hardware & Mechanical Specifications: 5-Cell Compression Stack Array

This document defines the physical hardware constraints, material callouts, and assembly torque tolerances required to fabricate the zero-gap Proton Exchange Membrane (PEM) modular stack.

## 📐 1. Mechanical Envelope & Structural Bill of Materials (BOM)

| Component | Quantity | Material Sourcing | Dimension Parameters | Function |
| :--- | :--- | :--- | :--- | :--- |
| **Outer End-Plates** | 2 | 316L Stainless Steel | 1100 mm × 180 mm × 25 mm | Rigid structural compression boundary |
| **Bipolar Substrate Plates** | 6 | Resin-Impregnated Synthetic Graphite | 1100 mm × 180 mm × 6 mm | Flow field distribution and electrical interconnect |
| **Membrane Electrode Assemblies**| 5 | Nafion 115 + Nanostructured Cu/IrO₂ | 1000 mm × 100 mm (125\,\mum thick) | Active electrochemical core matrix |
| **Sealing Gaskets** | 12 | Die-Cut EPDM Fluoropolymer | Custom Perimeter Boundary (1.5 mm uncompressed) | Fluid containment and perimeter isolation |
| **Tie-Rods** | 8 | Grade 8.8 High-Tensile Carbon Steel | M16 High-Strength Threads | Uniform stack compression mechanism |

---

## 🛠️ 2. CNC Fluidic Channel Milling Coordinates

The flow profiles are milled directly into both active faces of the synthetic graphite bipolar plates using a parallel co-flow channel geometry.

* **Flow Field Geometry:** 45 parallel channels running longitudinally along the 1.0-meter active axis.
* **Milling Depth (Channel):** 1.20 mm \pm 0.02 mm
* **Milling Width (Channel):** 1.50 mm
* **Rib / Land Width (Wall spacing):** 1.00 mm
* **Tolerance Spec:** Cross-channel dimensional uniformity must be maintained within \pm 0.01 mm to prevent preferential fluid bypassing or dead zones that cause localized hot-spots.

---

## 🔩 3. Stack Assembly Compression Protocol

Achieving a precise seal across a 1.0-meter active length without crushing the brittle graphite substrate plates or pinching the membrane layer requires strict compliance with a controlled torque gradient.

```text
       [Top End-Plate Steel Boundary]
   (Tie 1)     (Tie 3)     (Tie 5)     (Tie 7)
      O-----------O-----------O-----------O
      |                                   |
      |       ACTIVE BIPOLAR STACK        |
      |                                   |
      O-----------O-----------O-----------O
   (Tie 8)     (Tie 6)     (Tie 4)     (Tie 2)
     [Bottom End-Plate Steel Boundary]
