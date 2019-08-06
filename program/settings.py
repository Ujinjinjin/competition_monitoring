#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List

__all__ = ('admin_required', 'rating_url', 'log_file', 'students', 'data_file', 'encoding', 'alert_changed_position',
           'alert_lost', 'end_date', 'sleep_time')

encoding = 'utf-8'

rating_url: str = 'https://priem.mirea.ru/rating-2019/names_rating.php?competition=1620822713013640502&prior=any' \
                  '&documentType=any&accepted=1&onlyActive=1&onlyPaid=0 '

admin_required: bool = False

log_file: str = 'storage/log'
data_file: str = 'storage/data.json'
alert_lost: str = 'storage/alert_lost.wav'
alert_changed_position: str = 'storage/alert_changed_position.wav'
alert_moved_up: str = 'storage/moved_up.wav'

students: List[str] = [
    'Галладжов Камиль Амруллаевич',
    'Галладжов Шахмир Амруллаевич',
    'Итуа Жуэль-Габэн',
    'Саркисян Грачья Аветикович',
    'Тертищенко Виктория Юрьевна'
]

sleep_time: int = 600
end_date: datetime = datetime(2019, 8, 8, 23, 59, 59)
