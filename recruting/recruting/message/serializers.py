from rest_framework import serializers

from recruting.message.models import Chat


class ChatCreateSerializer(serializers.Serializer):
    from_mes = serializers.CharField(required=False)
    to_mes = serializers.CharField(required=True)
    mess = serializers.CharField(required=True)

    def create(self, validated_data):
        return Chat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'