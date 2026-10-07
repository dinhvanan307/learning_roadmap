# AI02 · Dữ liệu, training và đánh giá

[Mục lục](../README.md) · [Bài trước](01-ai-map.md) · [Bài sau](03-llm-basics.md)

**Mục tiêu:** đọc một kết quả model và biết cần hỏi gì trước khi tin. **Thời lượng đọc:** khoảng 20 phút.

## Model học gì?

**Feature** là đầu vào dùng để dự đoán; **label** là mục tiêu đã biết trong supervised learning. **Parameters** là giá trị học được; **hyperparameters** là cấu hình cách học/mô hình do quá trình thiết kế/chọn cấu hình quyết định. **Loss** đo mức sai để thuật toán tối ưu tham số; **metric** báo chất lượng theo mục tiêu đánh giá. Loss và metric có thể khác nhau.

Trong neural network, các layer biến đổi biểu diễn qua weights và activation. Gradient mô tả độ thay đổi của loss theo parameters; optimizer dùng thông tin này để cập nhật, learning rate điều chỉnh độ lớn bước. Một batch là nhóm mẫu xử lý trong một bước; một epoch thường là một lượt qua tập train. Ở lượt ôn này cần giải thích được luồng, chưa cần tự cài backpropagation.

```mermaid
flowchart LR
  X["Dữ liệu train"] --> F["Model dự đoán"]
  F --> L["Loss so với nhãn"]
  L --> U["Optimizer cập nhật parameters"]
  U --> F
```

Đây là sơ đồ ý tưởng của supervised training, không phải quy trình duy nhất của mọi AI.

| Tập dữ liệu | Dùng để làm gì | Điều cần tránh |
| --- | --- | --- |
| Train | Fit model và các bước preprocessing cần học từ dữ liệu | Dùng nhãn/thông tin không tồn tại lúc inference |
| Validation/dev | Chọn cấu hình, threshold, prompt hoặc phương án | Gọi điểm trên dev là đánh giá độc lập cuối cùng |
| Test | Đánh giá sau khi đã chốt lựa chọn | Xem điểm rồi tune tiếp và vẫn coi test chưa bị dùng |

**Overfitting:** học tốt đặc điểm của train nhưng tổng quát hóa kém. **Underfitting:** model/cách học chưa nắm đủ quan hệ cần thiết. **Leakage:** thông tin ngoài phạm vi hợp lệ lọt vào quá trình học/chọn model. Ví dụ cùng tài liệu được chia thành các bản gần trùng nằm cả train lẫn test. Preprocessing cần fit trên train rồi áp dụng sang dev/test; cách split phải xét thời gian, nhóm người dùng hoặc tài liệu nếu dữ liệu có phụ thuộc.

## Accuracy chưa đủ

Với nhãn dương = “cần hỗ trợ”, TP là đoán cần và thực tế cần; FP là báo nhầm; FN là bỏ sót; TN là đoán không cần đúng. Accuracy đếm tỷ lệ đúng; precision hỏi trong các ca báo dương có bao nhiêu đúng; recall hỏi tìm được bao nhiêu ca dương thật. F1 là trung bình điều hòa precision/recall.

```python
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
```

[File chạy được](../examples/ai02.py). Dự đoán tất cả âm đạt 90% accuracy nhưng bỏ sót toàn bộ người cần hỗ trợ. Đây là tính metric từ prediction mẫu, không phải model được huấn luyện.

## Tự kiểm

1. Vì sao nên có majority/rule baseline trước model phức tạp?
2. Một model có train score cao hơn nhưng test thấp hơn cho thấy điều gì?
3. Đổi prompt sau khi xem test failures có còn là test độc lập không?

<details>
<summary>Đáp án ngắn</summary>

1. Để biết độ phức tạp có tạo cải thiện hay không. 2. Có thể tổng quát hóa kém; cần xem split, mẫu, metric và lỗi trước khi kết luận nguyên nhân. 3. Không còn cho lần lựa chọn đó; cần dữ liệu đánh giá chưa dùng để tune.

</details>

**Bài tập 15 phút:** tự tạo bốn prediction có TP/FP/FN/TN; tính precision, recall và F1 bằng tay. Chọn metric ưu tiên theo tác hại của báo nhầm và bỏ sót.

**Nguồn:** [scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html), [Google Classification Metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall), [Google Neural Networks](https://developers.google.com/machine-learning/crash-course/neural-networks). Đi sâu theo [D.5](../../../ROADMAP.md#d-5) và [E.2](../../../ROADMAP.md#e-2).
