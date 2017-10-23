# -*- coding: utf-8 -*-
import pytest

from fixture.Application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_fixber(app):
    app.login(username="ultras", password="KzkMK")
    app.edit_product_field(Group(product_kind="TeamCity Redmine Microsoft Visual Studio Python Python"))
    app.logout()


def test_fixber_another_data(app):
    app.login(username="ultras", password="KzkMK")
    app.edit_product_field(Group("rambler"))
    app.logout()