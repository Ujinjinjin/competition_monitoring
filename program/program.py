#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform
import time
from datetime import datetime
from typing import Dict, Type

from .utils.utils import *
from .utils.logger import *
from .monitoring.observer import *
from . import settings

__all__ = ('Program',)


class Program:
    """Main program, that should be started"""

    def __init__(self, main_file: str):
        self.main_file: str = main_file
        self.utils: BaseUtils = self._get_utils()
        self._logger: Logger = Logger()
        self.observer: Observer = Observer()

    async def start(self):
        """Start program as admin"""
        if self.utils.is_admin() or not settings.admin_required:
            await self._start()
        else:
            self.utils.restart_as_admin()

    # noinspection PyBroadException
    async def _start(self):
        """Main logic"""
        print('Starting to clean processes...')
        await self._logger.log_async('Program started')
        while True:
            try:
                await self.observer.observe(settings.students)
                print(f'\n\n\nFetched data at: {datetime.now()}\n')
            except Exception as ex:
                print(f'Failed at:       {datetime.now()}', end='\r')
                await self._logger.log_async(str(ex), LogLevel.Error)
            finally:
                if datetime.utcnow() < settings.end_date:
                    await self._logger.log_async(f'Sleeping for {settings.sleep_time}...')
                    time.sleep(settings.sleep_time)
                else:
                    await self._logger.log_async('Finished observing')
                    print('Finished observing')
                    break

    def _get_utils(self) -> BaseUtils:
        """Get utils class depending on what system it's running"""
        cleaners_by_system: Dict[str, Type[BaseUtils]] = {
            'Linux': LinuxUtils,
            'Windows': WindowsUtils
        }
        platform_name: str = platform.system()
        if platform_name in cleaners_by_system.keys():
            return cleaners_by_system[platform_name](self.main_file)
        else:
            raise OSError(f'Your OS currently not supported. '
                          f'Program works on following systems: {", ".join(cleaners_by_system.keys())}')
