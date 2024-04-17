from django.urls import path
from rest_framework.routers import DefaultRouter

from .v1.product.views import (
    ProductModelViewSet,
    CategoryModelViewSet
)

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

        # # login
        # path("login/", UserAuthenticationView.as_view({"post": "login"}), name="login"),
        # path("logout/", UserAuthenticationView.as_view({"post": "logout"}), name="logout"),

        # Products
        path("products/", ProductModelViewSet.as_view({"get": "products_list"}), name="products-list"),
        path("products-detail/<slug>/", ProductModelViewSet.as_view({"get": "product_detail"}), name="products-detail"),

        # path("apartments/create/", EstablishmentModelViewSet.as_view({"post": "create"}), name="apartments-create"),
        # path("apartments/update/<int:pk>/", EstablishmentModelViewSet.as_view({"put": "update"}),
        #      name="apartments-update"),
        # path("apartments/delete/<int:pk>/", EstablishmentModelViewSet.as_view({"delete": "delete"}),
        #      name="apartments-delete"),

        # Category
        path("category-list/<slug>/", CategoryModelViewSet.as_view({"get": "category_list"}), name="category-list"),

    ]
)