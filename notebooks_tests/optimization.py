#!/usr/bin/env python
# coding: utf-8

# ### Using PuLP package

# In[32]:


import pandas as pd
import pulp
from pulp import LpProblem, LpMinimize, LpVariable, lpSum


# In[ ]:


class MaintenanceOptimization:
    '''
    data: 
        The dataframe containing turbine fault, SCADA, and status information.
    model: 
        The optimization model for minimizing maintenance costs.
    downtime_vars: 
        A dictionary of decision variables representing downtime hours for each observation.
    '''
    def __init__(self, data, maintenance_costs, downtime_cost_per_kwh):
        self.data = data
        self.maintenance_costs = maintenance_costs
        self.downtime_cost_per_kwh = downtime_cost_per_kwh
        self.model = LpProblem("Maintenance_Cost_Minimization", LpMinimize)
        self.downtime_vars = LpVariable.dicts("Downtime", data.index, lowBound=0, upBound=24, cat='Continuous')

    def setup_objective(self):
        '''
        Sets up the objective function for the optimization model, which minimizes total maintenance and downtime costs.
        '''
        maintenance_costs = []
        downtime_costs = []

        for i, row in self.data.iterrows():
            fault_type = row['Fault']
            is_high_demand = row['Is_High_Demand']
            season = row['Season']

            # Maintenance cost per fault type
            if is_high_demand:
                maintenance_cost = self.maintenance_costs['high_demand']
            elif fault_type == 'Routine':
                maintenance_cost = self.maintenance_costs['routine']
            else:
                maintenance_cost = self.maintenance_costs['default']

            # Adjust maintenance cost by season if needed
            if season == 'Winter':
                maintenance_cost *= 1.1

            # Downtime cost
            production_loss = row['WEC: Production kWh'] * self.downtime_vars[i]
            downtime_cost = production_loss * self.downtime_cost_per_kwh

            maintenance_costs.append(maintenance_cost)
            downtime_costs.append(downtime_cost)

        # Define objective function
        self.model += lpSum(maintenance_costs) + lpSum(downtime_costs), "Total_Maintenance_Cost"

    def add_constraints(self):
        '''
        Adds necessary constraints to the model, such as maximum allowable downtime per observation.
        '''
        for i in self.data.index:
            downtime_constraint = self.downtime_vars[i] <= 24
            constraint_name = f"Maximum allowable downtime for observation {i}"
            self.model += downtime_constraint, constraint_name

    def solve(self):
        '''
        Solves the optimization model and returns the decision variable values.
        '''
        self.model.solve()

        result_dict = {}
        for v in self.model.variables():
            result_dict[v.name] = v.varValue

        return result_dict



# ### Overview of the Class
# 
# The `MaintenanceOptimization` class is designed to minimize the total cost of maintaining wind turbines by balancing two key costs:
# 1. Maintenance Costs: Costs associated with repairing turbines based on the type and severity of faults.
# 2. Downtime Costs: Losses when turbines are not producing energy.
# 
# The class uses data from feature engineering (e.g., season, fault severity, high-demand periods) to adjust costs dynamically.
# 
# ---
# 
# ### Key Components and Variables
# 
# #### 1. **Inputs to the Class**
# - **`data`(DataFrame)**:
#   - The feature-engineered dataset with all necessary columns, such as:
#     - `Fault`: Type of fault (e.g., "Routine" or "High-Severity").
#     - `WEC: Production kWh`: Energy production in kWh, used to calculate downtime costs.
#     - `Is_High_Demand`: Indicator for high-demand seasons (1 for high-demand, 0 otherwise).
#     - `Season`: The season (e.g., Winter, Summer) for potential seasonal adjustments.
# - **`maintenance_costs`**:
#   - A dictionary specifying costs for different conditions:
#     - `'high_demand'`: Maintenance cost during high-demand seasons (e.g., summer).
#     - `'routine'`: Maintenance cost for routine faults.
#     - `'default'`: Maintenance cost for all other cases.
# - **`downtime_cost_per_kwh`**:
#   - A float representing the cost per kilowatt-hour of downtime (e.g. energy revenue lost when turbines are offline).
# 
# #### 2. **Variables in the Class**
# - **`self.model`**:
#   - The optimization problem (defined using PuLP) that minimizes the total cost.
# - **`self.downtime_vars`**:
#   - Decision variables representing the number of downtime hours for each observation in the dataset. 
#   - Each observation has its own variable.
#     - Example: Downtime_0 represents downtime for the first observation.
# 
# #### 3. **Methods**
# - **`__init__`**:
#   - Initializes the class with input `data`, `maintenance_costs`, and `downtime_cost_per_kwh`.
#   - Sets up the optimization model and decision variables.
# - **`setup_objective`**:
#   - Constructs the **objective function** to minimize total costs:
#   - Combines:
#     - **Maintenance Costs**:
#       - Determined by `maintenance_costs` and fault/seasonal conditions.
#     - **Downtime Costs**:
#       - Based on lost production (`WEC: Production kwh`) and `downtime_cost_per_kwh`.
#     **Example**:
#       - For a **high-severity fault** during **Winter**:
#       - Maintenance Cost: `high_demand_cost * 1.1` (adjusted for Winter).
#         - Downtime Cost: `Lost Production kWh * downtime_cost_per_kwh`.
# - **`add_constraints`**:
#   - Adds constraints to ensure downtime does not exceed 24 hours per observation.
# - **`solve`**:
#   - Solves the optimization problem and returns the optimal values of decision variables (i.e., recommended downtime hours for each observation).
# 
# ---
# 
# ### 4. **Outputs**
# - **Optimal Downtime**:
#    - The downtime values (e.g., `Downtime_0`, `Downtime_1`) for each observation.
#    - Suggests the best maintenance schedule.
# 
# - **Minimized Total Cost**:
#    - The calculated minimized maintenance + downtime cost for the dataset.
# 
# ---
# 
# ### 5. **Step-by-Step Walkthrough**
# 
# #### 1. **Input Data Integration**
# - Feature-Engineered Data:
#   - The data DataFrame contains both feature-engineered columns (e.g., `Season`, `Fault_Severity`) and raw metrics (e.g., `WEC: Production kWh`).
#   - This allows the optimization to dynamically adjust maintenance and downtime costs based on meaningful patterns (e.g., high faults during winter or low production in fall).
# 
# #### 2. **Defining Maintenance Costs**
# - Maintenance costs are calculated for each observation:
#   - If the season is high-demand (e.g., summer): use `high_demand` cost.
#   - If the fault is routine: use `routine` cost.
#   - Otherwise, use `default` cost.
#   - Example: During winter, costs might increase by 10% (adjusted by season).
# 
# #### 3. **Calculating Downtime Costs**
# - Downtime costs depend on:
#   - `WEC: Production kWh`: Average energy production of the turbine.
#   - `downtime_vars[i]`: The downtime hours for observation `i`.
#   - Formula: `production_loss * downtime_cost_per_kwh`.
# 
# #### 4. **Objective Function**
# - Combines maintenance and downtime costs
#   - $Total Cost = \sum (Maintenance Cost) +  \sum (Downtime Cost)$
# 
# #### 5. **Adding Constraints**
# - Ensures downtime variables do not exceed 24 hours (realistic daily downtime limits).
# 
# #### 6. **Solving the Problem**
# - The `solve()` method uses PuLP to compute the optimal downtime for each observation, minimizing the total cost.
#   
# 
# 
# 
# 
