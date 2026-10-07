# DL2 · Computer Vision và Fine-tuning

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** DL1, dữ liệu được phép và ngân sách tính toán được chốt.

**Khối lượng:** 25–45 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Chọn transfer learning hay fine-tuning dựa vào lỗi và dữ liệu. | PLO1 |
| CLO2 | Thực hiện một thử nghiệm CV nhỏ với pretrained model hoặc một thí nghiệm thích nghi model phù hợp. | PLO2 |
| CLO3 | Đo chất lượng trước/sau cùng latency và tài nguyên. | PLO3 |
| CLO4 | Giải thích khi nào không fine-tune, phân biệt LoRA, quantization và distillation. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. Chọn cách thích nghi](units/01.md) | pretrained; frozen backbone; classifier head; transfer learning; data quality | Experiment brief và điều kiện dừng. |
| [2. Thử nghiệm có giới hạn](units/02.md) | fine-tuning; learning rate; batch size; compute budget; adapter/LoRA ở mức nhận biết | Training/eval report; nếu thiếu tài nguyên ghi NOT_TESTED và giữ thiết kế thí nghiệm. |
| [3. Inference và bàn giao](units/03.md) | export/checkpoint; batching; quantization; distillation; model card; license | Demo inference, model card và decision note. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
