import numpy as np


def readB():
    List = input(
        "Enter a list separeted by comma as B (it must have same number of rows as A)"
    )
    B = [int(i) for i in List.split(",")]
    return B
