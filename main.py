import streamlit as st
import task_recommendation.analyze as anal

st.title( "Task Priortization and Roadmap Preparation Model")

task = st.text_input("Enter you task")

if task != "" :
    priority = anal.recommend_priority(task)

    st.write("Priority of the task you provided is "+priority)

    roadmap = anal.recommend_roadmap(task)
    
    module = anal.recommend_module(task)

    st.write("-----------------------------------------------------------------------------------------------")

    st.title("## Roadmap ")
    st.write(roadmap)

    st.write("----------------------------------------------------------------------------------------------")

    st.title("## Modules ")
    st.write(module)

    st.write("-------------------------------------------------------------------------------------------")

    query = st.text_input("Enter your Query")

    if query != "" :
        query_resolution = anal.recommend(task , query)
        st.write(query_resolution)


    
    