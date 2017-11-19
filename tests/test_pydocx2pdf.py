#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pydocx2pdf` package."""


import unittest
import os
from pydocx2pdf import pydocx2pdf


class TestPydocx2pdf(unittest.TestCase):
    """Tests for `pydocx2pdf` package."""

    def setUp(self):
        self.cwd = os.getcwd()

    def tearDown(self):
        os.remove(os.path.join(self.cwd, "tests", "test.pdf"))

    def test_pdf_is_created(self):
        pydocx2pdf.convert_to(os.path.join(self.cwd, "tests"), os.path.join(self.cwd, "tests", "test.pdf"))
        self.assertTrue(os.path.exists("./test.pdf"))
