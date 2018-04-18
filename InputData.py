
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03
DELTA_T = 1         # years (length of time step, how frequently you look at the patient)

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,   0.0,    0.1],   # Well
    [0,     0.0,    1.0,    0.0],   # Stroke
    [0,     0.25,   0.55,   0.2],   # Post-Stroke
    [0.0,   0.0,    0.0,    1.0],   # Dead
    ]

ANNUAL_STATE_COST = [
    0,   # Well
    5000,   # Stroke
    200.0,    # Post-stroke
    0        #Death
]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1,   # Well
    0.90,   # Sproke
    0.8865,    # Post-Stroke
    0 #Death
]

anticoagulation_COST = 2000

# treatment relative risk
TREATMENT_RR = 0.509
TREATMENT_RR_CI = 0.365, 0.71  # lower 95% CI, upper 95% CI

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05
