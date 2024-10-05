#You are a Pokémon trainer. 
# Each Pokémon has its own power, described by a positive integer value. 
# As you travel, you watch Pokémon and you catch each of them. 
# After each catch, you have to display maximum and minimum powers of Pokémon caught so far. 
# You must have linear time complexity. So sorting won’t help here. 
# Try having minimum extra space complexity.

#Suppose you catch Pokémon of powers 3 8 9 7. Then the output should be
#3 3
#3 8
#3 9
#3 9

#python code to train pokemon
powers = [3,8,9,7]
mini, maxi = 0,0
for power in powers:
    if mini == 0 and maxi == 0:
        mini, maxi = powers[0], powers[0]
        print(mini, maxi)
    else:
        mini = min(mini, power)
        maxi = max(maxi, power)
        print(mini, maxi)

#Time Complexity is 0(N) with Space Complexity 0(1)