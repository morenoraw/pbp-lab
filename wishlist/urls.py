from django.urls import path
from wishlist.views import show_wishlist, generate_xml, generate_xml_by_id, generate_json, generate_json_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', generate_xml, name='generate_xml'),
    path('xml/<int:id>', generate_xml_by_id, name='generate_xml_by_id'),
    path('json/', generate_json, name='generate_json'),
    path('json/<int:id>', generate_json_by_id, name='generate_json_by_id'),
]