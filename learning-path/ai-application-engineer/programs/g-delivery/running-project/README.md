# Running project · Deployment, DevOps và LLMOps

[Chương trình](../README.md) · [Dự án xuyên suốt](../../../../../projects/RUNNING_PROJECT.md)

## Mục tiêu và output

Bản release trên một môi trường được chọn, CI/CD, dashboard/report vận hành, backup/restore và runbook.

Đây là đầu ra cần thực hiện, chưa phải sản phẩm đã có mã hoặc đã chạy. Có thể giữ code ở repo bài tập riêng và ghi commit trong bằng chứng.

## Năng lực được đánh giá

| PLO | Bằng chứng cần nộp |
| --- | --- |
| PLO1 · Giải thích cấu hình runtime, network, container, storage và secret. | Sơ đồ hoặc giải thích kèm ví dụ cụ thể, chỉ ra input/output và ranh giới. |
| PLO2 · Triển khai một môi trường có build/release và quy trình rollback rõ. | Artifact chạy được, README và commit tương ứng. |
| PLO3 · Theo dõi chất lượng, độ trễ, lỗi, chi phí và khả năng phục hồi. | Test/report cho ca đúng, ca lỗi và giới hạn kết luận. |
| PLO4 · Quản lý thay đổi model/prompt/data và nêu khi nào cần mở rộng hạ tầng. | Demo, một biến thể mới, lý do thiết kế và ghi rõ mức trợ giúp. |

## Mốc theo course

- [ ] G1: Đóng gói app và triển khai trên một target với cấu hình tách khỏi code. — [yêu cầu course](../courses/devops/README.md).
- [ ] G2: Theo dõi request/model/prompt/dataset version cùng latency và cost. — [yêu cầu course](../courses/llmops/README.md).

## Nghiệm thu

Có bằng chứng deploy/health, rollback app/config và restore dữ liệu thử nghiệm; monitor chất lượng AI ngoài uptime; chưa triển khai thì ghi NOT_TESTED.

Ghi môi trường, input, lệnh chạy, expected/actual, commit, lỗi còn lại, người review và quyết định tiếp tục/bổ sung. Một artifact có thể chứng minh nhiều CLO/PLO, nhưng phải chỉ rõ phần nào hỗ trợ kết luận nào.
