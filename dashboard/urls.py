from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import get_chart_data, get_table_data, get_pie_graph_data, get_table2_data, get_table3_data,get_chart3
app_name = "dashboard"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    # path('data', views.get_data, name="data"),
    path('chart/data', get_chart_data, name="chart_data"),
    path('dashboardTable/data', get_table_data, name="table_data"),
    path('pieChart/data', get_pie_graph_data, name="pie_graph"),
    path('dashboardTable2/data', get_table2_data, name="table2_data"),
    path('dashboardTable3/data', get_table3_data, name="table3_data"),
    path('chart3/data', get_chart3, name="chart3_data"),
]

