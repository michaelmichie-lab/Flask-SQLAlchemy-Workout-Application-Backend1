#!/usr/bin/env python3

from app import app
from config import db
from models import Workout, Exercise, WorkoutExercise
from datetime import date

with app.app_context():
    print("Clearing old database records...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Seeding exercises...")
    ex1 = Exercise(name="Push Ups", category="Strength", equipment_needed=False)
    ex2 = Exercise(name="Treadmill Run", category="Cardio", equipment_needed=True)
    ex3 = Exercise(name="Plank", category="Strength", equipment_needed=False)
    
    db.session.add_all([ex1, ex2, ex3])
    db.session.commit()

    print("Seeding workouts...")
    w1 = Workout(date=date(2026, 3, 1), duration_minutes=45, notes="Morning full body routine")
    
    db.session.add_all([w1])
    db.session.commit()

    print("Seeding workout exercises...")
    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=ex1.id, reps=15, sets=3, duration_seconds=0)
    db.session.add(we1)
    db.session.commit()

    print("Database successfully seeded!")
