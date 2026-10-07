# Machine Learning và Deep Learning

[Danh mục concept](../docs/CONCEPTS.md) · [Roadmap](../ROADMAP.md)

**Học trong:** [ML1](../learning-path/ai-application-engineer/programs/ml-foundations/courses/math/README.md), [ML2](../learning-path/ai-application-engineer/programs/ml-foundations/courses/classical-ml/README.md), [DL1](../learning-path/ai-application-engineer/programs/dl-foundations/courses/neural-networks/README.md), [DL2](../learning-path/ai-application-engineer/programs/dl-foundations/courses/adaptation/README.md).

Các mức ưu tiên là lựa chọn của roadmap cho phạm vi ứng dụng này; không phải bảng xếp hạng độ phổ biến trên thị trường.

| Concept | Hiểu ngắn gọn | Khi dùng | Câu hỏi tự kiểm | Mức |
| --- | --- | --- | --- | --- |
| Feature và label | Đầu vào dùng để dự đoán và đích học cần xác định rõ. | Thiết kế bài toán supervised. | Feature có vô tình chứa kết quả chỉ biết sau sự kiện? | CORE |
| Fit, transform và pipeline | Học tham số biến đổi, áp dụng biến đổi và ghép các bước. | Preprocessing không leakage. | Scaler được fit trên train hay toàn bộ dữ liệu? | PRACTICE |
| Loss và objective | Hàm đo sai lệch để tối ưu, có thể khác metric nghiệm thu. | Training và chọn model. | Loss thấp hơn có chắc recall nhóm quan trọng cao hơn? | CORE |
| Gradient và autograd | Đạo hàm chỉ hướng biến đổi; autograd tính qua computation graph. | Học bằng gradient descent. | Gradient đã được reset đúng bước chưa? | PRACTICE |
| Batch, epoch và learning rate | Nhóm mẫu, một lượt qua data và bước cập nhật tham số. | Điều khiển training. | Tăng batch có làm thay điều kiện so sánh? | PRACTICE |
| Overfitting và regularization | Học quá sát train; các biện pháp giới hạn/hướng quá trình học để khái quát. | Chênh train/validation. | Cải thiện chỉ có trên train hay cả held-out data? | PRACTICE |
| Training from scratch | Khởi tạo và học weights cho bài toán/model, khác với tự viết code gọi pretrained. | Nghiên cứu model nhỏ để hiểu cơ chế. | Mô tả rõ cái gì tự viết và weights có sẵn hay chưa. | AWARENESS |
| Transfer learning và fine-tuning | Dùng tri thức pretrained; fine-tuning cập nhật một phần/toàn bộ weights. | Dữ liệu hạn chế, nhiệm vụ chuyên biệt. | Baseline frozen model đã được đo trước? | PRACTICE |
| LoRA/PEFT | Học một tập tham số thích nghi nhỏ thay vì cập nhật toàn bộ model. | Fine-tuning phù hợp giới hạn tài nguyên. | Adapter gắn với base model/version nào? | OPTIONAL |
| Quantization và distillation | Giảm độ chính xác biểu diễn số; hoặc học model học trò từ tín hiệu model thầy. | Giảm tài nguyên inference/training tùy kỹ thuật. | Đo giảm tài nguyên cùng mất mát chất lượng chưa? | AWARENESS |
| Checkpoint và model card | Lưu trạng thái/model; mô tả dữ liệu, mục đích, metric, giới hạn và điều kiện dùng. | Tái lập, bàn giao và deploy. | Load lại có đủ tokenizer/preprocessing/config không? | PRACTICE |
| Data/model drift | Thay đổi phân bố dữ liệu hoặc quan hệ khiến chất lượng triển khai đổi. | Theo dõi sau release. | Có nhãn/metric phù hợp để phát hiện thay vì chỉ đo input? | AWARENESS |

## Nguồn đối chiếu

[scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html), [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html), [PyTorch Transfer Learning](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html), [Hugging Face LoRA](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora).

Bảng là diễn giải phục vụ học tập; bài thực hành và câu hỏi tự kiểm là thiết kế của repo. Đọc đúng phần được chỉ trong unit, sau đó giải thích bằng code hoặc ví dụ thay vì học thuộc bảng.
