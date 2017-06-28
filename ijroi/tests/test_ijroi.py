import os

import numpy as np
import py
import pytest

import ijroi

def get_fixture(name):
    dirpath = py.path.local(__file__).dirpath()
    return dirpath.join("fixtures", name)

def test_ijroi_import():
    assert ijroi.__version__

def test_rectangle():
    fixture = get_fixture("subpixel_rectangle.roi")
    with fixture.open("rb") as f:
        rect = ijroi.read_roi(f)
    assert (rect == np.array([[5, 4], [5, 8], [10, 8], [10, 4]])).all()
    assert rect.dtype == np.float32

    fixture = get_fixture("integer_rectangle.roi")
    with fixture.open("rb") as f:
        rect = ijroi.read_roi(f)
    assert (rect == np.array([[5, 4], [5, 8], [10, 8], [10, 4]])).all()
    assert rect.dtype == np.int16

def test_freehand_circle():
    fixture = get_fixture("freehand_circle.roi")
    with fixture.open("rb") as f:
        circle_roi = ijroi.read_roi(f)
        circle = circle_roi.points
        position = circle_roi.position
    assert len(circle) == 100
    assert abs(circle[:, 1].mean()-10) < 0.01
    assert abs(circle[:, 0].mean()-15) < 0.01
    assert position == 0

def test_integer_freehand():
    fixture = get_fixture("freehand_integer.roi")
    with fixture.open("rb") as f:
        freehand_roi = ijroi.read_roi(f)
        freehand = freehand_roi.points
        position = freehand_roi.position
    assert len(freehand) == 3
    assert all(freehand[2, :] == [1, 10])
    assert freehand.dtype == np.int16
    assert position == 0

def test_polygon():
    fixture = get_fixture("polygon_circle.roi")
    with fixture.open("rb") as f:
        circle_roi = ijroi.read_roi(f)
        circle = circle_roi.points
        position = circle_roi.position
    assert len(circle) == 100
    assert abs(circle[:, 1].mean()-10) < 0.01
    assert abs(circle[:, 0].mean()-15) < 0.01
    assert position == 0

    fixture = get_fixture("polygon_integer.roi")
    with fixture.open("rb") as f:
        polyint_roi = ijroi.read_roi(f)
        polyint = polyint_roi.points
        position = polyint_roi.position
    assert len(polyint) == 3
    assert all(polyint[2, :] == [1, 10])
    assert polyint.dtype == np.int16
    assert position == 0

def test_point():
    fixture = get_fixture("int_point.roi")
    with fixture.open("rb") as f:
        point_roi = ijroi.read_roi(f)
        point = point_roi.points
        position = point_roi.position
    assert point.ndim == 2
    assert point[0,0] == 256
    assert point[0,1] == 128
    assert position == 0

def test_float_point():
    fixture = get_fixture("float_point.roi")
    with fixture.open("rb") as f:
        point_roi = ijroi.read_roi(f)
        point = point_roi.points
        position = point_roi.position
    assert point.ndim == 2
    assert abs(point[0,0] - 567.8) < 0.01
    assert abs(point[0,1] - 123.4) < 0.01
    assert position == 0