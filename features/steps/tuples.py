# from unittest import *
import unittest

from behave import *
from raytracer.tuple import *

EPSILON = 0.0000001
def equal(a, b):
    if abs(a - b) < EPSILON:
        return True
    else:
        return False


@given(u'a ← tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, x, y, z, w):
    context.a = Tuple(x, y, z, w)

@then(u'a.x = {x:f}')
def step_impl(context, x):
    assert equal(context.a.x, x) is True, f"Expected x {context.a.x}, {x = }"

@then(u'a.y = {y:f}')
def step_impl(context, y):
    assert equal(context.a.y, y) is True, f"Expected y {context.a.y}, but {y = }"

@then(u'a.z = {z:f}')
def step_impl(context, z):
    assert equal(context.a.z, z) is True, f"Expected z {context.a.z}, but {z = }"

@then(u'a.w = {w:f}')
def step_impl(context, w):
    assert equal(context.a.w, w) is True, f"Expected w {context.a.w}, but {w = }"

@then(u'a is a point')
def step_impl(context):
    assert context.a.is_point() is True, f'{str(context.a) = } is not a point'

@then(u'a is not a point')
def step_impl(context):
    assert context.a.is_point() is False, f'{str(context.a) = } is a point'

@then(u'a is a vector')
def step_impl(context):
    assert context.a.is_vector() is True, f'{str(context.a) = } is not a vector'

@then(u'a is not a vector')
def step_impl(context):
    assert context.a.is_vector() is False, f'{str(context.a) = } is a vector'

@given(u'p ← point({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    context.p = Point(x, y, z)

@then(u'p = tuple({x:d}, {y:d}, {z:d}, {w:d})')
def step_impl(context, x, y, z, w):
    tuple = Tuple(x, y, z, w)
    assert context.p == tuple, f'{str(context.p) = } not equal with {str(tuple) =}'
