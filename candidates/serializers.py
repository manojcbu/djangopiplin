from rest_framework import serializers
from candidates.models import Candidate, Skill


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'


class CandidateSerializerReadOnly(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Candidate
        fields = (
            "full_name",
            "aadhaar_id",
            "dob",
            "state",
            "pin_code",
            "gender",
            "email",
            "primary_phone",
            "other_phone",
            "address",
            "longitude",
            "latitude",
            "experience",
            "skills"
        )


class CandidateSerializer(serializers.ModelSerializer):
    print("############")
    skills = serializers.ListField(write_only=True)
    _skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Candidate
        fields = (
            "full_name",
            "aadhaar_id",
            "dob",
            "state",
            "pin_code",
            "gender",
            "email",
            "primary_phone",
            "other_phone",
            "address",
            "longitude",
            "latitude",
            "experience",
            "skills",
            "_skills"
        )

    def create(self, validated_data):
        """
        Creating a candidate data and mapping Skills to ids.
        This will be overriding default create method.

        :param validated_data:
        :return: Object for Candidate Instance
        """
        skills = validated_data.pop('skills')

        # Candidate Info
        candidate = Candidate(**validated_data)
        candidate.save()

        # Map Skills
        for i in skills:
            skill_obj, _ = Skill.objects.get_or_create(skill=i)
            print(skill_obj, _)
            candidate.skills.add(skill_obj)
            candidate.save()

        return candidate
