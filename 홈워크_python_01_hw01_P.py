score = {
    'python': 80,
    'django': 89,
    'web': 83,
}

score['alghrithm'] = 90
score['python'] = 85


score_value_list = list(score.values())
sum_score = 0

for i in range(len(score_value_list)):
    sum_score += score_value_list[i]

avg_score = sum_score / len(score_value_list)
print(avg_score)
