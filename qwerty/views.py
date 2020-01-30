from django.shortcuts import render
from rest_framework import serializers
from rest_framework import views


# Create your views here.
from rest_framework.response import Response

from qwerty.models import Order


class Example4Serializer(serializers.Serializer):
    field1 = serializers.CharField(default="")
    field2 = serializers.CharField(default="")
    field3 = serializers.CharField(default="")
    field4 = serializers.CharField(default="")
    field5 = serializers.CharField(default="")


class Example4(views.APIView):  # FIXED IN NEXT DJANGO VERSION
    def patch(self, *args, **kwargs):
        instance = {"field1": "example"}
        serialized_data = Example4Serializer(data=instance, partial=True)
        if serialized_data.is_valid():
            _declared_fields = serialized_data._declared_fields.keys()
            _declared_fields = [x for x in _declared_fields]
            for key in _declared_fields:
                if key not in serialized_data.validated_data.keys():
                    serialized_data._declared_fields.pop(key)

            _ = serialized_data._fields
            _ = serialized_data._readable_fields

            del serialized_data._fields
            del serialized_data._readable_fields
        return Response(serialized_data.data)

    def get(self, *args, **kwargs):
        return Response(Example4Serializer(instance={}).data)


class Example5(views.APIView):
    def post(self, *args, **kwargs):
        order = Order.objects.last()
        order.name = "example"
        order.save()


class Example5_2(views.APIView):
    def post(self, *args, **kwargs):
        order = Order.objects.last()
        order.cost = "example"
        order.save()


class Example6(views.APIView):
    def get(self):
        orders = Order.objects.all()
        customer_names = []
        for order in orders:
            customer_names.append(order.customer.name)
        return Response(len(customer_names))
