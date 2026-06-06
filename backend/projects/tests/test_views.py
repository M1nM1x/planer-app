from django.urls import reverse

from .test_setup import BaseAPITestCase

from ..models import Project

class CreateProjectTestCase(BaseAPITestCase):

    def test_create_project_correctly(self):
        user, refresh = self.authenticate()

        res = self.client.post(self.create_url, self.project_data, format='json')
        self.assertEqual(res.status_code, 201)

    def test_project_does_not_creating_with_short_name(self):
        user, refresh = self.authenticate()

        res = self.client.post(self.create_url, self.project_invalid_name, format='json')
        self.assertEqual(res.status_code, 400)

    def test_project_create_attempt_without_authorization(self):
        res = self.client.post(self.create_url, self.project_invalid_name, format='json')
        self.assertEqual(res.status_code, 401)

    def test_project_detail(self):
        user, refresh = self.authenticate()
        project = Project.objects.create(
            name=self.project_data['name'],
            description=self.project_data['description'],
            owner=user
        )
        detail_url = reverse('project_detail', kwargs={'pk': project.pk})

        res = self.client.get(detail_url)
        self.assertEqual(res.status_code, 200)

    def test_project_list(self):
        res = self.client.get(self.create_url)
        self.assertEqual(res.status_code, 200)