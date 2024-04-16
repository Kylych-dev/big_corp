from django.urls import path
from rest_framework.routers import DefaultRouter

# from api.v1.appartments.views import EstablishmentModelViewSet
#
# from api.auth.views import (
#     RegisterView,
#     UserAuthenticationView
# )

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend(
    [

        # # registration
        # path("register/", RegisterView.as_view({"post": "register"}), name="register"),
        #
        # # login
        # path("login/", UserAuthenticationView.as_view({"post": "login"}), name="login"),
        # path("logout/", UserAuthenticationView.as_view({"post": "logout"}), name="logout"),
        #
        # # Establishment
        # path("apartments/", EstablishmentModelViewSet.as_view({"get": "list"}), name="apartments-list"),
        # path("apartments/create/", EstablishmentModelViewSet.as_view({"post": "create"}), name="apartments-create"),
        # path("apartments/update/<int:pk>/", EstablishmentModelViewSet.as_view({"put": "update"}),
        #      name="apartments-update"),
        # path("apartments/delete/<int:pk>/", EstablishmentModelViewSet.as_view({"delete": "delete"}),
        #      name="apartments-delete"),
    ]
)