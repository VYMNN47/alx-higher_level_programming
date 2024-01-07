#!/usr/bin/python3
"""
Multiply 2 matricies using numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrix that is given
    Args:
        m_a: first input
        m_b: second input
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
