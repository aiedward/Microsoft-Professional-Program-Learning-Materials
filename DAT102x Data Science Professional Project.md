## Ho to inteprete Negative Feature Importance
A negative score is returned when a random permutation of a feature’s values results in a better performance metric (higher accuracy or a lower error, etc..) compared to the performance before a permutation is applied.

In general, features with higher importance scores are more sensitive to random shuffling of their values, which means they are more ‘important’ for prediction. Beware that the shuffling is performed for one feature at a time, and although a feature might seem unnecessary or less important because of its low (or negative) importance score, it could be the case that it is correlated to other features that can still produce a ‘good’ performance result.
