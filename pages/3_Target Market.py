import streamlit as st


st.title("Who would use the app?")

col1,col2,col3 = st.columns([1,30,1])

col2.image("./images/target_market.jpg", caption="Anyone in Education.")

tabs = ["Individuals", "Instructors", "Organisations", "Exam Providers"]
whitespace = 19
tab1, tab2, tab3, tab4 = st.tabs([s.center(whitespace, "\u2001") for s in tabs])

with tab1:
    
    
    col1,col2,col3 = st.columns([1,19,1])
    text = """
    The AI Tutor is a game-changer for individual learners embarking on the challenging journey of standardized test preparation. Whether you're a student gearing up for the SAT, AP exams, IGCSE, A-levels, TOEFL, IELTS, or any other standardized assessment, our AI-powered tool is here to provide you with personalized, actionable feedback that can make all the difference.
    """
    col2.markdown(text)

    col1,col2,col3 = st.columns([1,30,1])

    col2.image("./images/student_exam.jpg", caption="Millions of students take standardized tests every year.")

    col1,col2,col3 = st.columns([1,19,1])
    text = """
    For students, the path to academic success is often paved with practice tests and mock exams. Our application recognizes the importance of this preparation phase and offers a unique advantage: after each practice session, you receive detailed feedback that is specifically designed to help you refine your study strategy, address knowledge gaps, and build confidence. This continuous loop of assessment and improvement is crucial for effective learning and performance enhancement.

    The Generative AI feedback is not just a critique; it's a roadmap to success, guiding you through the areas that require attention and suggesting methods to strengthen your understanding. With our AI agent acting as your private tutor, the stressful period of test preparation becomes a structured, supported, and strategic experience.

    Considering the sheer number of test-takers annually, the demand for a tool like ours is substantial. Beyond standardized test prep, secondary and high school students will find our application invaluable for their academic tests and coursework. The potential user base is vast, encompassing anyone seeking to optimize their learning and achieve their educational goals.

    Discover how our application can empower you as an individual learner, providing the tailored support and guidance you need to excel in your academic pursuits. Join the multitude of students who are already enhancing their study routines and achieving greater success with the help of our AI-driven insights.
    """
    col2.markdown(text)

    st.caption("https://www.theatlantic.com/education/archive/2015/04/what-happens-when-students-boycott-a-standardized-test/390087/")

with tab2:
    col1,col2,col3 = st.columns([1,19,1])
    text = """
    Our project is a transformative tool for educators, designed to alleviate the burden of exam grading and to enhance the quality of feedback provided to students. As a former teacher, I understand firsthand the challenges and limitations of traditional grading methods. The typical outcomes—scores like 70%, grades such as 4 out of 5, or binary labels like 'passed' or 'failed'—offer little in the way of constructive guidance for students seeking to improve.    """
    col2.markdown(text)

    col1,col2,col3 = st.columns([1,30,1])

    col2.image("./images/teacher_exam.jpg", caption="Nothing is impossible.")    

    col1,col2,col3 = st.columns([1,19,1])
    text = """
    The task of providing detailed, formative feedback for each question on every student's test is a daunting, if not impossible, endeavor for any instructor. Our application turns this once-impossible task into a streamlined, efficient process. Imagine being able to upload all of your students' exam papers as image or PDF files, and within minutes, our OCR tool, coupled with our feedback mechanism, evaluates every single question for each student, delivering professional-level, personalized feedback.

    The benefits of this approach are manifold. Students receive specific, actionable insights that directly contribute to their learning process. Parents gain a clearer understanding of their child's progress and areas for improvement. And educators are empowered to focus on teaching and mentoring, rather than spending countless hours grading.

    Furthermore, our application maintains a record of each student's exam feedback, allowing for the generation of comprehensive transition reports at the end of the academic year. These reports reflect a student's progress and development, offering a valuable resource for both students and educators.

    This application is not just a tool; it's a futuristic solution for educators at all grade levels, in any country, and across all curricula. Explore how our application can revolutionize your teaching experience, providing you with the means to offer high-quality, formative feedback at scale, and ultimately enriching the educational journey for you and your students.
    """
    col2.markdown(text)

    st.caption("https://schoolsweek.co.uk/wp-content/uploads/2017/11/Workload_Large-1000x525.jpg")

with tab3:
    col1,col2,col3 = st.columns([1,19,1])
    text = """
    Leadership teams within these organizations are often in search of effective ways to enhance learning outcomes, yet they may find themselves navigating through a maze of ineffectual initiatives, misdirected technology adoption, or costly investments that fail to deliver the desired impact. The application is a strategic asset for educational organizations committed to elevating the quality of education they provide. 
    """
    col2.markdown(text)

    col1,col2,col3 = st.columns([1,30,1])

    col2.image("./images/organisation.jpg", caption="Guidance for SLTs in organisations.")    

    col1,col2,col3 = st.columns([1,19,1])
    text = """
    Our application addresses these challenges by offering a solution that prioritizes individualized reporting and data-driven insights, all within an affordable framework. By focusing on the power of personalized feedback and assessment, our tool captures the attention of educational leaders who understand the value of targeted, actionable information.

    For organizations, our system goes beyond individual student assessments. It aggregates data to evaluate class-wide, subject-specific, and grade-level performance, generating comprehensive reports that guide decision-makers. These reports are crucial for administrators and educational leaders, as they provide a clear picture of where interventions are needed, what strategies are working, and where resources should be allocated to improve the educational offerings.

    Our application is the solution that educational organizations have been seeking. It empowers them with the ability to make informed decisions based on a thorough analysis of educational outcomes. With our tool, organizations can ensure that their actions are not just well-intentioned but are also effective and aligned with their goals of providing high-quality education.

    Discover how our application can become a pivotal tool for your educational organization, enabling you to take the right actions for the betterment of your educational programs and the success of your students. Join us in transforming the educational landscape with data-driven solutions that make a real difference.
    """
    col2.markdown(text)

    st.caption("https://www.sienaheights.edu/10-reasons-leadership-is-important-in-the-workplace/")

with tab4:
    col1,col2,col3 = st.columns([1,19,1])
    text = """
    The application is poised to capture the interest of national and international test providers, such as ETS, College Board, Cambridge Assessment, and Ed-Excel. These organizations play a pivotal role in shaping educational standards and are continuously seeking innovative ways to support learners and educators in achieving success.
    """
    col2.markdown(text)

    col1,col2,col3 = st.columns([1,30,1])

    col2.image("./images/toefl.jpg", caption="Test providers")  


    col1,col2,col3 = st.columns([1,19,1])
    text = """
    We believe that these test providers will be enthusiastic about the potential of our project and will offer their support, much like they have with other educational initiatives. By providing essential documents such as assessment specifications, curriculum maps, and other resources, they can help us fine-tune our application to align perfectly with their testing frameworks.

    Organizations like the College Board have a history of collaborating with platforms like Khan Academy to enhance instructional resources, while Cambridge Assessment endorses publications that adhere to their guidelines. Our project aligns with their mission to expand access to education and improve test preparation, making us a natural partner in their efforts.

    As a unique resource, our application will complement the existing tools provided by these test providers, offering an additional layer of support to help more individuals excel in their exams. We aim to be an indispensable part of the test preparation ecosystem, providing personalized, AI-driven feedback and assessment that can make a significant difference in test outcomes.

    Explore how our collaboration with test providers can benefit your preparation journey, offering you a cutting-edge tool that is endorsed by the very organizations that design and administer the exams. With our application, test providers can extend their reach and efficacy, ensuring that every learner has the opportunity to achieve their full potential.
    """
    col2.markdown(text)
