from rest_framework import serializers


class TweetsSerializer(serializers.Serializer):
	content = serializers.CharField(style={'base_template': 'textarea.html'})
	image = serializers.FileField()