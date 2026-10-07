# Running project · Machine Learning Foundations

[Chương trình](../README.md) · [Dự án xuyên suốt](../../../../../projects/RUNNING_PROJECT.md)

## Mục tiêu và output

Mô hình phân loại dữ liệu mẫu công khai hoặc tổng hợp, kèm model card và evaluation.

Đây là đầu ra cần thực hiện, chưa phải sản phẩm đã có mã hoặc đã chạy. Có thể giữ code ở repo bài tập riêng và ghi commit trong bằng chứng.

## Năng lực được đánh giá

| PLO | Bằng chứng cần nộp |
| --- | --- |
| PLO1 · Giải thích vector, xác suất, loss và mục tiêu tối ưu trong một bài toán nhỏ. | Sơ đồ hoặc giải thích kèm ví dụ cụ thể, chỉ ra input/output và ranh giới. |
| PLO2 · Tạo baseline và pipeline học máy từ dữ liệu có nhãn. | Artifact chạy được, README và commit tương ứng. |
| PLO3 · Đánh giá không leakage, phân tích lỗi và so sánh với giải pháp đơn giản. | Test/report cho ca đúng, ca lỗi và giới hạn kết luận. |
| PLO4 · Giải thích lựa chọn feature/model và đóng gói inference có contract. | Demo, một biến thể mới, lý do thiết kế và ghi rõ mức trợ giúp. |

## Mốc theo course

- [ ] ML1: Dùng thống kê/xác suất mô tả phân bố và độ bất định trong mẫu. — [yêu cầu course](../courses/math/README.md).
- [ ] ML2: Xây pipeline preprocessing và model baseline bằng scikit-learn. — [yêu cầu course](../courses/classical-ml/README.md).

## Nghiệm thu

Split cố định; preprocessing fit trên train; baseline và candidate đo trên cùng test; lưu model/config/version.

Ghi môi trường, input, lệnh chạy, expected/actual, commit, lỗi còn lại, người review và quyết định tiếp tục/bổ sung. Một artifact có thể chứng minh nhiều CLO/PLO, nhưng phải chỉ rõ phần nào hỗ trợ kết luận nào.
