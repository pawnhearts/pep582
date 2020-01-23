#a!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `pep582` package."""


import unittest
import tempfile
import os


class TestPep582(unittest.TestCase):
    """Tests for `pep582` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        os.chdir(tempfile.mkdtemp())
        os.mkdir('__pypackages__')

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_pip_install(self):
        """Test pip install."""
        os.system('pip install pytest')
        self.assertEqual(os.system('test -e __pypackages__/*/lib/pytest/'), 0)  # assuming we are on unix, sorry


    def test_import_module(self):
        """Test import module."""
        import pytest
        self.assertTrue(pytest.__file__.startswith('__pypackages__'))


