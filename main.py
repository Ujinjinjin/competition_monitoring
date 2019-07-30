#!/usr/bin/env python
# -*- coding: utf-8 -*-
from asyncio import Task, AbstractEventLoop

try:
    if __name__ == '__main__':
        from program.program import Program
        import asyncio

        program: Program = Program(__file__)

        loop: AbstractEventLoop = asyncio.get_event_loop()
        task: Task = loop.create_task(program.start())
        loop.run_until_complete(task)
        loop.close()

except Exception as ex:
    print(ex)
    input('Press enter to continue')
