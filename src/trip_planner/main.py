#!/usr/bin/env python
import sys
import warnings

from datetime import datetime, timedelta
from textwrap import dedent
from trip_planner.crew import TripPlanner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    print("=======================================")
    print("=      Welcome to the trip planner    =")
    print("=======================================")

    origin = input(dedent("""
                    Where are you located?
                    """))
    
    cities = input(dedent("""
                    What are the cities options you are interested in visiting?
                    """))

    interest = input(dedent("""
                    What are some or your high level interest and hobbies?
                    """))
    
    start_date = input(dedent("""
                    What is the starting date you are interested in?
                    """))
    
    days = input(dedent("""
                    How long is the trip in days?
                    """))
    
    start = datetime.strptime(start_date.strip(), "%Y-%m-%d")
    end = start + timedelta(days=int(days))
    date_range = f"{start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}"

    inputs = {
        'origin'  : origin,
        'cities'    : cities,
        'interest': interest,
        'dates'   : date_range
    }

    try:
        TripPlanner().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")