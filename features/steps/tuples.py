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


@given(u'a ← tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, x, y, z, w):
    context.a = Tuple(x, y, z, w)

@given(u'a1 ← tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, x, y, z, w):
    context.a1 = Tuple(x, y, z, w)

@given(u'a2 ← tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, x, y, z, w):
    context.a2 = Tuple(x, y, z, w)

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

@given(u'p1 ← point({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    context.p1 = Point(x, y, z)

@given(u'p2 ← point({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    context.p2 = Point(x, y, z)

@then(u'p = tuple({x:d}, {y:d}, {z:d}, {w:d})')
def step_impl(context, x, y, z, w):
    tuple = Tuple(x, y, z, w)
    assert context.p == tuple, f'{str(context.p) = } not equal with {str(tuple) = }'

@given(u'v ← vector({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    context.v = Vector(x, y, z)

@given(u'v1 ← vector({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    context.v1 = Vector(x, y, z)

@given(u'v2 ← vector({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    context.v2 = Vector(x, y, z)

@given(u'zero ← vector({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    context.zero = Vector(x, y, z)

@then(u'v = tuple({x:d}, {y:d}, {z:d}, {w:d})')
def step_impl(context, x, y, z, w):
    tuple = Tuple(x, y, z, w)
    assert context.v == tuple, f'{str(context.v) = } not equal with {str(tuple) = }'

@then(u'a1 + a2 = tuple({x:d}, {y:d}, {z:d}, {w:d})')
def step_impl(context, x, y, z, w):
    tuple = Tuple(x, y, z, w)
    sum = context.a1 + context.a2
    assert sum == tuple, f'{str(sum) = } not equal with {str(tuple) = }'

@then(u'p1 - p2 = vector({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    diff = context.p1 - context.p2
    vector = Vector(x, y, z)
    assert diff == vector, f'{str(diff) = } not equal with {str(vector) = }'

@then(u'p - v = point({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    diff = context.p - context.v
    point = Point(x, y, z)
    assert diff == point, f'{str(diff) = } not equal with {str(point) = }'

@then(u'v1 - v2 = vector({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    diff = context.v1 - context.v2
    vector = Vector(x, y, z)
    assert diff == vector, f'{str(diff) = } not equal with {str(vector) = }'

@then(u'zero - v = vector({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    diff = context.zero - context.v
    vector = Vector(x, y, z)
    assert diff == vector, f'{str(diff) = } not equal with {str(vector) = }'

@then(u'-a = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, x, y, z, w):
    tuple = Tuple(x, y, z, w)
    assert -context.a == tuple

@then(u'a * {multiplier:g} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, multiplier, x, y, z, w):
    tuple = Tuple(x, y, z, w)
    product = context.a * multiplier
    assert product == tuple, f'{str(product) = }, not equal with {str(tuple) = }'

@then(u'a / {divisor:g} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, divisor, x, y, z, w):
    tuple = Tuple(x, y, z, w)
    division = context.a / divisor
    assert division == tuple, f'{str() = }, not equal with {str(tuple) = }'
