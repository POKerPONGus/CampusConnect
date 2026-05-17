import streamlit as st
from app.enrollment import Course

# Initialize session state
if "course" not in st.session_state:
    st.session_state.course = Course(capacity=3)

course = st.session_state.course

st.title("CampusConnect")
st.subheader("University Course Registration System")

st.write("## Enroll Student")

student_id = st.text_input("Enter Student ID")

if st.button("Enroll"):
    try:
        result = course.enroll_student(student_id)

        if result == "Success":
            st.success("Student enrolled successfully")
        else:
            st.warning(result)

    except ValueError as e:
        st.error(str(e))

st.write("## Drop Student")

drop_id = st.text_input("Enter Student ID to Drop")

if st.button("Drop"):
    try:
        result = course.drop_student(drop_id)

        if result == "Dropped":
            st.success("Student dropped successfully")
        else:
            st.warning(result)

    except ValueError as e:
        st.error(str(e))

st.write("## Course Information")

st.write(f"Course Capacity: {course.capacity}")
st.write(f"Current Enrollment Count: {course.get_enrollment_count()}")

if course.is_full():
    st.error("Course is FULL")
else:
    st.success("Course has available seats")

# Updated student list display
st.write("### Enrolled Students")

students = course.get_enrolled_students()

if students:
    for student in students:
        st.write(f"- {student}")
else:
    st.write("No students enrolled")