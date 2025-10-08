X = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [6.2, 3.4, 5.4, 2.3],
    [5.9, 3.0, 5.1, 1.8]
]
y = [0, 0, 2, 2]

def predict(sample):
    if sample[2] < 2.0:
        return 0
    else:
        return 2

correct = 0
for i, sample in enumerate(X):
    p = predict(sample)
    print(f"Sample {i+1}: Predicted={p}, Actual={y[i]}")
    if p == y[i]:
        correct += 1

accuracy = correct / len(X)
print("Accuracy:", accuracy)
