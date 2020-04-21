from django.shortcuts import render
from rest_framework import serializers
from rest_framework import views


# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from qwerty.models import Order, Films


class Example3Serializer(serializers.Serializer):
    some_field = serializers.CharField()


class Example3(views.APIView):
    def post(self, request, *_, **__):
        serializer = Example3Serializer(request.data)
        serializer.is_valid(raise_exception=True)
        orders = Order.objects.raw("SELECT * FROM core_order WHERE " + serializer.validated_data.get("some_field"))
        for order in orders:
            if "something" in order.name:
                return Response("Found")
        return Response("Not found")


class Example4(views.APIView):
    def post(self, *_, **__):
        order = Order.objects.last()
        order.name = "example"
        order.save()


class Example4_2(views.APIView):
    def post(self, *_, **__):
        order = Order.objects.last()
        order.cost = "example"
        order.save()


class Example5(views.APIView):
    def get(self):
        orders = Order.objects.all()
        customer_names = []
        for order in orders:
            customer_names.append(order.customer.name)
        return Response(len(customer_names))


class Example6Serializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = "__all__"  # another common mistake


class Example6(ListAPIView):
    serializer_class = Example6Serializer
    queryset = Films.objects.all()


class Example7Serializer(serializers.Serializer):
    field1 = serializers.CharField(default="")
    field2 = serializers.CharField(default="")
    field3 = serializers.CharField(default="")
    field4 = serializers.CharField(default="")
    field5 = serializers.CharField(default="")


class Example7(views.APIView):  # FIXED IN NEXT DJANGO VERSION
    def patch(self, *_, **__):
        instance = {"field1": "example"}
        serialized_data = Example7Serializer(data=instance, partial=True)
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
        return Response(Example7Serializer(instance={}).data)
