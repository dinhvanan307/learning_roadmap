# P07 · Async, concurrency và timeout

[Mục lục](../README.md) · [Bài trước](06-python-patterns.md) · [Bài sau](08-debug-test-environment.md)

**Mục tiêu:** biết khi nào async hữu ích và cách giới hạn công việc. **Thời lượng đọc:** khoảng 20 phút.

## Kiến thức cần nhớ

Concurrency cho phép quản lý nhiều công việc chồng lấn; parallelism nói tới thực thi đồng thời trên tài nguyên tính toán. Trong mô hình asyncio thông thường, event loop luân phiên các task khi chúng nhường điều khiển. Nó không biến phép tính CPU dài thành công việc tự chạy ở lõi khác.

| Thuật ngữ | Hiểu trong bài |
| --- | --- |
| Coroutine | Gọi hàm async tạo coroutine object; cần await hoặc schedule để thực thi |
| Task | Coroutine đã được schedule vào event loop |
| `await` | Chờ awaitable; có thể nhường điều khiển khi công việc chưa hoàn thành |
| `TaskGroup` | Quản lý một nhóm task; lỗi thông thường của một task làm nhóm hủy các task còn lại và báo lỗi |
| Semaphore | Giới hạn số tác vụ vào một đoạn xử lý đồng thời |
| Timeout/cancellation | Giới hạn chờ/yêu cầu hủy; cleanup cần được thực hiện đúng |

## Ví dụ I/O giả lập, không gọi mạng

```python
import asyncio

async def main():
    semaphore = asyncio.Semaphore(2)
    state = {"active": 0, "peak": 0}

    async def fetch_note(number):
        async with semaphore:
            state["active"] += 1
            state["peak"] = max(state["peak"], state["active"])
            try:
                await asyncio.sleep(0)  # Nhường điều khiển, mô phỏng điểm chờ I/O.
                return f"note-{number}"
            finally:
                state["active"] -= 1

    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(fetch_note(i)) for i in range(4)]
    assert [task.result() for task in tasks] == [f"note-{i}" for i in range(4)]
    assert state["active"] == 0 and state["peak"] <= 2

    cleaned = asyncio.Event()
    async def never_ready():
        try:
            await asyncio.Event().wait()
        finally:
            cleaned.set()

    try:
        await asyncio.wait_for(never_ready(), timeout=0.01)
    except TimeoutError:
        assert cleaned.is_set()
    else:
        raise AssertionError("expected timeout")
    print("P07 OK: bounded tasks and timeout cleanup")

asyncio.run(main())
```

[File chạy được](../examples/p07.py). Ví dụ kiểm hành vi, không dùng số giây chạy để khẳng định tăng tốc hệ thống thực tế. `wait_for` yêu cầu hủy khi timeout; quá trình chờ cleanup có thể làm tổng thời gian vượt ngưỡng timeout.

## Lỗi dễ gặp

- Dùng `time.sleep` hay I/O blocking ngay trong async handler.
- Tạo quá nhiều task mà không có giới hạn tài nguyên.
- Bắt và nuốt cancellation, để task sống lâu hơn caller mong đợi.
- Đo workload CPU rồi kỳ vọng chỉ thêm `async` là nhanh hơn. Thread/process cần lựa chọn theo workload, thư viện và môi trường chạy.

## Tự kiểm

1. Vì sao có async function nhưng gọi nối tiếp bằng await vẫn có thể tuần tự?
2. Semaphore có làm CPU chạy song song không?
3. Nếu request bị hủy, connection/lock cần xử lý gì?

<details>
<summary>Đáp án ngắn</summary>

1. Caller chờ từng việc xong mới bắt đầu việc kế tiếp. 2. Không; semaphore giới hạn quyền vào vùng xử lý. 3. Cleanup ở finally/context manager và truyền cancellation phù hợp, không giả vờ đã thành công.

</details>

**Bài tập 20 phút:** làm một task raise lỗi; quan sát TaskGroup hủy nhóm, xác nhận active về 0. Giải thích tác dụng của finally trước khi thử tăng concurrency.

**Nguồn:** [asyncio Tasks](https://docs.python.org/3/library/asyncio-task.html), [asyncio Synchronization](https://docs.python.org/3/library/asyncio-sync.html). Đi sâu theo [A.3](../../../ROADMAP.md#a-3).
