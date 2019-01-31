from todoapi.views import TaskViewSet, DonetaskViewSet, AlltasksViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todolist', TaskViewSet)
router.register('done', DonetaskViewSet)
router.register('all', AlltasksViewSet)
