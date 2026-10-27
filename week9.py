import numpy as np
from scipy import stats
from scipy.stats import bernoulli, binom
from statsmodels.stats.weightstats import ztest

print("----- Bernoulli Distribution -----")

p = 0.7
bernoulli_samples = bernoulli.rvs(p, size=10)
print("Probability of Passing:", p)
print("Student Outcomes (1=Pass, 0=Fail):")
print(bernoulli_samples)
print("\nProbability of Pass:")
print(bernoulli.pmf(1, p))
print("Probability of Fail:")
print(bernoulli.pmf(0, p))

print("\n\n----- Binomial Distribution -----")

n = 10

p = 0.7

k = 8
binomial_probability = binom.pmf(k, n, p)
print("Number of Students:", n)
print("Probability of Passing:", p)
print(f"\nProbability that exactly {k} students pass:")
print(binomial_probability)

random_binomial = binom.rvs(n, p, size=5)
print("\nRandom Binomial Outcomes:")
print(random_binomial)

print("----- Z-Test -----")

sample_marks = np.array([78, 82, 85, 88, 90, 76, 95, 89, 84, 91])

population_mean = 80

z_stat, p_value = ztest(sample_marks, value=population_mean)
print("Sample Marks:")
print(sample_marks)
print("\nPopulation Mean:", population_mean)
print("\nZ-Statistic:", z_stat)
print("P-Value:", p_value)
# Decision
alpha = 0.05
if p_value < alpha:
    print("\nResult: Reject Null Hypothesis")
else:
    print("\nResult: Fail to Reject Null Hypothesis")

print("\n\n----- Independent t-Test -----")

class_A = np.array([78, 82, 85, 88, 90])
class_B = np.array([72, 75, 70, 68, 74])

t_stat, p_value = stats.ttest_ind(class_A, class_B)
print("Class A Marks:")
print(class_A)
print("\nClass B Marks:")
print(class_B)
print("\nt-Statistic:", t_stat)
print("P-Value:", p_value)
# Decision
if p_value < alpha:
    print("\nResult: Reject Null Hypothesis")
else:
    print("\nResult: Fail to Reject Null Hypothesis")
