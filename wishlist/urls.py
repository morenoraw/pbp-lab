from django.urls import path
from wishlist.views import new_wishlist, show_wishlist, show_ajax, generate_xml, generate_xml_by_id, generate_json, generate_json_by_id, register, login_user, logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path("ajax", show_ajax, name="show_ajax"),
    path("ajax/submit", new_wishlist, name="new_wishlist"),
    path('xml/', generate_xml, name='generate_xml'),
    path('xml/<int:id>', generate_xml_by_id, name='generate_xml_by_id'),
    path('json/', generate_json, name='generate_json'),
    path('json/<int:id>', generate_json_by_id, name='generate_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]