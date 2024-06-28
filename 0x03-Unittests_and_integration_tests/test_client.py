#!/usr/bin/env python3
"""Test client module"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class."""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json) -> None:
        """Tests the `org` method."""
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json) -> None:
        """Tests the `public_repos` method."""
        mock_get_json.return_value = TEST_PAYLOAD
        test_client = GithubOrgClient("google")
        self.assertEqual(test_client.public_repos(), ["google-repo1", "google-repo2"])
        self.assertEqual(test_client.public_repos("apache-2.0"), ["google-repo2"])

    @patch("client.get_json")
    def test_public_repos_with_license(self, mock_get_json) -> None:
        """Tests the `public_repos` method with a license."""
        mock_get_json.return_value = TEST_PAYLOAD
        test_client = GithubOrgClient("google")
        self.assertEqual(test_client.public_repos("apache-2.0"), ["google-repo2"])

    @patch("client.get_json")
    def test_public_repos_without_license(self, mock_get_json) -> None:
        """Tests the `public_repos` method without a license."""
        mock_get_json.return_value = TEST_PAYLOAD
        test_client = GithubOrgClient("google")
        self.assertEqual(test_client.public_repos(), ["google-repo1", "google-repo2"])

    @patch("client.get_json")
    def test_has_license(self, mock_get_json) -> None:
        """Tests the `has_license` method."""
        test_client = GithubOrgClient("google")
        self.assertTrue(test_client.has_license({"license": {"key": "apache-2.0"}}, "apache-2.0"))
        self.assertFalse(test_client.has_license({"license": {"key": "mit"}}, "apache-2.0"))
        self.assertFalse(test_client.has_license({"license": {"key": "mit"}}, None))

    @patch("client.get_json")
    def test_public_repos_with_license(self, mock_get_json) -> None:
        """Tests the `public_repos` method"""
        mock_get_json.return_value = TEST_PAYLOAD
        test_client = GithubOrgClient("google")
        self.assertEqual(test_client.public_repos("apache-2.0"), ["google-repo2"])
