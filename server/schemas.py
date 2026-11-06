from marshmallow import Schema, fields, validate, validates, ValidationError

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(validate=validate.Range(min=0, error="Reps cannot be negative."))
    sets = fields.Int(validate=validate.Range(min=0, error="Sets cannot be negative."))
    duration_seconds = fields.Int(validate=validate.Range(min=0, error="Duration in seconds cannot be negative."))
    

    exercise = fields.Nested('ExerciseSchema', only=('id', 'name', 'category', 'equipment_needed'), dump_only=True)


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True, error_messages={"required": "Date is required."})
    duration_minutes = fields.Int(required=True, validate=validate.Range(min=1, error="Duration must be at least 1 minute."))
    notes = fields.Str()
    

    workout_exercises = fields.List(fields.Nested(WorkoutExerciseSchema), dump_only=True)


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, error="Exercise name cannot be empty."))
    category = fields.Str(required=True)
    equipment_needed = fields.Bool(required=True)
    

    workout_exercises = fields.List(fields.Nested(WorkoutExerciseSchema, exclude=('exercise',)), dump_only=True)

    @validates('category')
    def validate_category(self, value):
        valid_categories = ['Cardio', 'Strength', 'Flexibility', 'Balance', 'HIIT']
        if value not in valid_categories:
            raise ValidationError(f"Category must be one of: {', '.join(valid_categories)}")