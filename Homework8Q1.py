#Steady state
import Homework8Classes as Cls

# run trail of 1000 games to calculate expected reward
fairgames = Cls.SetOfGames(id=1, prob_head=0.5, n_games=1000)
testFair = fairgames.simulation()
# print the average reward
print('Expected reward when the probability of head is 0.5:', testFair.get_ave_reward())

# run trail of 1000 games to calculate expected reward
unfairgames = Cls.SetOfGames(id=2, prob_head=0.45, n_games=1000)
testUnFair = unfairgames.simulation()
# print the average reward
print('Expected reward when the probability of head is 0.45:', testUnFair.get_ave_reward())

#Problem 1:
#-29.9 - -5.9 = $24 difference in the casino owners reward