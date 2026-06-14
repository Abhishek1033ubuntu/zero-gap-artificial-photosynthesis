"""
Simulation 04: Techno-Economic & Policy Financing Model
Calculates initial CapEx amortization, hourly operational income, 
and infrastructure break-even points under a Green Cess mandate.
"""

import numpy as np
import matplotlib.pyplot as plt

def run_economic_simulation():
    hours = np.linspace(0, 1000, 1000)
    
    # Financial Configuration Parameters
    capex_stack = 3500.00    
    capex_solar_pv = 2500.00 
    total_capex = capex_stack + capex_solar_pv
    om_cost_per_hour = 0.05  

    # Product Valuations (Sourced from 1,000-hour module averages)
    val_methanol = 215.8 * 0.65
    val_ethanol = 92.6 * 0.90
    val_ethylene = 5.05 * 1.20
    commodity_revenue_rate = (val_methanol + val_ethanol + val_ethylene) / 1000.0 

    # Policy Revenue (2% Green Cess on a standard $250/hr industrial sales output)
    factory_net_sales_per_hour = 250.00
    green_cess_percentage = 0.02  
    policy_cess_rate = factory_net_sales_per_hour * green_cess_percentage 

    cumulative_cash_flow = []
    net_balance = -total_capex 

    for h in hours:
        hourly_net = commodity_revenue_rate + policy_cess_rate - om_cost_per_hour
        net_balance += hourly_net
        cumulative_cash_flow.append(net_balance)

    payback_hour = total_capex / (commodity_revenue_rate + policy_cess_rate - om_cost_per_hour)
    return hours, cumulative_cash_flow, total_capex, payback_hour

if __name__ == "__main__":
    hours, cash_flow, capex, payback = run_economic_simulation()
    print(f"Simulation 04 Status: Complete.")
    print(f"Total CapEx Outlay: ${capex:.2f} | Cost Recovery Achieved at: {payback:.1f} Hours")
