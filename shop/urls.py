from django.urls import path
from . import views
urlpatterns = [
       path('shophome', views.shophome, name='shophome'),
       path('<int:shop_id>', views.shopdetail, name='shopdetail'),
       path('<int:shop_id>/createshopreview', views.createshopreview, name='createshopreview'),
       path('review/<int:review_id>', views.updateshopreview, name='updateshopreview'),
       path('review/<int:review_id>/delete', views.deleteshopreview, name='deleteshopreview'),
]