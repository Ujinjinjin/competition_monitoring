#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum
from aiofile import AIOFile
from datetime import datetime

from program import settings

__all__ = ('Logger', 'LogLevel')


class LogLevel(Enum):
    Debug = 0,
    Information = 1,
    Error = 2,
    Warning = 3


class Logger:
    def __init__(self, log_file: str = settings.log_file):
        self._log_file = log_file

    async def log_async(self, message: str, log_level: LogLevel = LogLevel.Debug):
        async with AIOFile(self._log_file, 'a', encoding=settings.encoding) as afp:
            await afp.write(f'{datetime.utcnow()} | {log_level.name}: {message}\n')
