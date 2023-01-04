from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
   # path('soon',views.soon,name='soon'),
    path('dash',views.dash,name='dash'),
    path('dash/ftab',views.ftab,name='ftab'),
    path('dash/ktab',views.ktab,name='ktab'),
    path('dash/swtab',views.swtab,name='swtab'),
    path('dash/mustab',views.mustab,name='mustab'),
    path('dash/artab',views.artab,name='artab'),
    path('dash/fitab',views.fitab,name='fitab'),
    path('dash/sc',views.sc,name='sc'),
    path('dash/pc',views.pc,name='pc'),
    path('dash/attendance',views.attendance,name='attendance'),
    path('dash/attendance/fa',views.fa,name='fa'),
    path('dash/attendance/ka',views.ka,name='ka'),
    path('dash/attendance/fitnessa',views.fitnessa,name='fitnessa'),
    path('dash/attendance/aa',views.aa,name='aa'),
    path('dash/attendance/ma',views.ma,name='ma'),
    path('dash/attendance/sa',views.sa,name='sa'),
    path('dash/renew',views.renew,name='sa')
]