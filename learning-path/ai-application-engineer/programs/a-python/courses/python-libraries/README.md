# A2 · Python Libraries for Data and AI

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** A1: đọc/kiểm dữ liệu và test được.

**Khối lượng:** 20–30 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Giải thích shape/dtype/axis, view/copy và cardinality khi ghép bảng. | PLO1 |
| CLO2 | Chuẩn hóa dữ liệu bằng NumPy/Pandas và tạo báo cáo thống kê. | PLO2 |
| CLO3 | Đối chiếu aggregate/merge với expected thủ công và kiểm missing/duplicate. | PLO3 |
| CLO4 | Chọn biểu đồ phù hợp, ghi nguồn và giải thích giới hạn dữ liệu. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. NumPy và phép tính](units/01.md) | ndarray; shape/dtype; broadcasting; vectorization; view/copy | Notebook hoặc script có expected nhỏ tính tay. |
| [2. Pandas và chất lượng dữ liệu](units/02.md) | DataFrame; missing values; groupby; merge; deduplication; schema | clean.csv, rejects.csv và report.json trên fixture giả lập. |
| [3. Biểu đồ và báo cáo](units/03.md) | Matplotlib Figure/Axes; Seaborn distribution; aggregation; units; outlier | Hai biểu đồ, dữ liệu đầu vào và báo cáo ngắn. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
