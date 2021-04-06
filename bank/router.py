from testdb.viewsets import CardViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('card',CardViewset)