

X = [
    [5.1, 3.5],
    [4.9, 3.0],
    [6.2, 3.4],
    [5.9, 3.0]
]
y = [0, 0, 1, 1]

def predict(sample):
    if sample[0] <= 5.0:
        return 0
    else:
        return 1

correct = 0
for i, sample in enumerate(X):
    pred = predict(sample)
    print(f"Sample {i+1} prediction: {pred}, Actual: {y[i]}")
    if pred == y[i]:
        correct += 1

accuracy = correct / len(X)
print("Accuracy:", accuracy)
