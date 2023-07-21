"""It uses multiprocessing and queue to create a framework which in theory can speed up your program."""
import multiprocessing
import traceback
from typing import Any, Union

class ProcessWithException(multiprocessing.Process):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """It overloads Process.__init__."""
        super().__init__(*args, **kwargs)
        self._parent_conn, self._child_conn = multiprocessing.Pipe()
        self._exception = None

    def execute_target_function(self):
        self._target(*self._args, **self._kwargs)

    def run(self) -> None:
        """It runs when ProcessWithException.start() is called."""
        try:
            self.execute_target_function()
        except Exception as e:  # pylint: disable=broad-except
            self._child_conn.send((e, traceback.format_exc()))
            # raise e  # You can still rise this exception if you need to
        else:
            self._child_conn.send(None)  # everything works

    @property
    def exception(
        self,
    ) -> Union[None, Any]:
        """It returns its exceptions to caller."""
        if self._parent_conn.poll():
            self._exception = self._parent_conn.recv()
        return self._exception
