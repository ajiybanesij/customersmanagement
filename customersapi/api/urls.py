from django.urls import path
from customersapi.api import views as api_views

urlpatterns = [
    path('customers/', api_views.CustomersCrateAPIViews.as_view(), name='customers-list'),
    path('customers/<int:pk>', api_views.CustomersDetailAPIViews.as_view(), name='customers-detail'),
    path('customers/list/', api_views.CustomersListView.as_view(), name='customers-list-view'),
]
