from sklearn.metrics import precision_score


y_test = [1, 0, 0, 1]

y_pred = [1, 0, 0, 1]

pre_val = precision_score(y_true=y_test, y_pred=y_pred)

print(pre_val)