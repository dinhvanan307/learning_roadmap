# LLM và tích hợp model

[Danh mục concept](../docs/CONCEPTS.md) · [Roadmap](../ROADMAP.md)

**Học trong:** [D1](../learning-path/ai-application-engineer/programs/d-ai-systems/courses/llm-integration/README.md).

Các mức ưu tiên là lựa chọn của roadmap cho phạm vi ứng dụng này; không phải bảng xếp hạng độ phổ biến trên thị trường.

| Concept | Hiểu ngắn gọn | Khi dùng | Câu hỏi tự kiểm | Mức |
| --- | --- | --- | --- | --- |
| Token và tokenizer | Đơn vị biểu diễn text theo tokenizer của model, không đồng nhất với từ hoặc ký tự. | Giới hạn input, latency, chi phí. | Cùng văn bản qua hai tokenizer có cùng token count? | CORE |
| Embedding | Vector biểu diễn đối tượng theo model và mục tiêu huấn luyện. | Similarity, retrieval và features. | Vector cùng chiều nhưng khác model có so trực tiếp được không? | CORE |
| Attention và Transformer | Cơ chế kết hợp biểu diễn theo quan hệ; Transformer dùng attention trong kiến trúc model. | Hiểu biểu diễn và giới hạn tích hợp. | Có phân biệt kiến trúc với toàn bộ ứng dụng phục vụ request? | AWARENESS |
| Encoder và decoder | Vai trò biến đổi biểu diễn và sinh đầu ra; có encoder-only, decoder-only hoặc encoder–decoder. | Chọn nhóm model theo nhiệm vụ. | Không mặc định mọi LLM có cả hai khối. | AWARENESS |
| Context window và output budget | Giới hạn và phân bổ token phụ thuộc model/provider. | Hội thoại dài, RAG và tool results. | Chừa ngân sách output và xử lý context quá dài thế nào? | PRACTICE |
| Training, inference, fine-tuning | Học tham số, dùng model và điều chỉnh model bằng huấn luyện bổ sung. | Quyết định gọi API hay làm việc với model weights. | Thêm tài liệu vào prompt có đổi weights không? | CORE |
| Decoding và temperature | Cách chọn token đầu ra; tham số ảnh hưởng phân phối khi cơ chế hỗ trợ. | So sánh độ ổn định/chất lượng. | Temperature thấp có bảo đảm đúng hoặc tái lập tuyệt đối? | AWARENESS |
| Structured output và schema | Ép/kiểm hình dạng đầu ra theo contract; vẫn phải kiểm nghĩa và nghiệp vụ. | Extraction và tool arguments. | JSON đúng schema nhưng địa điểm bịa thì xử lý sao? | PRACTICE |
| Hallucination và grounding | Nội dung không được căn cứ đầy đủ; grounding nối đầu ra với dữ liệu được cung cấp. | Hỏi đáp tài liệu. | Chỉ ra nguồn hỗ trợ từng claim thay vì chỉ có link. | CORE |
| Provider abstraction | Contract thống nhất ở ứng dụng, giữ khác biệt capability qua cấu hình rõ. | Đổi model/provider và kiểm thử giả lập. | Fallback có hỗ trợ cùng schema/tool/stream không? | PRACTICE |
| Streaming và cancellation | Trả kết quả từng phần và kết thúc công việc khi client hủy. | UX phản hồi sớm và giới hạn tài nguyên. | Ngắt UI có thực sự ngắt request phía server/provider? | PRACTICE |
| Caching và routing | Tái sử dụng phần tính toán/kết quả hoặc chọn model theo policy. | Tối ưu khi đã có số đo. | Cache key, privacy, phiên bản và quality fallback có rõ? | OPTIONAL |

## Nguồn đối chiếu

[Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter1/1), [Attention Is All You Need](https://arxiv.org/abs/1706.03762), [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/).

Bảng là diễn giải phục vụ học tập; bài thực hành và câu hỏi tự kiểm là thiết kế của repo. Đọc đúng phần được chỉ trong unit, sau đó giải thích bằng code hoặc ví dụ thay vì học thuộc bảng.
