import asyncio

class Timer:
    def __init__(self, timeout : float, callback, callback_args = (), callback_kwargs = {}):
        """An asynchronous Timer object.
        
        Parameters
        -----------
        timeout: :class:`float`:
        The duration for which the timer should last.

        callback: :class:`Coroutine` or `Method`:
        An `asyncio` coroutine or a regular method that will be called as soon as the timer ends.

        callback_args: Optional[:class:`tuple`]:
        The args to be passed to the callback.

        callback_kwargs: Optional[:class:`dict`]:
        The kwargs to be passed to the callback. 
        """
        self._timeout = timeout
        self._callback = callback
        self._task = asyncio.ensure_future(self._job())
        self._callback_args = callback_args
        self._callback_kwargs = callback_kwargs
        

    async def _job(self):
        await asyncio.sleep(self._timeout)
        await self._call_callback()

    async def _call_callback(self):
        if asyncio.iscoroutine(self._callback):
            await self._callback(*self._callback_args, **self._callback_kwargs)
        else:
            self._callback(*self._callback_args, **self._callback_kwargs)

    def cancel(self):
        """
        Cancels the timer. The callback will not be called.
        """
        self._task.cancel()
 
    def end_early(self):
        """
       Ends the timer early, and calls the callback coroutine.
       """
        self._task.cancel()
        asyncio.ensure_future(self._call_callback())
