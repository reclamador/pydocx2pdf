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
        self.PATH_TO_DOCX_FILE = os.path.join(self.cwd, "tests", "test.docx")
        self.PATH_TO_OUTPUT_FOLDER = os.path.join(self.cwd, "tests")
        self.PATH_TO_OUTPUT_PDF_FILE = os.path.join(self.cwd, "tests", "test.pdf")

    def tearDown(self):
        os.remove(self.PATH_TO_OUTPUT_PDF_FILE)
        pass

    def test_pdf_is_created(self):
        pydocx2pdf.convert_to(self.PATH_TO_OUTPUT_FOLDER, self.PATH_TO_DOCX_FILE)
        self.assertTrue(os.path.join(self.PATH_TO_OUTPUT_PDF_FILE))
