import time
import os
from win32com import client
from win32gui import (GetWindowText, GetForegroundWindow, SetForegroundWindow,
                      EnumWindows)
from win32process import GetWindowThreadProcessId


class ActivateVenv:

    def set_cmd_to_foreground(self, hwnd, extra):
        """sets first command prompt to forgeround"""

        if "cmd.exe" in GetWindowText(hwnd):
            SetForegroundWindow(hwnd)
            return

    def get_pid(self):
        """gets process id of command prompt on foreground"""

        window = GetForegroundWindow()
        return GetWindowThreadProcessId(window)[1]

    def activate_venv(self, shell, venv_location):
        """activates venv of the active command prompt"""

        shell.AppActivate(self.get_pid())
        shell.SendKeys("cd \ {ENTER}")
        shell.SendKeys(r"cd %s {ENTER}" % venv_location)
        shell.SendKeys("activate {ENTER}")

    def run_py_script(self, shell, project_location):
        """runs the py script"""

        shell.SendKeys("cd / {ENTER}")
        shell.SendKeys("cd %s {ENTER}" % project_location)
        shell.SendKeys("python run.py {ENTER}")

    def open_cmd(self, shell):
        """ opens cmd """

        shell.run("cmd.exe")
        time.sleep(1)


def activate_venv_and_run_py_script(folder_location, virtualenv_location):
    shell = client.Dispatch("WScript.Shell")
    run_venv = ActivateVenv()
    run_venv.open_cmd(shell)
    EnumWindows(run_venv.set_cmd_to_foreground, None)
    run_venv.activate_venv(shell, virtualenv_location)
    run_venv.run_py_script(shell, folder_location)

