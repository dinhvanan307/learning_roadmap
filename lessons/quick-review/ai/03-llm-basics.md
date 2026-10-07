# AI03 · LLM, token, attention và context

[Mục lục](../README.md) · [Bài trước](02-learning-and-evaluation.md) · [Bài sau](04-prompt-context-memory.md)

**Mục tiêu:** giải thích luồng sinh câu trả lời mà chưa cần cài Transformer. **Thời lượng đọc:** khoảng 15 phút.

## Luồng khái quát của một autoregressive language model

```text
Text → tokenizer → token IDs → biểu diễn số → các tầng model
     → phân bố token kế tiếp → chọn token → ghép vào chuỗi → lặp
```

Sơ đồ mô tả một kiểu sinh văn bản phổ biến, không đại diện tất cả kiến trúc/model hoặc toàn bộ runtime của sản phẩm AI.

| Concept | Cần hiểu |
| --- | --- |
| Token/tokenizer | Token là đơn vị model dùng; có thể là phần từ, dấu hoặc chuỗi khác, không luôn bằng một từ |
| Embedding | Biểu diễn vector học được; token embedding trong model và embedding cho tìm kiếm có mục tiêu/cách tạo khác nhau |
| Attention | Cơ chế kết hợp thông tin giữa các vị trí dựa trên mức liên quan tính được; không phải bằng chứng model đã hiểu đúng sự thật |
| Transformer | Họ kiến trúc dùng attention cùng các thành phần khác; các biến thể có cách sử dụng khác nhau |
| Encoder | Thường dùng để tạo biểu diễn input cho các tác vụ như phân loại/trích xuất |
| Decoder | Trong model sinh tự hồi quy, tạo token theo context đã có |
| Encoder-decoder | Mã hóa input rồi giải mã output; thường gặp ở tác vụ biến đổi chuỗi |
| Context window | Giới hạn thông tin model có thể xử lý trong một lần theo thiết kế/API; phải tính ngân sách input và output phù hợp |

Pretraining học tham số từ dữ liệu nền; fine-tuning tiếp tục cập nhật tham số/adapter cho mục tiêu phù hợp. Đưa tài liệu vào prompt thường chỉ thay input của lần suy luận, không cập nhật weights.

## Sampling và độ tin cậy

Decoder tạo phân bố token; cơ chế chọn token có thể dùng các thiết lập như temperature/top-p. Temperature điều chỉnh phân bố lấy mẫu, không phải nút tăng trí thông minh. Thiết lập ít ngẫu nhiên hơn cũng không bảo đảm câu trả lời đúng hoặc luôn tái lập tuyệt đối trên mọi hệ thống.

**Hallucination** trong thực hành là output có vẻ hợp lý nhưng sai hoặc không có căn cứ phù hợp. Văn phong chắc chắn, JSON hợp lệ hay câu trả lời dài đều không thay thế kiểm chứng nội dung.

## Một ví dụ cần tự phân tích

Input: “Tài liệu của tôi có quy định thời hạn nộp bài không?” nhưng ứng dụng chưa cung cấp tài liệu và chưa có tool truy cập. Output: “Bạn phải nộp trước thứ Sáu.”

Thiếu thành phần nào? Model không có nguồn để kết luận quy định riêng. Ứng dụng cần dữ liệu liên quan hoặc trả lời rằng chưa đủ thông tin; tăng context window mà không đưa đúng dữ liệu vào cũng không giải quyết được.

## Tự kiểm

1. Có phải mọi LLM đều có cả encoder và decoder?
2. Model thấy tài liệu trong prompt có đồng nghĩa đã được training lại?
3. Một câu ngắn hơn có luôn ít token hơn trên mọi tokenizer không?

<details>
<summary>Đáp án ngắn</summary>

1. Không, có các họ kiến trúc khác nhau. 2. Không. 3. Không thể suy chỉ từ số từ/ký tự; phải dùng tokenizer tương ứng nếu cần số chính xác.

</details>

**Bài tập 10 phút:** vẽ ba hộp model, context và ứng dụng; đặt “lịch sử hội thoại”, “weights”, “file dữ liệu” và “tool thực thi” vào nơi phù hợp. Nêu trường hợp file phải được nạp vào context hoặc truy xuất trước khi model dùng được.

**Nguồn:** [How Transformers work](https://huggingface.co/learn/llm-course/en/chapter1/4), [Tokenizers](https://huggingface.co/learn/llm-course/en/chapter2/4). Đi sâu theo [D.1](../../../ROADMAP.md#d-1).
