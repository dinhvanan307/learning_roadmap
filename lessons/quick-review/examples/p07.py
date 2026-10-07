# Example from python/07-async.md; keep in sync with the lesson.
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
