class MLBSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLBData
        fields = '__all__'

class MiLBSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiLBData
        fields = '__all__'