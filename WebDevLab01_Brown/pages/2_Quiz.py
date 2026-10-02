import streamlit as st

# Title
# MUSIC QUIZ. Whats ur fav genre? how many hours do u listen per week?
#When are you in the mood to jam(sad, happy)multi? What is Star sign?
st.title("Jammin' With The Stars ✧")
st.image("Images/staff.jpg")
st.write("Lets find your music archetype")
genre = st.multiselect("Which genres are your favorites?", ["Rock","Classical","Kpop","R&B","Jazz","Pop","Hiphop", "Country"])#NEW
hours = st.slider("How many hours do you jam out per week?", 0, 50, 5)#NEW
mood = st.radio("What color best describes the mood of your playlist?", ["Yellow", "Blue", "Purple", "Red"])#NEW
sign = st.text_input("What's your star sign?")#NEW
time = st.slider("What time is it right now?", 1, 24, 1)#NEW


ready = st.checkbox("Ready to explore the cosmos!")#NEW

if st.button("Reveal My Archetype"):#NEW
    if sign == "":
        st.warning("What is your star sign?")
        st.stop()
    elif ready:
        st.write("The Stars have aligned!")
        st.image("Images/constellation.jpg")

    #HOURS
        if hours > 7:
            listener = True
        else:
            listener = False
        

    #GENRE
        if len(genre) > 3:
            explorer = True
            
        else:
            explorer = False

    #TIME
        if 4 < time < 12:
            nightOwl = "early morning"
        elif 12 <= time <= 7:
            nightOwl = "afternoon"
        else:
            nightOwl = "late night"
            
    #MOOD
        if mood == "Yellow" or mood == "Red":
            passion = True
            vibe = "passionate"
        else:
            passion = False
            vibe = "chill"
            
    #ARCHETYPE
        if listener and explorer and passion:
            archetype = "Super Nova"
        elif listener and not explorer and not passion:
            archetype = "New Moon"
        elif listener and explorer and not passion:
            archetype = "Stargazer"
        elif listener and not explorer and passion:
            archetype = "North Star"
        else:
            archetype = "Space Cadet"

       



    else:
        st.warning("Let's put our space shoes on!")
        st.stop()#NEW
        
    st.write(f"Your archetype is: {archetype}!")
    
    st.balloons()#NEW
    st.success("Yay!")#NEW

    st.image("Images/zodiac.jpg")
    st.write(f"A(n) {sign} like you loves {vibe} vibes and {nightOwl} jam sessions!") 
    
    


# Create new repository in GitHub (can be named anything)
# Under configuration choose visibility to be private
# Upload script and image files into the repository
# Connect Github with streamlit (must create a streamlit account)
# Go to streamlit and deploy app
# If doesnt work you can make it public > deploy > make private
# For branch choose main for Main file path choose Home_Page.py
# Use the GitHub URL paste
