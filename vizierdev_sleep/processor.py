# Copyright (C) 2017-2019 New York University,
#                         University at Buffalo,
#                         Illinois Institute of Technology.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

from vizier.engine.task.processor import ExecResult, TaskProcessor
from vizier.viztrail.module.output import ModuleOutputs, TextOutput
from vizier.viztrail.module.provenance import ModuleProvenance


class SleepTaskProcessor(TaskProcessor):
    """Implementation of the task processor for the Sleep cell package."""
    def compute(self, command_id, arguments, context):
        """Execute the Python script that is contained in the given arguments.

        Parameters
        ----------
        command_id: string
            Unique identifier for a command in a package declaration
        arguments: vizier.viztrail.command.ModuleArguments
            User-provided command arguments
        context: vizier.engine.task.base.TaskContext
            Context in which a task is being executed

        Returns
        -------
        vizier.engine.task.processor.ExecResult
        """
        if command_id == 'sleep':
            return self.execute_sleep(
                args=arguments,
                context=context
            )
        else:
            raise ValueError('unknown command \'' + str(command_id) + '\'')

    def execute_sleep(self, args, context):
        """Execute the sleep commandt. Goes to sleep for a specified time.
        Print text before and after sleep to standard output if verbose.

        Parameters
        ----------
        args: vizier.viztrail.command.ModuleArguments
            User-provided command arguments
        context: vizier.engine.task.base.TaskContext
            Context in which a task is being executed

        Returns
        -------
        vizier.engine.task.processor.ExecResult
        """
        # Get sleep interval and the value of the verbose argument
        interval = args.get_value('time')
        verbose = args.get_value('verbose', default_value=False)
        # Initialize the output object
        outputs = ModuleOutputs()
        # Print message before going to sleep if verbose
        if verbose:
            line = TextOutput('Go to sleep for ' + str(interval) + ' sec.')
            outputs.stdout.append(line)
        # Sleep for the specified number of seconds
        time.sleep(interval)
        # Print wakeup message if verbose
        if verbose:
            line = TextOutput('Woke up')
            outputs.stdout.append(line)
        # Return execution result
        return ExecResult(
            is_success=True,
            outputs=outputs,
            provenance=ModuleProvenance(
                read=dict(),
                write=dict()
            )
        )
