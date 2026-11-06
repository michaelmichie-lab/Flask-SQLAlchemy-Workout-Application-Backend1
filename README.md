# Personal Trainer Workout Tracker API

A RESTful backend API built with Flask, SQLAlchemy, and Marshmallow that allows personal trainers to design workouts, build a reusable library of exercises, and attach exercises with specific performance metrics (reps, sets, duration) to workouts.

## Validations Summary
- **Table Constraints**:
  1. `CheckConstraint("duration_minutes > 0")` on `workouts` table.
  2. `CheckConstraint("length(name) > 0")` on `exercises` table.
  3. `CheckConstraint("reps >= 0")`, `sets >= 0`, `duration_seconds >= 0` on `workout_exercises` table.
- **Model Validations**:
  1. Validates non-empty names and pre-approved categories (`Cardio`, `Strength`, etc.) in `Exercise`.
  2. Validates positive `duration_minutes` in `Workout`.
- **Schema Validations**:
  1. Marshmallow range checks for non-negative numerical fields in `WorkoutExerciseSchema`.
  2. Custom category validation and non-empty string constraints in `ExerciseSchema`.

## Installation Instructions

1. Install dependencies using Pipenv:
   ```bash
   pipenv install
   pipenv shell# Flask-SQLAlchemy-Workout-Application-Backend1
