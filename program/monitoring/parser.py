#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

from requests import Response
from program import settings
from program.utils.logger import Logger
from ..models.student import *
import requests
import re

__all__ = ('Parser',)


class Parser:
    def __init__(self):
        self._regex = r"<tr id='\d+'>\n\s+<td class='num'>(\d+)<\/td>\n\s+<td class='fio'>([а-яА-Я\s-]+)<\/td>"
        self._logger = Logger()

    async def parse(self) -> List[Student]:
        await self._logger.log_async('Started parsing')
        rating_page: Response = requests.get(settings.rating_url)
        content: str = rating_page.content.decode(rating_page.encoding)
        result: list = re.findall(self._regex, content)
        student_list: List[Student] = [Student(item[1], int(item[0])) for item in result]
        await self._logger.log_async(f'Finished parsing. Parsed data: {student_list}')

        return student_list
