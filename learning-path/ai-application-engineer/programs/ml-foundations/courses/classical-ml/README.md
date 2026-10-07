# ML2 · Machine Learning và Evaluation

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** ML1 hoặc kiến thức tương đương.

**Khối lượng:** 30–45 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Phân biệt supervised/unsupervised, feature/label và train/validation/test. | PLO1 |
| CLO2 | Xây pipeline preprocessing và model baseline bằng scikit-learn. | PLO2 |
| CLO3 | Đánh giá precision/recall/F1 hoặc MAE phù hợp mục tiêu, tránh leakage. | PLO3 |
| CLO4 | Giải thích error cases, overfit và điều kiện sử dụng model. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. Dữ liệu và baseline](units/01.md) | label; feature; split; leakage; preprocessing; baseline | Dataset card và baseline report. |
| [2. Fit và chọn model](units/02.md) | pipeline; fit/transform; linear/tree model; cross-validation; hyperparameter | Training script và bảng chọn model. |
| [3. Đóng gói và giải thích](units/03.md) | confusion matrix; threshold; error analysis; model card; inference contract | Model card, prediction tests và báo cáo test cuối. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
