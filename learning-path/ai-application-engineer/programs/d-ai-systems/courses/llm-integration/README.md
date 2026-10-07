# D1 · LLM Architecture và Integration

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** API, async và kiểm thử; ôn vector/xác suất nếu cần.

**Nhập môn trước course:** [6 bài AI cơ bản](../../../../../../lessons/quick-review/ai/01-ai-map.md), đi từ AI/ML và evaluation đến LLM, context, RAG và agent. Phần đọc nhập môn không yêu cầu hoàn thành backend; course triển khai này vẫn cần đầu vào nêu trên.

**Khối lượng:** 25–40 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Mô tả token, embedding, attention, encoder/decoder và context window ở mức tích hợp. | PLO1 |
| CLO2 | Tạo adapter model với schema output, timeout và dữ liệu lỗi giả lập. | PLO2 |
| CLO3 | So sánh baseline và cấu hình model trên cùng bộ input có số đo. | PLO3 |
| CLO4 | Giải thích trade-off quality/latency/cost và giới hạn của structured output. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. Model và biểu diễn](units/01.md) | tokenization; vector/cosine; attention; Transformer; encoder; decoder; pretraining/inference | Sơ đồ và ví dụ tính cosine trên vector nhỏ. |
| [2. Provider adapter](units/02.md) | prompt/messages; structured output; schema validation; timeout; fallback; rate limit | Adapter và contract tests; config mẫu không secret. |
| [3. Đánh giá tích hợp](units/03.md) | baseline; dev/test; exact match/rubric; p50/p95; token usage; cost; model version | Model-selection report và dữ liệu có version. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
