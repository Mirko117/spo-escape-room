#!/bin/bash

echo "Starting Gunicorn server..."
exec gunicorn -w 3 -b 0.0.0.0:5000 manage:app