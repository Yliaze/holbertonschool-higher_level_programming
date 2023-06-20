#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""main with tests for 7-base_geometry"""
bg = BaseGeometry()

bg.area()
bg.integer_validator()
bg.integer_validator("age")
bg.integer_validator("age", 1)
bg.integer_validator("age", 0)
bg.integer_validator("age", -4)
bg.integer_validator("age", "4")
bg.integer_validator("age", (4,))
bg.integer_validator("age", [3])
bg.integer_validator("age", True)
bg.integer_validator("age", {3, 4})
bg.integer_validator("age", None)
