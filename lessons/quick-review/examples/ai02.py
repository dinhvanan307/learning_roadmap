# Example from ai/02-learning-and-evaluation.md; keep in sync with the lesson.
truth = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
prediction = [0] * 10
tp = sum(y == 1 and p == 1 for y, p in zip(truth, prediction))
fp = sum(y == 0 and p == 1 for y, p in zip(truth, prediction))
fn = sum(y == 1 and p == 0 for y, p in zip(truth, prediction))
accuracy = sum(y == p for y, p in zip(truth, prediction)) / len(truth)
# Quy ước riêng cho demo: mẫu số bằng 0 thì metric trả 0.
precision = tp / (tp + fp) if tp + fp else 0.0
recall = tp / (tp + fn) if tp + fn else 0.0
assert accuracy == 0.9 and recall == 0.0
print(f"AI02: accuracy={accuracy:.1f}, precision={precision:.1f}, recall={recall:.1f}")
