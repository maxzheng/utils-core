from time import sleep

from utils_core.aio import run_sync


async def test_run_sync():
    def sync_method(start_value, end_value, return_value=None):
        sync_method.check_value = start_value
        sleep(0.01)
        sync_method.check_value = end_value
        return return_value

    future = run_sync(sync_method, 0, 1, return_value=2)
    assert not future.done()
    assert sync_method.check_value == 0

    # Wait for it to finish running in the background
    sleep(0.02)
    assert sync_method.check_value == 1
    assert not future.done()

    return_value = await future
    assert return_value == 2
    assert future.done()
