#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from typing import List

from program import settings
from program.utils.logger import Logger, LogLevel
from playsound import playsound
from .parser import *
from ..models.student import *

import json

__all__ = ('Observer',)


class Observer:
    def __init__(self):
        self._parser: Parser = Parser()
        self._logger: Logger = Logger()

    async def observe(self, student_names: List[str]):
        """Observe current monitoring"""

        await self._logger.log_async(f'Started observing following students: {student_names}')
        all_students, total_positions = await self._parser.parse()
        observable_students: List[Student] = list()

        os.system('cls')

        # Get observable students
        for student in all_students:
            if student.name in student_names:
                observable_students.append(student)

        # Get saved data
        with open(settings.data_file, 'r', encoding=settings.encoding) as file:
            saved_data: List[Student] = StudentSerializer.deserialize_many(json.load(file))
            await self._logger.log_async(f'Data loaded from file {settings.data_file}')

        print()
        for student in observable_students:
            print(f'{10*" "}{student.name}{(40 - len(student.name))*" "}{student.position}/{total_positions}')
        print()

        # Compare positions
        for student in observable_students:
            for saved_student in saved_data:
                if student.name == saved_student.name and student.position != saved_student.position:
                    await self.notify(student.name, saved_student.position, student.position, total_positions)

        # Save fresh data
        with open(settings.data_file, 'w', encoding=settings.encoding) as file:
            json.dump(StudentSerializer.serialize_many(observable_students), file, ensure_ascii=False, indent=2)
            await self._logger.log_async(f'Data saved to file {settings.data_file}')

    async def notify(self, student_name: str, old_position: int, new_position: int, total_positions: int):
        """Notify observer of changes"""

        if new_position > total_positions > old_position:
            playsound(settings.alert_lost)
            message: str = f'Attention! {student_name} has lost competition.'
        else:
            playsound(settings.alert_changed_position)
            message: str = f'{student_name}{(30-len(student_name))*" "} ' \
                f'has moved from position {old_position} to {new_position}. '
        await self._logger.log_async(message, LogLevel.Warning)
        print(message)
