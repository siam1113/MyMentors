from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path("", views.home , name="home"),
    path("blog", views.blog , name="blog"),
    path("post<int:pid>", views.post , name="post"),
    path("qna", views.qna , name="qna"),
    path("question<int:qid>", views.question , name="question"),
    path("mentors/", include("Mentors.urls")),
    path("ask", include("Ask.urls")),
    path("notifications", include("Notifications.urls")),
    path("dashboard/", include("Dashboard.urls")),
] 