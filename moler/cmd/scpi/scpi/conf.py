# -*- coding: utf-8 -*-
"""
SCPI command CONF module.
"""

from moler.cmd.scpi.scpi.genricscpinooutput import GenericScpiNoOutput

__author__ = 'Marcin Usielski'
__copyright__ = 'Copyright (C) 2019, Nokia'
__email__ = 'marcin.usielski@nokia.com'


class Conf(GenericScpiNoOutput):

    def __init__(self, connection, prompt=None, newline_chars=None, runner=None, params=None):
        """
        Class for command CONF for SCPI device.

        :param connection: connection to device.
        :param prompt: expected prompt sending by device after command execution. Maybe String or compiled re.
        :param newline_chars:  new line chars on device (a list).
        :param runner: runner to run command.
        :param params: parameters to add to command string.
        """
        super(Conf, self).__init__(connection=connection, prompt=prompt, newline_chars=newline_chars,
                                   runner=runner)
        self.params = params

    def build_command_string(self):
        cmd = "CONF"
        if self.params:
            cmd = "{}:{}".format(cmd, self.params)
        return cmd


COMMAND_OUTPUT_param = """CONF:FREQ 1, (@1)
SCPI>"""

COMMAND_KWARGS_param = {"params": 'FREQ 1, (@1)'}

COMMAND_RESULT_param = {}

COMMAND_OUTPUT_no_param = """CONF
SCPI>"""

COMMAND_KWARGS_no_param = {}

COMMAND_RESULT_no_param = {}