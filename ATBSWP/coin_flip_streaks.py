# flips coin 100 times and sees how many times there 
# is a streak of 6 or more.
# This case is doine 100000 times.

import random
STREAK = 6 # How many wins before we count the streak
CASES_TO_RUN = 1000

streak_count = 0
results = []

for i in range(CASES_TO_RUN): #run 100,000 cases
    
    # 1 Case = 100 flips
    # create a list with the results of the 100 flips
    for flip in range(100):
        outcome = random.randint(0, 1)
        if outcome == 0: #HEADS
            results.append('H')
        else: #TAILS
            results.append('T')
    
    # Need to iterate list and find streaks of STREAK or more
    prior_result = '' #Keep track of the previous result
    current_streak = 0    
    for result in results:
        if result == prior_result:
            #Add to the streak
            current_streak += 1
        else:
            #Reset the streak
            current_streak = 1
        prior_result = result #pass the result down the prior
        
        # Add to the streak count if there is a streak
        # We can break out of this iteration and go to the next as well
        if current_streak == STREAK: 
            streak_count += 1
            has_streak = True
            break
    
        
    if i % 100 == 0:
        print(i, '/{} test cases ran...'.format(CASES_TO_RUN))
streak_pct = (streak_count / CASES_TO_RUN) * 100
print('Chance of streak: {:.2f}'.format(streak_pct))