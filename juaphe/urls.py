from django.urls import include, path
from kye import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('aduser/<int:pk>', views.ADeleteUser.as_view(), name='aduser'),
    path('alvuser/<int:pk>', views.ALViewUser.as_view(), name='alvuser'),
    path('aeuser/<int:pk>', views.AEditUser.as_view(), name='aeuser'),
    path('create_user/', views.create_user, name='create_user'),
    path('create_user_form/', views.create_user_form, name='create_user_form'),
    path('aluser/', views.ListUserView.as_view(), name='aluser'),
    path('olchat/', views.UListChat.as_view(), name='olchat'),
    path('alchat/', views.AListChat.as_view(), name='alchat'),
    path('oachat/', views.UCreateChat.as_view(), name='oachat'),
    path('achat/', views.ACreateChat.as_view(), name='achat'),
    path('officer/', views.officer, name='officer'),
    path('add_case/', views.add_case, name='add_case'),
    path('case_form/', views.case_form, name='case_form'),
    path('home/', views.home, name='home'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),
    path('osearch/', views.osearch, name='osearch'),
    path('publish_case/', views.publish_case, name='publish_case'),
    path('publish/', views.publish, name='publish'),
    path('pending/case/<int:pk>', views.Deadline.day, name='update_status'),
    path('case_list/', views.TaskListView.as_view(), name='task_list'),
    path('list_case/', views.CaseListView.as_view(), name='list_case'),
    path('pending/', views.Pending.as_view(), name='pending'),
    path('pencase/', views.PenCase.as_view(), name='pencase'),
    path('deadline/', views.DeadlineTask.as_view(), name='deadline'),
    path('deadcase/', views.DeadCaseTask.as_view(), name='deadcase'),
    path('completed/', views.Completed.as_view(), name='completed'),
    path('compcase/', views.CompCase.as_view(), name='compcase'),
    path('manage-tasks/', views.ManageTask.as_view(), name='manage-tasks'),
    path('users/', views.UserView.as_view(), name='users'),
    path('comp/', views.comp, name='comp'),
    path('tasks/upload/', views.UploadTask.as_view(), name='upload_task'),
    path('tasks/', views.book_list, name='book_list'),
    path('view/<int:pk>', views.TaskView.as_view(template_name='dashboard/admin/task_detail.html'), name='view_task'),
    path('delete_task/<int:pk>', views.DeleteTask.as_view(template_name='dashboard/admin/confirm_delete.html'), name='delete_task'),
    path('edit_task/<int:pk>', views.UpdateTask.as_view(), name='update_task'),



    # User URLs
    path('addcase_form/', views.addcase_form, name='addcase_form'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('u-taslist/', views.UTaskListView.as_view(), name='u_tasklist'),









    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
