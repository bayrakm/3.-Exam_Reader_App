import streamlit as st

st.title('AI Tutor')

col1,col2,col3 = st.columns([1,19,1])

col2.image("./images/AI-Teacher.jpg", caption="An AI agent to help")


tabs = ["Overview", "Question", "Read Exam", "Feedback", "Councelor"]
whitespace = 14
tab1, tab2, tab3, tab4, tab5 = st.tabs([s.center(whitespace, "\u2001") for s in tabs])

with tab1:
        
    col1,col2,col3 = st.columns([1,19,1])
    text = """
    Welcome to the future of education, where the power of **Generative AI** transforms the way we assess and enhance learning. Our innovative application is designed to revolutionize the educational landscape by focusing on a critical yet often overlooked component of the teaching-learning process: **formative evaluation**.
    """
    col2.markdown(text)

    col1,col2,col3 = st.columns([1,30,1])

    col2.image("./images/Assessment.jpg", caption="Summative Assessment!")

    col1,col2,col3 = st.columns([1,19,1])
    text = """
    In the realm of education, preparation and instruction have long been supported by a wealth of resources, from comprehensive curricula to engaging lesson plans and interactive presentation slides, many of which are readily accessible online. However, when **it comes to assessment, the tools available are predominantly geared towards summative results, providing a snapshot of learning outcomes without offering much in the way of ongoing, personalized guidance.**

    Recognizing this gap, our application steps in to fill the void with a cutting-edge formative evaluation tool that leverages Generative AI to deliver tailored feedback and actionable insights. Our goal is not to replace the existing preparation or instruction materials but to complement them by equipping educators and learners with a dynamic means of tracking and improving the learning process.

    Our application is designed to cater to a diverse range of users, from individual students and teachers to educational institutions of all sizes. By providing personalized guidance based on formative assessment outcomes, we empower users to identify areas for improvement, adjust their learning strategies, and achieve better educational results.

    We embark on this journey to enhance education through AI-driven insights, fostering a more informed, adaptive, and successful learning experience for all. 
    """
    col2.markdown(text)

    st.caption("https://unsplash.com/photos/woman-in-white-shirt-using-microsoft-surface-laptop-3-in-platinum-DMVU0XqiT90?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash")

with tab2:
        
    col1,col2,col3 = st.columns([1,19,1])
    text = """
    This innovative tool harnesses the power of Generative AI to generate high-quality, curriculum-aligned questions complete with solutions and detailed explanations.

    """
    col2.markdown(text)

    col1,col2,col3 = st.columns([1,30,1])

    col2.image("./images/Questions.png", caption="Summative Assessment!")

    col1,col2,col3 = st.columns([1,19,1])
    text = """
    Educators can input specific topics, difficulty levels, and question formats (multiple choice, short answer, essay, etc.) to generate tailored questions that align with their lesson plans and assessment goals. Alongside each question, the AI generates a corresponding solution, ensuring that educators have ready-to-use material for teaching and assessment. To enhance understanding, the AI provides in-depth explanations for each question, delving into the concepts being tested and offering insights into the problem-solving process. 
    
    Students can use the feature to create practice questions, allowing them to test their knowledge, identify areas for improvement, and prepare effectively for exams. Teachers save significant time in exam preparation, freeing them to focus on teaching and personalized student support. Students benefit from personalized practice sessions that adapt to their learning pace and style.

    The "Preparing Question" feature is not just a tool; it's a comprehensive solution for the educational industry's assessment needs. It empowers educators with efficiency and supports students in achieving academic excellence. By integrating this AI-driven feature into our web application, we are setting a new standard for educational resources and paving the way for a smarter, more effective learning experience.   
    """
    col2.markdown(text)

    st.caption("https://images.squarespace-cdn.com/content/v1/534c20f3e4b0b51fbb0ee82e/1444424846630-FGHQAL2DBBVS3UQKCGUC/image-asset.jpeg")

with tab3:
    col1,col2,col3 = st.columns([1,19,1])
    text = """
Introducing the Exam Reader, a cornerstone feature of our Generative AI application, designed to seamlessly bridge the gap between traditional assessment methods and the digital realm. At the heart of our project, the Exam Reader is an advanced OCR (Optical Character Recognition) tool that meticulously converts handwritten student responses into a digital format, paving the way for a more efficient and accurate evaluation process.

    """
    col2.markdown(text)

    col1,col2,col3 = st.columns([1,30,1])

    col2.image("./images/Exam_reader.jpg", caption="Optical Character Recognition")    

    col1,col2,col3 = st.columns([1,19,1])
    text = """
Our Exam Reader is adept at processing a wide array of answer sheets, from bubble forms used in standardized testing to paper-based multiple-choice exams. But its capabilities extend far beyond the recognition of structured responses. The tool is equally proficient in deciphering open-ended answers, such as essays, making it an invaluable asset for comprehensive assessment.
    
Leveraging the latest breakthroughs in Generative AI technology, including models like Google's GEMINI and Azure's AI custom form evaluation tools, the Exam Reader can extract information from images of handwritten texts with remarkable precision. This means that users can simply upload images of their exam sheets, and our system will handle the intricate task of data extraction.

The Exam Reader is not just a concept; it's a practical solution that users can experience firsthand. To understand how it integrates into the assessment process and enhances the learning experience, we invite you to explore the use cases section of our website. Here, you'll find real-world examples demonstrating the Exam Reader's capabilities and the transformative impact it can have on educational evaluation.
    """
    col2.markdown(text)

    st.caption("https://www.labellerr.com/blog/content/images/2023/06/banner.webp")

with tab4:
    col1,col2,col3 = st.columns([1,19,1])
    text = """
Meet the Private Tutor, a sophisticated component of our educational ecosystem that elevates the assessment experience to new heights. The Private Tutor is a finely calibrated LLM (Large Language Model) that is meticulously fine-tuned to align with specific educational curricula, ensuring that the feedback it provides is both relevant and curriculum-specific.
    """
    col2.markdown(text)

    col1,col2,col3 = st.columns([1,30,1])

    col2.image("./images/Tutor.jpg", caption="A private tutor all the time at your fingertips.")    

    col1,col2,col3 = st.columns([1,19,1])
    text = """
Imagine having a personal tutor at your fingertips, one that is tailored to the exact requirements of your educational program. Whether you're a student practicing for the SAT Math section or preparing for your GCSE Physics exams, the Private Tutor is equipped to offer expert-level guidance. Our system selects a model that has been fine-tuned with the appropriate curriculum, such as the US High School math standards for SAT preparation or the GCSE specifications for UK secondary education.

The process of fine-tuning these models is streamlined by the public availability of curriculum specifications within the education sector. This accessibility allows us to create highly specialized models that can evaluate user inputs with precision and provide professional feedback and actionable suggestions.

Quality assurance is at the forefront of our service. We meticulously craft our prompts to extract the most beneficial insights from the model, ensuring that the feedback you receive is not only accurate but also constructive. The formative feedback provided by the Private Tutor is designed to be a game-changer, offering a level of personalized attention that is unparalleled by traditional summative assessments.

This personalized feedback opens doors to equal educational opportunities for learners across the globe. Users can track their progress over time, saving suggestions and comparing them across various mock exams to monitor their improvement.

Explore the transformative potential of the Private Tutor on our website, where you can discover how our application can become your personal companion in the journey towards academic excellence.
    """
    col2.markdown(text)

    st.caption("https://www.additudemag.com/does-my-child-need-a-tutor/")

with tab5:
    col1,col2,col3 = st.columns([1,19,1])
    text = """
Envision a future where the journey to higher education is demystified and personalized through the power of AI. Our application's extension plan includes the development of a virtual College Counselor, an AI-driven guide that mirrors the role of a traditional college advisor within a high school setting.
    """
    col2.markdown(text)

    col1,col2,col3 = st.columns([1,30,1])

    col2.image("./images/college_counselor.jpg", caption="Plan your future ahead.")  


    col1,col2,col3 = st.columns([1,19,1])
    text = """
The College Counselor feature is designed to harness the comprehensive data profile of each student, including their test preparation exam results, academic strengths, and subject weaknesses. By integrating a model fine-tuned with data on college admissions processes and guidance, this AI agent will be able to offer bespoke recommendations tailored to each user's unique academic profile and aspirations.
    
Imagine an AI that can evaluate your educational achievements and extracurricular experiences to suggest colleges and universities where you are likely to thrive. It could provide insights into the likelihood of admission, scholarship opportunities, and even recommend career paths that align with your skills and interests.

While this step is currently conceptual, it represents the vast potential of our AI application to extend beyond assessment and into the realm of strategic educational planning. College counseling is just one example of how our technology could evolve to offer end-to-end support for students navigating the complexities of post-secondary education and career development.

Stay tuned for updates on this exciting extension of our project, where the goal is to create an AI companion that not only evaluates academic performance but also illuminates the path to future success.
    """
    col2.markdown(text)

    st.caption("https://www.bacp.co.uk/bacp-journals/university-and-college-counselling/")

st.caption("https://feweek.co.uk/how-chatgpt-could-reduce-and-transform-teacher-workload/")



