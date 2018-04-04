import Homework8Parameters as P
import Homework8SupportTransientState as Support
import Homework8Classes as Hw8

# create multiple cohorts for when the drug is not available
multiCohortFairCoin = Hw8.MultipleGameSets(
    ids=range(P.SIM_NUM_GAMES),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    n_games_in_a_set= P.REAL_NUM_GAMES,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=P.HEADS_PROB_FAIR # [p, p, ...]
)
# simulate all cohorts
multiCohortFairCoin.simulation()

# create multiple cohorts for when the drug is available
multiCohortUnFairCoin = Hw8.MultipleGameSets(
    ids=range(P.SIM_NUM_GAMES, 2*P.SIM_NUM_GAMES),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
    n_games_in_a_set= P.REAL_NUM_GAMES,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=P.HEADS_PROB_UNFAIR
)
# simulate all cohorts
multiCohortUnFairCoin.simulation()

# print outcomes of each cohort
print(Support.print_outcomes(multiCohortFairCoin, 'When coin is fair:'))
print(Support.print_outcomes(multiCohortUnFairCoin, 'When coin is unfair:'))

# print comparative outcomes
print(Support.print_comparative_outcomes(multiCohortFairCoin, multiCohortUnFairCoin))

#Problem 2:
#When coin is fair:
#The estimate of mean reward ($) and 95% prediction interval: -2473.2 (-4300.0, -800.0)

#When coin is unfair:
#The estimate of mean reward ($) and 95% prediction interval: -503.2 (-2400.0, 1300.0)

#The change in reward is $1,970.

