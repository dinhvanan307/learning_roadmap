# DL1 · Neural Networks và PyTorch

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** ML1–ML2 hoặc đầu vào tương đương.

**Khối lượng:** 25–40 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Giải thích tensor, layer, loss, gradient và optimizer. | PLO1 |
| CLO2 | Viết training loop cho mạng nhỏ và lưu/load checkpoint. | PLO2 |
| CLO3 | Kiểm overfit bằng train/validation curves và thử thay đổi có kiểm soát. | PLO3 |
| CLO4 | Phân biệt model tự cài, training from scratch và dùng pretrained. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. Tensor và autograd](units/01.md) | tensor/device; computation graph; backward; gradient; optimizer | Notebook có kiểm shape và gradient. |
| [2. Training loop](units/02.md) | Dataset/DataLoader; batch/epoch; loss; train/eval mode; checkpoint | Train script, config và curves. |
| [3. Generalization](units/03.md) | overfitting; regularization; dropout; augmentation; early stopping | Ablation report và error cases. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
