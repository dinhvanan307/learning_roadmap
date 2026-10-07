# Running project · Deep Learning và Model Adaptation

[Chương trình](../README.md) · [Dự án xuyên suốt](../../../../../projects/RUNNING_PROJECT.md)

## Mục tiêu và output

Thử nghiệm nhận diện ảnh nhỏ hoặc thích nghi model cho dữ liệu mẫu, kèm benchmark và model card.

Đây là đầu ra cần thực hiện, chưa phải sản phẩm đã có mã hoặc đã chạy. Có thể giữ code ở repo bài tập riêng và ghi commit trong bằng chứng.

## Năng lực được đánh giá

| PLO | Bằng chứng cần nộp |
| --- | --- |
| PLO1 · Giải thích tensor, autograd, training loop và khác biệt training/inference. | Sơ đồ hoặc giải thích kèm ví dụ cụ thể, chỉ ra input/output và ranh giới. |
| PLO2 · Huấn luyện một mạng nhỏ hoặc dùng mô hình pretrained có nguồn. | Artifact chạy được, README và commit tương ứng. |
| PLO3 · So sánh baseline với transfer learning/fine-tuning trên dữ liệu cố định. | Test/report cho ca đúng, ca lỗi và giới hạn kết luận. |
| PLO4 · Đóng gói checkpoint/inference và nêu trade-off tài nguyên, chất lượng. | Demo, một biến thể mới, lý do thiết kế và ghi rõ mức trợ giúp. |

## Mốc theo course

- [ ] DL1: Viết training loop cho mạng nhỏ và lưu/load checkpoint. — [yêu cầu course](../courses/neural-networks/README.md).
- [ ] DL2: Thực hiện một thử nghiệm CV nhỏ với pretrained model hoặc một thí nghiệm thích nghi model phù hợp. — [yêu cầu course](../courses/adaptation/README.md).

## Nghiệm thu

Có dataset/split/license/config/checkpoint; evaluation ngoài train; lựa chọn fine-tune được giải thích bằng evidence.

Ghi môi trường, input, lệnh chạy, expected/actual, commit, lỗi còn lại, người review và quyết định tiếp tục/bổ sung. Một artifact có thể chứng minh nhiều CLO/PLO, nhưng phải chỉ rõ phần nào hỗ trợ kết luận nào.
