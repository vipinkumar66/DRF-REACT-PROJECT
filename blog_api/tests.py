from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from blog.models import Post, Category
from django.contrib.auth.models import User


class PostTest(APITestCase):

    def test_view_post(self):
        """
        Ensure that we are able to see all the data
        """
        url = reverse("blog_api:listcreate")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_post(self):
        """
        Here we will try to post the data
        => data
        => credentials
        """
        self.test_category = Category.objects.create(name = "Django Test")
        self.test_user1 = User.objects.create_superuser(username= "mahesh", password=
                            "maheshtest6")
        data= {
            "title":"try post",
            "excerpt":"trying with the test cases",
            "content":"trying with the test cases",
            "author":1
        }
        self.client.login(username=self.test_user1.username, password="maheshtest6")
        post_url = reverse("blog_api:listcreate")
        response = self.client.post(post_url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        individual_url = reverse("blog_api:detailcreate", kwargs={"pk":1})
        get_post_response = self.client.get(individual_url, format="json")
        self.assertEqual(get_post_response.status_code, status.HTTP_200_OK)

    def test_post_update(self):
        self.test_category = Category.objects.create(name="django")
        client = APIClient()
        self.testuser1 = User.objects.create_user(username="xyz", password="xyztest6")
        individual_url = reverse("blog_api:detailcreate", kwargs={"pk":1})
        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Post Excerpt', content = 'Post Content', author_id=1,
            slug='post-title', status='published'
        )

        data = {
            "id":1,
            "title":"post",
            "excerpt":"new",
            "content":"new",
            "author":1,
            "status":"published"
        }
        client.login(username = self.testuser1.username, password="xyztest6")
        response = client.put(individual_url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
