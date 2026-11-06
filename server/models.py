from config import db
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
from datetime import date

class Exercise(db.Model):
    __tablename__ = 'exercises'

    __table_args__ = (
        CheckConstraint("length(name) > 0", name="check_exercise_name_not_empty"),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(50), nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False, nullable=False)

    workout_exercises = db.relationship('WorkoutExercise', backref='exercise', cascade='all, delete-orphan')

    @validates('name')
    def validate_name(self, key, name):
        if not name or not name.strip():
            raise ValueError("Exercise name cannot be empty.")
        return name.strip()

    @validates('category')
    def validate_category(self, key, category):
        valid_categories = ['Cardio', 'Strength', 'Flexibility', 'Balance', 'HIIT']
        if category not in valid_categories:
            raise ValueError(f"Category must be one of: {', '.join(valid_categories)}")
        return category


class Workout(db.Model):
    __tablename__ = 'workouts'

    __table_args__ = (
        CheckConstraint("duration_minutes > 0", name="check_workout_duration_positive"),
    )

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=True)

    workout_exercises = db.relationship('WorkoutExercise', backref='workout', cascade='all, delete-orphan')

    @validates('duration_minutes')
    def validate_duration(self, key, duration_minutes):
        if duration_minutes is None or duration_minutes <= 0:
            raise ValueError("Duration must be a positive integer.")
        return duration_minutes


class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'

    __table_args__ = (
        CheckConstraint("reps >= 0", name="check_reps_non_negative"),
        CheckConstraint("sets >= 0", name="check_sets_non_negative"),
        CheckConstraint("duration_seconds >= 0", name="check_duration_seconds_non_negative"),
    )

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    reps = db.Column(db.Integer, nullable=True, default=0)
    sets = db.Column(db.Integer, nullable=True, default=0)
    duration_seconds = db.Column(db.Integer, nullable=True, default=0)

    @validates('reps', 'sets', 'duration_seconds')
    def validate_metrics(self, key, value):
        if value is not None and value < 0:
            raise ValueError(f"{key} cannot be negative.")
        return value