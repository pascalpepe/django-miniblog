# Copyright 2017-2023 Pascal Pepe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for MiniBlog views."""

from django.test import TestCase
from django.urls import reverse

from miniblog.models import Post


class PostDetailViewTest(TestCase):
    """Tests for the post detail view."""

    @classmethod
    def setUpTestData(cls):
        """Create objects for all tests."""
        cls.post = Post.objects.create(title="Foo", content="bar")

    def test_route_from_name(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_route_from_path(self):
        response = self.client.get("/blog/1/")
        self.assertEqual(response.status_code, 200)

    def test_templates_used(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "miniblog/post_detail.html")


class PostListViewTest(TestCase):
    """Tests for the post list view."""

    def test_route_from_name(self):
        response = self.client.get(reverse("miniblog:post-list"))
        self.assertEqual(response.status_code, 200)

    def test_route_from_path(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_templates_used(self):
        response = self.client.get(reverse("miniblog:post-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "miniblog/post_list.html")
