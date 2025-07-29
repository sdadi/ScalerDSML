import numpy as np

data = np.loadtxt('fit.txt', dtype='str')
print(data.ndim, data.shape)
print(data)

active_days = data[data[:, 5] == 'Active']
print('Active days:', active_days)
print('Average step count on Active days:', np.average(active_days[:,1].astype(int)))

step_count = data[:,1].astype(int)
mood = data[:,2]
calories = data[:,3].astype(int)
sleep = data[:,4].astype(int)
is_active  = data[:,5]

steps5000cal150 = data[(step_count > 5000) & (calories > 150)]
print('Days with > 5000 steps and burned > 150 calories:',steps5000cal150, len(steps5000cal150), len((step_count > 5000) & (calories > 150)), sum((step_count > 5000) & (calories > 150)))

print('% of days with Sad mood: ', np.sum(mood == 'Sad') / len(mood) * 100)


print('Max number of steps on days with < 6 hrs of sleep: ', np.max(step_count[(sleep < 6)]))

sleep[is_active == 'Inactive'] 
np.mean(calories[is_active == 'Inactive'])
print('Average calories burned per hour of sleep on inactive days: ', np.mean(calories[is_active == 'Inactive']/sleep[is_active == 'Inactive']))

unique_mood = np.unique(mood)
np.mean(step_count[mood == 'Happy'])
np.mean(step_count[mood == 'Sad'])
np.mean(step_count[mood == 'Neutral'])
print( [np.mean(step_count[mood == m]) for m in np.unique(mood)])
mood_mean = [np.mean(step_count[mood ==m]) for m in np.unique(mood)]
print('mood mean values: ',mood_mean)
print('Mood with hightest average step count: ',np.max(mood_mean), unique_mood[np.argmax(mood_mean)])

print('Days with Sad mood and sleep < median sleep')


#Q longest streak where Inactive and claories < daily mean across full dataset
daily_mean_calories = np.mean(calories[is_active == 'Inactive'])
longest_streak = 0
current_streak = 0
for streak in calories[is_active == 'Inactive']:
    if streak < daily_mean_calories:
        current_streak += 1
    else:
        longest_streak = max(longest_streak,current_streak)
print('longest streak where Inactive and claories < daily mean across full dataset: ', longest_streak)