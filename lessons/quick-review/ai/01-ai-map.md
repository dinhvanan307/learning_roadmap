# AI01 · AI, Machine Learning, Deep Learning và LLM

[Mục lục](../README.md) · [Ôn Python](../python/08-debug-test-environment.md) · [Bài sau](02-learning-and-evaluation.md)

**Mục tiêu:** đặt đúng tên bài toán và thành phần đang dùng. **Thời lượng đọc:** khoảng 10–15 phút.

## Bản đồ khái niệm

| Khái niệm | Hiểu ngắn gọn | Ví dụ |
| --- | --- | --- |
| AI | Lĩnh vực rộng về hệ thống thực hiện nhiệm vụ cần các năng lực như nhận biết, suy luận, lập kế hoạch | Trợ lý, hệ nhận diện hoặc bộ lập kế hoạch |
| Machine Learning — ML | Học quy luật/tham số từ dữ liệu để thực hiện nhiệm vụ | Phân loại thư rác từ email đã gắn nhãn |
| Deep Learning — DL | Nhóm phương pháp ML dùng neural network nhiều tầng | Mô hình ảnh hoặc ngôn ngữ |
| Generative AI — GenAI | Hệ thống sinh nội dung như văn bản/ảnh/âm thanh | Soạn bản nháp từ yêu cầu |
| Large Language Model — LLM | Mô hình ngôn ngữ lớn; có thể dùng để sinh, phân loại, trích xuất và nhiều tác vụ ngôn ngữ | Trích trường từ ghi chú hoặc trả lời câu hỏi |

AI rộng hơn ML, ML rộng hơn DL. GenAI mô tả khả năng/mục tiêu sinh nội dung; không nên coi mọi khái niệm trong bảng là các tầng nối tiếp tuyệt đối. Một ứng dụng LLM còn có code, dữ liệu, giao diện và cơ chế kiểm tra.

## Các loại bài toán nền tảng

- **Classification:** dự đoán nhãn rời rạc, ví dụ “Python / SQL / khác”.
- **Regression:** dự đoán giá trị số, ví dụ thời lượng hoàn thành bài.
- **Clustering:** nhóm các mẫu có đặc trưng tương tự mà không dùng sẵn nhãn nhóm như supervised classification.
- **Generation:** tạo nội dung, ví dụ giải thích một đoạn code.
- **Reinforcement learning:** học cách hành động qua tín hiệu reward trong tương tác; chỉ cần nhận biết ở lượt ôn này.

**Model** là thành phần đã có cấu trúc/tham số để xử lý input. **Training** điều chỉnh tham số qua dữ liệu và mục tiêu học; **inference** dùng model để tạo prediction/output. Chỉ gọi API không có nghĩa là đang tự training model.

## Ví dụ chọn công cụ

| Nhu cầu của ứng dụng học tập | Điểm bắt đầu hợp lý |
| --- | --- |
| Tổng số phút học, ID có trùng không | Code/rule xác định, unit tests |
| Dự đoán chủ đề từ nhiều ghi chú đã gắn nhãn | Baseline rồi thử model phân loại |
| Giải thích đoạn code bằng tiếng Việt | LLM, kèm kiểm lại tính đúng |
| Trả lời nội quy từ tài liệu được cung cấp | Tra cứu nguồn; cân nhắc RAG khi cần sinh câu trả lời |

Bảng là bài tập lựa chọn phương pháp, không khẳng định một model luôn thắng. Bắt đầu từ tiêu chí đúng/sai và baseline dễ kiểm.

## Tự kiểm

1. Tính tổng số phút bằng Python có cần dùng LLM không?
2. Dùng một pretrained model để gắn nhãn là training hay inference?
3. Một câu trả lời đúng ngữ pháp có đủ chứng minh đúng sự thật không?

<details>
<summary>Đáp án ngắn</summary>

1. Không; phép tính có contract xác định. 2. Inference nếu không cập nhật tham số. 3. Không, cần đối chiếu dữ kiện hoặc oracle phù hợp.

</details>

**Bài tập 10 phút:** chọn ba việc bạn đang làm, ghi input → output → cách kiểm → baseline không dùng AI. Chỉ đề xuất AI ở nơi baseline có giới hạn cụ thể.

**Nguồn:** [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course), [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter1/1). Liên hệ [Phase D](../../../ROADMAP.md#phase-d).
