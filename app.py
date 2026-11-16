# CIS 211 Lab 4 starter
# Build a fictional campus club or service information page.
# Read CIS_211_Lab4_Guide.pdf before editing this file.
# This starter runs, but its TODO sections are not a completed submission.

import streamlit as st

# TODO 1: Replace these values with your own fictional club or service details.
# Keep at least three key-value pairs. You may add more.
club_info = {
    "name": "Andre's Basketball Club",
    "day": "Monday, Wednesday, Friday",
    "time": "3:00 PM Monday and Wednesday, 2:00 PM Friday",",
}

# TODO 2: Replace these sample strings with at least three relevant activities.
# During the list change check, add one new item and keep it in the final app.
activities = [
    "Stretching",
    "Suicide Run",
    "Shooting training",
    "Dribbling Drills",
]

st.title(club_info["name"])
st.caption("Welcome to Andre's Basketball club. Come train and get some buckets")

# Remove this starter message when your page is complete.
st.write("Welcome to Andre's Basketball club. Come train and get some buckets.")

st.header("Come every Monday, Wednesday, and Friday to learn how to improve your basketball skills like shooting, dribbling, and passing")
# TODO 3: Use st.markdown() to write your own two- or three-sentence introduction.
# Include both **bold** and *italic* text inside your Python string.
# The handout explains triple quotes if your Markdown spans several lines.

st.header("Activities")
for activity in activities:
    st.write(activity)
# TODO 4: Write a for loop that displays every value from activities.
# Use Streamlit output inside the loop. Do not type each activity again.

st.header("Basketball Schedule")
st.write("Day:", club_info["day"])
st.write("Time:", club_info["time"])
# TODO 5: Display at least two dictionary values by looking them up by key.
# Give the displayed values meaningful labels such as Day and Time.

st.header("Prepare for a visit")

st.markdown("Bring your basketball shoes."
            "Bring a water bottle." 
            "Wear comfortable athletic clothing." 
            "Come on time." 
            "Bring your confidence")

st.markdown("[https://github.com/AndreCM13/CIS211-LAb-4/edit/main/app.py)")
# Add one meaningful, working external Markdown link. 
# TODO 7: Add at least three comments explaining your OWN completed code.
Comment 1(My code is explaining to those who would want to join my basketball club)
Comment 2( Another part of my code is to explain the actvites being done in the club)
Comment 3( Another is telling the days and time of when the club is starts and how to prepare)
# TODO 8: Perform both change checks and complete the private submission template.
# Upload your final source files, links, reflection, and app screenshots to Brightspace.
