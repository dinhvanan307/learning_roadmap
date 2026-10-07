# Bảng năng lực tham chiếu

Tám nhóm năng lực dưới đây được chuyển từ dashboard gốc. L1/L2/L3 là các mức mô tả của kế hoạch để tìm phần cần học và trao đổi với reviewer; không phải chuẩn nghề nghiệp đã được xác nhận.

## Tiêu chí từng nhóm

### D1 — LLM Foundations & Model Selection

**Vai trò trong rubric gốc:** nhóm bổ sung vào đánh giá tổng thể.

- **L1:** Biết gọi API, hiểu token/temperature
- **L2:** Chọn model theo ma trận cost/latency/quality có số liệu TỰ CHẠY; hiểu tokenizer, context window, reasoning vs non-reasoning, structured output, caching
- **L3:** Model portfolio đa nhà cung cấp, routing động, tự host open-weight

### D2 — Prompt & Context Engineering

**Vai trò trong rubric gốc:** nhóm bổ sung vào đánh giá tổng thể.

- **L1:** Viết prompt theo mẫu
- **L2:** System prompt có cấu trúc, few-shot có chủ đích, context budgeting, compaction, tool-result shaping; ĐO được prompt nào tốt hơn
- **L3:** Prompt framework tái sử dụng cho tổ chức, tự động tối ưu prompt

### D3 — Application Architecture

**Vai trò trong rubric gốc:** nhóm bắt buộc.

- **L1:** Gắn LLM vào 1 endpoint
- **L2:** Kiến trúc AI service tách lớp (provider abstraction, streaming, queue, state store); async/background job; multi-tenant; versioning prompt & model
- **L3:** Nền tảng AI dùng chung nhiều sản phẩm, microservice + event-driven

### D4 — RAG & Knowledge Systems

**Vai trò trong rubric gốc:** nhóm bổ sung vào đánh giá tổng thể.

- **L1:** Naive RAG với vector DB
- **L2:** Hybrid search (BM25+vector) + reranking + chunking strategy có đo; citation; ingestion pipeline; xử lý được 7 failure mode của RAG
- **L3:** GraphRAG, agentic retrieval, multi-corpus governance, retrieval eval harness

### D5 — Agent Systems

**Vai trò trong rubric gốc:** nhóm bắt buộc.

- **L1:** Dùng tool calling đơn giản
- **L2:** Thiết kế agent loop (plan–act–observe), state machine/graph, tool design, MCP server/client, HITL, error recovery, sub-agent delegation
- **L3:** Multi-agent orchestration quy mô lớn, A2A, agent governance & sandbox

### D6 — Fine-tuning & Customization

**Vai trò trong rubric gốc:** nhóm bổ sung vào đánh giá tổng thể.

- **L1:** Biết fine-tune là gì
- **L2:** Quyết định đúng khi nào KHÔNG fine-tune; chạy được LoRA/QLoRA trên open-weight, chuẩn bị dataset, đánh giá trước/sau, serve model đã tune
- **L3:** Distillation, RLHF/DPO, tối ưu serving (vLLM, quantization)

### D7 — Evaluation & Observability

**Vai trò trong rubric gốc:** nhóm bắt buộc.

- **L1:** Test thủ công
- **L2:** Eval-driven development: golden dataset, LLM-as-judge có calibrate, regression suite trong CI, tracing/span, dashboard chất lượng + cost
- **L3:** Online eval, A/B, canary theo chất lượng, eval platform nội bộ

### D8 — Production Ops: Security, Cost, Scale

**Vai trò trong rubric gốc:** nhóm bổ sung vào đánh giá tổng thể.

- **L1:** Deploy được
- **L2:** Phòng prompt injection & data exfiltration, tool permission model, PII redaction, rate limit, cost per request/tenant, fallback & degradation, SLO
- **L3:** Threat model toàn hệ, cost forecasting, compliance, multi-region

## Kết quả review

| Nhóm | Mức tự đánh giá | Mức sau review | Bằng chứng | Người review và ngày |
| --- | --- | --- | --- | --- |
| D1 — LLM Foundations & Model Selection | UNKNOWN | Chưa review | — | — |
| D2 — Prompt & Context Engineering | UNKNOWN | Chưa review | — | — |
| D3 — Application Architecture | UNKNOWN | Chưa review | — | — |
| D4 — RAG & Knowledge Systems | UNKNOWN | Chưa review | — | — |
| D5 — Agent Systems | UNKNOWN | Chưa review | — | — |
| D6 — Fine-tuning & Customization | UNKNOWN | Chưa review | — | — |
| D7 — Evaluation & Observability | UNKNOWN | Chưa review | — | — |
| D8 — Production Ops: Security, Cost, Scale | UNKNOWN | Chưa review | — | — |

## Cách dùng rubric

Dashboard đặt mục tiêu L2 ở ít nhất 6/8 nhóm, trong đó D3, D5 và D7 bắt buộc. Repo giữ ngưỡng này như mục tiêu nội bộ để review, không suy ra nhãn Middle/Senior tự động từ điểm tự chấm.

Mỗi kết luận cần trỏ đến bài làm, kết quả chạy và phần giải thích của người học. Ghi rõ mức trợ giúp. Khi thiếu bằng chứng, để `UNKNOWN` hoặc ghi phần còn thiếu; chưa chấm không có nghĩa là đạt mức 0.
