from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from organization.models import Organization
from . import serializer


class OrganizationAPI(ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = serializer.OrganizationSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'status': True,
                         'message': 'Organization added!',
                         'data': serializer.data},
                        status=status.HTTP_201_CREATED, headers=headers)


class OrganizationRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.OrganizationSerializer

    def get_queryset(self):
        return Organization.objects.filter(id=self.kwargs.get('pk', None))
