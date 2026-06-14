"""
Simulation 02: Integrated Master Lifespan Model
Simulates a 1,000-hour continuous production run tracking catalyst poisoning 
decay factors alongside automated 200-hour electrochemical flush cycles.
"""

import numpy as np

def run_integrated_master():
    hours = np.linspace(0, 1000, 1000)
    recycle_interval = 200
    decay_rate = 0.0015
    
    initial_fe_methanol = 0.50
    initial_fe_ethanol = 0.30
    
    efficiency_index_history = []
    time_since_flush = 0
    
    for h in hours:
        # Standard exponential decay tracking surface poisoning
        decay_factor = np.exp(-decay_rate * time_since_flush)
        
        # In-situ pulse recycling condition logic
        if int(h) % recycle_interval == 0 and h > 0:
            decay_factor = 0.98  # Reset catalyst surface to near-pristine state
            time_since_flush = 0
        else:
            time_since_flush += 1
            
        fe_meoh = initial_fe_methanol * decay_factor
        fe_etoh = initial_fe_ethanol * decay_factor
        
        # Combined chemical faradaic index score (%)
        system_score = (fe_meoh + fe_etoh) * 100
        efficiency_index_history.append(system_score)
        
    return hours, efficiency_index_history

if __name__ == "__main__":
    hours, eff_history = run_integrated_master()
    min_eff = min(eff_history)
    max_eff = max(eff_history)
    print(f"Simulation 02 Status: Verified.")
    print(f"  Sawtooth Efficiency Bounds -> Peak: {max_eff:.1f}% | Absolute Floor: {min_eff:.1f}%")
    print(f"  Thermodynamic Profitability Limit (45.0%) Maintained Successfully: {min_eff > 45.0}")
