from time import sleep

from promptulate.tools import BaseTool


class SleepTool(BaseTool):
    name: str = "sleep"
    description: str = "Make agent sleep for a specified number of seconds."

    def _run(
        self,
        sleep_time,
    ) -> str:
        """Use the Sleep tool."""
        sleep(int(sleep_time))
        return f"Agent slept for {sleep_time} seconds."
