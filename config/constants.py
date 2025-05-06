# Dictionary for all constants
PARAMETER_UNITS = {
    # Core Biological - Metabolic & Feed
    "VO2": "ml/kg/hr",
    "VCO2": "ml/kg/hr",
    "RER": "ratio",
    "HEAT": "kcal/hr",
    "FEED": "g", # Represents FEED1 ACC

    # Core Biological - Activity
    "XTOT": "counts",
    "XAMB": "counts",
    "YTOT": "counts",
    "YAMB": "counts",
    "ZTOT": "counts",
    "ZAMB": "counts",

    # Core Biological - Accumulated Gas (Net Change)
    "ACCCO2": "l",      # Net Accumulated CO2 (Liters) over period
    "ACCO2": "l",       # Net Accumulated O2 (Liters) over period - Often represents consumption

    # Diagnostic - Gas Concentrations
    "O2IN": "%",
    "O2OUT": "%",
    "CO2IN": "%",
    "CO2OUT": "%",

    # Diagnostic - Delta Gas Concentrations
    "DO2": "%",         # O2IN - O2OUT
    "DCO2": "%",        # CO2OUT - CO2IN

    # Diagnostic - Environmental/System
    "FLOW": "lpm",      # Liters per minute
    "PRESSURE": "mmhg", # Millimeters of mercury
}

GROUP_COLORS = {
    "Group 1": "#4285F4",  # Google Blue
    "Group 2": "#EA4335",  # Google Red
    "Group 3": "#FBBC05",  # Google Yellow
    "Group 4": "#34A853",  # Google Green
    "Group 5": "#8A2BE2",  # Blue Violet
    "Group 6": "#FF7F00",  # Orange
    "Group 7": "#FF69B4",  # Hot Pink
    "Group 8": "#1E90FF",  # Dodger Blue
}

# Add parameter_descriptions dictionary
parameter_descriptions = {
    # Core Biological - Metabolic & Feed
    "VO2": "Oxygen consumption rate (ml/kg/hr)",
    "VCO2": "Carbon dioxide production rate (ml/kg/hr)",
    "RER": "Respiratory Exchange Ratio (VCO2/VO2)",
    "HEAT": "Calculated heat production (kcal/hr)",
    "FEED": "Accumulated food intake (g) [Use FEED1 ACC file]", # Emphasize file

    # Core Biological - Activity
    "XTOT": "Total X-axis activity (fine + ambulatory, counts)",
    "XAMB": "Ambulatory X-axis activity (locomotion, counts)",
    "YTOT": "Total Y-axis activity (fine + ambulatory, counts)",
    "YAMB": "Ambulatory Y-axis activity (locomotion, counts)",
    "ZTOT": "Total Z-axis activity (fine + rearing/climbing, counts)",
    "ZAMB": "Ambulatory Z-axis activity (rearing/climbing, counts)",

    # Core Biological - Accumulated Gas (Net Change)
    "ACCCO2": "Net Accumulated CO2 production (L) over period", # Clarify 'Net' and 'L? hmm'
    "ACCO2": "Net Accumulated O2 consumption (L) over period", # Clarify 'Net' and 'L'

    # Diagnostic - Gas Concentrations
    "[Diagnostic] O2IN": "Inlet Oxygen concentration (%) ",
    "[Diagnostic] O2OUT": "Outlet Oxygen concentration (%)",
    "[Diagnostic] CO2IN": "Inlet Carbon Dioxide concentration (%)",
    "[Diagnostic] CO2OUT": "Outlet Carbon Dioxide concentration (%)",

    # Diagnostic - Delta Gas Concentrations
    "[Diagnostic] DO2": "Delta O2 conc. (O2IN - O2OUT, %)",
    "[Diagnostic] DCO2": "Delta CO2 conc. (CO2OUT - CO2IN, %)",

    # Diagnostic - Environmental/System
    "[System] FLOW": "Air flow rate through cage (lpm)",
    "[System] PRESSURE": "Barometric pressure (mmhg)",
}