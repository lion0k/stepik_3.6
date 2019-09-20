# -*- coding: utf-8 -*-

import time

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_exists_button(browser):
    browser.get(LINK)
    # time.sleep(30)
    assert browser.find_element_by_css_selector('.btn-add-to-basket')
