#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from typing import List

import requests
from requests import Response

from program import settings
from program.utils.logger import Logger
from ..models.student import *

__all__ = ('Parser',)


class Parser:
    def __init__(self):
        self._student_regex = r"<tr id='\d+'>\n\s+<td class='num'>(\d+)<\/td>\n\s+<td class='fio'>([а-яА-Я\s-]+)<\/td>"
        self._total_positions_regex = r"<p>Всего мест — (\d+)"
        self._logger = Logger()

    async def parse(self) -> (List[Student], int):
        await self._logger.log_async('Started parsing')
        rating_page: Response = requests.get(settings.rating_url)
        content: str = rating_page.content.decode(rating_page.encoding)
        result: list = re.findall(self._student_regex, content)
        total_positions: int = int(re.findall(self._total_positions_regex, content)[0])
        student_list: List[Student] = [Student(item[1], int(item[0])) for item in result]
        await self._logger.log_async(f'Finished parsing. Parsed data: {student_list}')

        return student_list, total_positions
