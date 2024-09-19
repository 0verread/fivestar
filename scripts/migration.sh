#!/bin/bash

# use alembic for database migration

commitMsg=""

# init alembic if not there



# Generating migration
alembic revision --autogenerate -m "Initial migration"

# apply migration
alembic upgrade head
