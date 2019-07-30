#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

__all__ = ('Student', 'StudentSerializer')


class Student:
    def __init__(self, name: str, position: int):
        self.name: str = name
        self.position: int = position

    def __repr__(self):
        return f'\'{self.name}\''


class StudentSerializer:
    @staticmethod
    def deserialize(data: dict) -> Student:
        return Student(data['name'], data['position'])

    @staticmethod
    def serialize(data: Student) -> dict:
        return {
            'name': data.name,
            'position': data.position
        }

    @staticmethod
    def serialize_many(data: List[Student]) -> List[dict]:
        serialized_data: List[dict] = list()
        for item in data:
            serialized_data.append(StudentSerializer.serialize(item))

        return serialized_data

    @staticmethod
    def deserialize_many(data: List[dict]) -> List[Student]:
        deserialized_data: List[Student] = list()
        for item in data:
            deserialized_data.append(StudentSerializer.deserialize(item))
        return deserialized_data
