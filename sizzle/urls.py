from django.urls import path
from . import views_server, views_kitchen, views_manager

urlpatterns = [
    # Server URLs
    path("server/order/new/", views_server.create_order, name="server_new_order"),
    path("server/order/<int:order_id>/items/", views_server.add_items, name="server_add_items"),

    # Kitchen URLs
    path("kitchen/", views_kitchen.kitchen_dashboard, name="kitchen_dashboard"),
    path("kitchen/order/<int:order_id>/complete/", views_kitchen.complete_order, name="kitchen_complete_order"),

    # Manager URLs
    path("manager/menu/", views_manager.manage_menu, name="manager_menu"),
    path("manager/menu/add/", views_manager.add_menu_item, name="manager_add_menu_item"),
    path("manager/menu/<int:item_id>/edit/", views_manager.edit_menu_item, name="manager_edit_menu_item"),
]
