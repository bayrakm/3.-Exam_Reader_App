import streamlit as st
import openai
import json

api_key  = st.secrets["openai_api_key"]
client = openai.OpenAI(api_key=api_key)

def chat_bot(messages, model="gpt-4-1106-preview", temp=0):
    """ to chat with LLM model"""
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temp # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content

def read_string_to_json(input_string):
    """
    A function to convert string output to json file
    The input must be string of a json format.
    """
    if input_string is None:
        return None

    try:
        input_string = input_string.replace("'", "\'")  # Replace single quotes with double quotes for valid JSON
        input_string = input_string.replace("```", "") 
        input_string = input_string.replace("json", "")   
        data = json.loads(input_string)
        return data
    except json.JSONDecodeError:
        print("Error: Invalid JSON string")
        return None 

def assess_story(story):
    
    subject = "English"
    experties = f'you are an expert {subject} teacher '
    messages =  [{'role':'system', 'content':experties}]

    open_end_question_format = {"Question":"Write a story as an example of fiction style.",
                                "Student Response":f"{story}" }

    sample_output = {"Evaluation":"",
                    "Score":"",
                    "Feedback":""}
    role = 'user'

    user_message = f"""There is a question below to assess a learner's knowledge in {subject}. \

    #### Question: {open_end_question_format['Question']} \
    #### Student Response: {open_end_question_format['Student Response']}

    EVALUATE Students Response to the Question. Use your reasoning and provide a SCORE such as 50%, 30%. Finally give \
    FEEDBACK to the learner to improve himself. 

    The output MUST be a JSON file with keys exactly same as the example below. 

    Example Output: {sample_output}

    """

    messages.append({'role':role, 'content':user_message})

    response = chat_bot(messages)
    
    return read_string_to_json(response)

def mcq_evaluation(question_answer_json):
    
    subject = "Physics"
    experties = f'you are an expert {subject} teacher '
    messages =  [{'role':'system', 'content':experties}]

    open_end_question_format = question_answer_json

    sample_output = {"Evaluation":"",
                    "Feedback":""}
    role = 'user'

    user_message = f"""There is a question below to assess a learner's knowledge in {subject}. \

    #### Question: {open_end_question_format['Question']} \
    #### Student Response: {open_end_question_format['Student Response']}

    EVALUATE Students Response to the Question. Use your reasoning and provide feedback for the topic. Finally give \
    FEEDBACK to the learner to improve himself. 

    The output MUST be a JSON file with keys exactly same as the example below. 

    Example Output: {sample_output}

    """

    messages.append({'role':role, 'content':user_message})

    response = chat_bot(messages)
    
    return read_string_to_json(response)

def test_evaluation(student_responses):
    
    subject = "statistician"
    experties = f'you are an expert {subject}'
    messages =  [{'role':'system', 'content':experties}]

    student_responses = student_responses

    role = 'user'

    user_message = f"""You have the test results of a student in the following json file below.  
    The file below contains the student's demographic information: {student_responses["Student"]}

    The files below are the student's test results. Here are the descriptions of each key within the file.
    "num_qs": "Number of the question in the", 
    "correct_%": "percentage of correct answers" 
    "incorrect_%": "percentage of incorrect answers" 
    "empty_%": "percentage of empty questions"

    Here is the student's overall score on the test: 
    {student_responses["Overall_Score"]}

    Here are the student's results in each Bloom's taxonomy class:
    {student_responses["Bloom_class"]}

    Here are the student's results in each Difficulty question level:
    {student_responses["Diff_level"]}

    Here are the student's results in each Topic assessed in the test:
    {student_responses["Topics"]}

    Provide feedback for students from different perspectives by using the data provided above. Your feedback must contain /
    an evaluation of the overall score, Bloom's taxonomy cognitive skills, difficulty level and topic-wise suggestions.

    Write a clear, concise paragraph for the student. You MUST write only one paragraph to conclude your findings
    """

    messages.append({'role':role, 'content':user_message})

    response = chat_bot(messages)
    
    return response

with open("./jsons/diff_levels.json", "r") as f:
    diff_levels = json.load(f)

with open("./jsons/bloom_tax.json", "r") as f:
    blooms_tax = json.load(f)


with open("./jsons/GCSE_content.json", "r") as f:
    GCSE_content = json.load(f)

with open("./jsons/math_exam.json", "r") as f:
    math_exam = json.load(f)

with open("./jsons/student_responses.json", "r") as f:
    student_responses = json.load(f)

curriculum = "GCSE"

def create_resonse(curriculum, subject, question_type, year, topic, difficulty, bloom_class):

    experties = f'you are an expert {curriculum} {subject} teacher '
    messages =  [{'role':'system', 'content':experties}]

    question_format = {"multiple choice":{"Question": "here is the questions sentence. Write each choice in a newline \nA: choice A, \nB: choice B, \nC: choice C,\n D: choice D. ONLY one of the choice MUST be correct." ,
                                "Answer":"Correct answer of choices",
                                "Topic": "Topic within the subject that question assesses",
                                "Subtopic":"The subtopic within the topic of the question",
                                "Difficulty Level":"Difficulty level of question",
                                "Blooms Class":"Bloom's taxonomy of question"},
            "open ended":{"Question":"This is a question which require learner to show steps and explanation of the solution",
                            "Answer":"This is the step by step solution and explanations of the question NOT only the answer. Use LATEX format for any formula or math operation in the solution. Use MARKDOWN language format for the solution. PROVIDE grading rubric for each of the solution steps such as how many points for each steps.",
                            "Topic": "Topic within the subject that question assesses",
                            "Subtopic":"The subtopic within the topic of the question",
                            "Difficulty Level":"Difficulty level of question",
                            "Blooms Class":"Bloom's taxonomy of question"}}
    role = 'user'

    user_message = f"""
                    Write a {question_type} question to assess {year} students in {topic}. /
                    The question must be in difficulty level of {difficulty}. /
                    The question must assess the {bloom_class} of Bloom's taxonomy of learning. /
                    Output MUST be a json file as in {question_format[question_type]}, DO NOT change the keys. All {question_format[question_type].keys()} keys MUST be in output json object. /
                    Use {diff_levels} to decide the deficulty level of the question. /
                    Use {blooms_tax} to decide the learning level of question. 

                    Only output the JSON object nothing else.
                    """

    messages.append({'role':role, 'content':user_message})

    response = chat_bot(messages, temp=0.5)
    return read_string_to_json(response)

st.title('What to do with it?')

tabs = ["Create Question", "Open Ended Questions", "MC Questions", "Exam Reader"]
# tabs = ["Create Question", "Open Ended", "Multiple Choice"]
whitespace = 19
tab1, tab2, tab3, tab4 = st.tabs([s.center(whitespace, "\u2001") for s in tabs])
# tab1, tab2, tab3 = st.tabs([s.center(whitespace, "\u2001") for s in tabs])

with tab1: # Creating questions

    col1,col2,col3 = st.columns([1,19,1])
    text = f"""
    Explore the innovative 'Question Creation' feature of our AI Tutor: a versatile tool designed to generate tailored practice questions for students, assist educators in crafting assessments, enable publishers to enrich textbooks with engaging questions, and aid exam providers in constructing sample questions for standardized tests. 
    
    Witness the simplicity and effectiveness of this feature in action through our interactive demonstration below.
    """
    col2.markdown(text)

    with st.expander("Generate Question"):

        text = """Writing questions is a tedious job however with AI Tutor, this task is simplified. Below is an example of the creation of a single question. However, in the app, the user will have a chance to create as many questions in their selected criterion. The user will be able to create tests, mock exams, and even a book of questions by the selection. 
        
Imagine the potential use cases and target market of this app."""
        st.write(text)
        st.markdown("---")
    
        col1, col2, col3 = st.columns(3)

        # Set system to specific role of expertise
        # curriculum = "GCSE"
        with col1:
            subjects = list(GCSE_content.keys())
            subject = st.selectbox("Select Subject", options=subjects)

        with col2:
            years = list(GCSE_content[subject].keys())
            year = st.selectbox("Year Group", options=years)

        with col3:
            topics = list(GCSE_content[subject][year].keys())
            topic = st.selectbox("Topic", options=topics)

        col4, col5, col6 = st.columns(3)
        with col4:
            difficulties = list(diff_levels.keys())
            difficulty = st.selectbox('', options=difficulties, placeholder="Difficulty Level")

        with col5:
            b_class = {"1": ["Remembering", "Understanding"], "2":["Remembering", "Understanding", "Applying"], 
                       "3":["Understanding", "Applying", "Evaluating"], "4":["Applying", "Evaluating", "Creating"], 
                       "5":["Evaluating", "Creating"]}
            bloom_classes = b_class[difficulty]
            bloom_class = st.selectbox('', options=bloom_classes, index=None, placeholder="Cognitive Level")

        with col6:
            question_type = st.selectbox("", options=["multiple choice", "open ended"], index=None, placeholder="Question Type")

        
        with st.form("form1"):

            submitted = st.form_submit_button("Create Question")

            if submitted:
                response = create_resonse(curriculum, subject, question_type, year, topic, difficulty, bloom_class)

                # response = {'Question': 'A sample of radioactive isotope X has a half-life of 10 years. If a scientist starts with a 100g sample of isotope X, after 30 years, how much of the original isotope X would remain, and what fraction of the sample would be the daughter isotope? Show your analysis.',
                #     'Answer': 'After each half-life of 10 years, the amount of isotope X remaining is halved. \n\n- After the first 10 years (one half-life), 50g of isotope X would remain. \n- After 20 years (two half-lives), this amount is halved again, leaving 25g. \n- After 30 years (three half-lives), another half-life passes, so 12.5g of isotope X remains. \n\nThe fraction of the original sample that is the daughter isotope after 30 years is the complement of what remains of isotope X. Since 12.5g of isotope X remains, 87.5g has decayed into the daughter isotope. \n\nThe fraction of the daughter isotope is therefore 87.5g / 100g = 0.875 or 87.5%.\n\n**Grading Rubric:**\n- Identifying the concept of half-life (1 point)\n- Correctly calculating the amount of isotope X remaining after each half-life (3 points)\n- Calculating the amount of daughter isotope formed (1 point)\n- Expressing the final answer as a fraction (1 point)',
                #     'Topic': 'Radioactivity',
                #     'Subtopic': 'Half-life',
                #     'Difficulty Level': '3',
                #     'Blooms Class': 'Analyzing'
                #     }

                st.markdown("**Details of the questions**")
                st.markdown(f"""Topic: {response["Topic"]}""")
                st.markdown(f"""Subtopic: {response["Subtopic"]}""")
                st.markdown(f"""Difficulty level: {response["Difficulty Level"]}""")
                st.markdown(f"""Cognitive level: {response["Blooms Class"]}""")
                st.markdown("### Question")
                st.markdown(response["Question"])
                st.markdown("---")
                st.markdown("#### Answer")
                st.markdown(response["Answer"])
                st.markdown("---")

                text = f"""#### Your Turn :smile:
                
                """
                st.markdown(text)

                text = "The demonstration you've just witnessed showcases the AI Tutor's remarkable ability to swiftly generate questions tailored to specific curricula, subjects, topics, difficulty levels, and cognitive learning objectives, all within a chosen question type. This task, when performed manually, is both time-consuming and complex, especially when aiming for high-quality, diverse questions. *Attempt to manually create* **10** such questions to truly appreciate the intricate challenge educators face and the significant value that our AI Tutor's question creation feature brings to the educational landscape."
                st.markdown(text)

                
    with st.expander("A sample math test created by AI Tutor"): 

        text = "#### Question and Answers"
        st.markdown(text)

        col1,col2,col3 = st.columns([1,19,1])
        col2.image("./images/Math_Exam_answer_1.jpg")   

        col1,col2,col3 = st.columns([1,19,1])
        col2.image("./images/Math_Exam_answer_2.jpg") 

        col1,col2,col3 = st.columns([1,19,1])
        col2.image("./images/Math_Exam_answer_3.jpg") 

        col1,col2,col3 = st.columns([1,19,1])
        col2.image("./images/Math_Exam_answer_4.jpg") 

        text = "#### Exam Format"
        st.markdown(text)

        col1,col2,col3 = st.columns([1,19,1])
        col2.image("./images/Math_Exam_1.jpg") 

with tab2: # Evaluating open end question
    
    text = f""" Explore the transformative potential of our AI Tutor's feedback mechanism, adept at interpreting handwritten submissions and providing both summative grades and insightful formative feedback across multiple disciplines. Imagine the efficiency gains for educators tasked with assessing hundreds of open-ended questions—our AI makes personalized, constructive feedback a scalable reality.

    """
    st.markdown(text)
    
    with st.expander("Grading English Exam"):

        text = """This is a typical writing question and the student response contains lots of issues. Let's see how the AI tutor will handle it. \n There are two stages to evaluate student's response: \n 1. The image will be converted to digital text by our OCR tool. \n 2. Student's response will be evaluated by the LLM to provide feedback.
                """
        st.write(text)
        st.markdown("---")
        
        col1,col2,col3,col4,col5 = st.columns([1,25,1,100,1])
        col2.image("./images/Eng_Exam_student_response.jpg", caption="Student's handwritten response")

        text = f"""{student_responses["English"]["Question"]}
        """
        col4.markdown("**Question:**")
        col4.write(text)

        text = f"""{student_responses["English"]["Student Response"]}
        """
        col4.markdown("**Answer**")
        col4.write(text)

        col4.caption("Student's Response after OCR prosess*")

        with st.form("form2"):

            submitted = st.form_submit_button("Evaluate Question")         

            if submitted:
                
                response = {"Evaluation": "The student has made an attempt to write a story in a fictional style, which demonstrates an understanding of the task. However, there are several grammatical errors and issues with verb tenses, subject-verb agreement, and sentence structure that need to be addressed.",
                            "Score": "60%",
                            "Feedback": "You have a good start to your story, and your enthusiasm for the subject is clear. To improve, focus on the following areas: 1) Ensure that you use the correct verb tenses consistently throughout the story. For example, instead of 'He was very like to play football,' use 'He really liked to play football.' 2) Pay attention to subject-verb agreement; for instance, 'He play football everyday' should be 'He plays football every day.' 3) Use pronouns correctly; 'He name was Tom' should be 'His name was Tom.' 4) Work on sentence structure to make your story flow better. Try to vary your sentence beginnings and lengths to create a more engaging narrative. 5) Consider expanding on your ideas and providing more descriptive details to enhance the reader's experience. Keep practicing, and you will see improvement in your writing skills!"
                            }
                
                text = """**Here is the reasoning result of LLM on an English writing task.**"""
                st.markdown(text)
                st.markdown("---")

                st.markdown(f"""#### Evaluation """)
                st.write(f"{response['Evaluation']}")

                st.markdown(f"""##### Score: """)
                st.write(f"{response['Score']}")

                st.markdown(f"""##### Feedback""")
                st.write(f"{response['Feedback']}")

                st.markdown("---")

                st.write("The LLM model did a great job in the first attempt. I am aware that prompt engineering is an iterative process and needs time to get the best prompt for an expected outcome. However, I have limited time to submit the project for a review so here I intend to show that the concept works.")              

    with st.expander("Grading Math Exam"):
        text = """Below is an example of a student's response to a Math question which is handwritten. There is a trivial mistake even the human eye would not catch but the LLM model identified it. Take a look at whether you could catch that mistake.
                """
        st.write(text)
        st.markdown("---")
        col1,col2,col3,col4,col5 = st.columns([1,25,1,100,1])
        col2.image("./images/Math_Exam_student_response.jpg", caption="Student's handwritten response")

        text = f"""{student_responses["Math"]["Question"]}
        """
        col4.markdown("**Question 2.**")
        col4.write(text)

        text = f"""{student_responses["Math"]["Student Response"]}
        """
        col4.markdown("**Answer**")
        col4.write(text)

        col4.caption("Student's Response after OCR prosess*")

        with st.form("form3"):

            submitted = st.form_submit_button("Evaluate Question")

            if submitted:

                response = {"Evaluation": "Partially Correct. You have correctly set up the system of equations based on the given points, which is great. However, there seems to be a minor error in your final answer. Let s solve the system of equations step by step:\n\n1. From the first point (1, 6), we get the equation a + b + c = 6.\n2. From the second point (2, 11), we get the equation 4a + 2b + c = 11.\n3. From the third point (3, 18), we get the equation 9a + 3b + c = 18.\n\nNow, let s solve these equations. Subtract the first equation from the second and third to eliminate c:\n\n(4a + 2b + c) - (a + b + c) = 11 - 6, which simplifies to 3a + b = 5. (Equation 4)\n(9a + 3b + c) - (a + b + c) = 18 - 6, which simplifies to 8a + 2b = 12. (Equation 5)\n\nNow, let s solve Equations 4 and 5. Divide Equation 5 by 2 to make it easier to eliminate b:\n\n4a + b = 6. (Equation 6)\n\nSubtract Equation 4 from Equation 6:\n\n(4a + b) - (3a + b) = 6 - 5, which simplifies to a = 1.\n\nNow that we have a = 1, we can substitute it back into Equation 4 to find b:\n\n3(1) + b = 5, which simplifies to b = 2.\n\nFinally, substitute a and b back into the first equation to find c:\n\n1 + 2 + c = 6, which simplifies to c = 3.\n\nTherefore, the correct function is f(x) = x^2 + 2x + 3, which matches your final answer. However, please note that the points should be written as (x, f(x)), not (f(x), x). Despite this, you have correctly solved for the values of a, b, and c.", 
                    "Score": "7/10",  
                    "Feedback": "You have correctly set up the system of equations based on the points provided, which shows a good understanding of how to apply the function's formula to given points. However, there appears to be a minor mistake in your notation when listing the points; the points should be listed with the x-coordinate first, followed by the y-coordinate (e.g., (1, 6) instead of (6, 1)). Despite this, you've proceeded correctly by substituting the points into the quadratic function to create the system of equations. You have also correctly solved the equations to find the values of a, b, and c. Just ensure that you list the points correctly in the future to avoid any confusion. Well done!"}
                
                text = """**Here is the reasoning result of LLM on a Math task.**"""
                st.markdown(text)
                st.markdown("---")
                
                st.markdown(f"""#### Evaluation """)
                st.write(f"{response['Evaluation']}")

                st.markdown(f"""##### Score: """)
                st.write(f"{response['Score']}")

                st.markdown(f"""##### Feedback""")
                st.write(f"{response['Feedback']}")

                st.markdown("---")

                st.write("The response is generated by an LLM model. It is a long, token consuming response for the sake of demonstration however the prompt will be crafted for optimum result.")

    with st.expander("Try AI Tutor to assess yourself!"):

        text = """To test your self write your own story so the model will evaluate and score it for you and you will get feedback for free :smile:
                """
        st.write(text)
        st.markdown("---")
        
        col1,col2,col3 = st.columns([1,20,1])

        with col2:
            story = st.text_input(" ", value="Write your story here!")

        with st.form("form4"):

            submitted = st.form_submit_button("Evaluate My Story")

            if submitted:

                text = """**Here is the reasoning result of LLM on your story.**"""
                st.markdown(text)
                st.markdown("---")

                st.markdown(story)
                st.markdown("---")
                
                response = assess_story(story)

                st.markdown(f"""#### Evaluation """)
                st.write(f"{response['Evaluation']}")

                st.markdown(f"""##### Score: """)
                st.write(f"{response['Score']}")

                st.markdown(f"""##### Feedback""")
                st.write(f"{response['Feedback']}")

                st.markdown("---")

                st.write("The response is generated by an LLM model. It is a long, token consuming response for the sake of demonstration however the prompt will be crafted for optimum result.")

    st.caption("*The OCR tool is under construction.")

with tab3: # Evaluating Multiple choice questions
    text = f""" Explore the transformative potential of our AI Tutor in the education sector, designed to address the limitations of traditional multiple-choice assessments. While these tests are convenient for grading, they often fail to provide the constructive feedback necessary for student growth. Our innovative solution elevates the multiple-choice format by offering both summative and formative evaluations, delivering insightful feedback that goes beyond mere right or wrong answers. Experience this dynamic feature in action as our AI Tutor not only scores responses but also guides students towards a deeper understanding of the subject matter.
"""
    st.write(text)

    with st.expander("Feedback on MCQ"):
        text = """Typically students will not get feedback on a multiple-choice exam question which is a downside of MCQ questions. However, in the example below you will witness the AI Tutor successfully provide suggestions to students to guide his/her future learning.
                """
        st.write(text)
        st.markdown("---")
        
        col1,col2,col3,col4,col5 = st.columns([1,25,1,100,1]) 
           
        text = f"""{student_responses["MCQ"]["Question"]}
        """
        col4.markdown("**Question:**")
        col4.write(text)

        text = f"""{student_responses["MCQ"]["Answer"]}
        """
        col4.markdown("**Answer**")
        col4.write(text)

        text = f"""{student_responses["MCQ"]["Student Response"]}
        """
        col4.markdown("**Student's Response**")
        col4.write(text)

        with st.form("form5"):

            submitted = st.form_submit_button("Evaluate Question")         

            if submitted:
                
                response = mcq_evaluation(student_responses["MCQ"])
                
                text = """**Here is the reasoning result of LLM on a multiple choice question.**"""
                st.markdown(text)
                st.markdown("---")

                st.markdown(f"""#### Evaluation """)
                st.write(f"{response['Evaluation']}")

                st.markdown(f"""##### Feedback""")
                st.write(f"{response['Feedback']}")

                st.markdown("---")

                st.write("As you've witnessed in our demo, our application goes beyond simply tallying correct answers—it provides rich, detailed feedback on multiple choice questions. This feature is a game-changer for both students and educators, offering insights that foster understanding and retention. Imagine the ease with which students can identify areas for improvement and the efficiency educators gain in guiding their pupils towards academic excellence. Our feedback system is not just a tool; it's a bridge to deeper learning and more effective teaching.")              

with tab4: # Evaluating an Exam
    text = f""" 
    * description of the page - introduce the test and content - bubble answer sheet image - answer key
    * provide mc test and answer keys to be evaluated.
    * provide results in topics, diff level, bloom class 

"""
    st.write(text)

    with st.expander("Life cycle of a test"):

        st.markdown("---")

        col1,col2,col3 = st.columns([5,19,1])
        col2.image("./images/answer_sheet.png", caption="Multiple Choice Test")
        st.write("Imagine a test where test takers mark their responses on an answer sheet.")
        st.write(" ")

        st.image("./images/answer_key.png", caption="Answer keys")
        st.write("Here is the detailed answer key for the test. Each question corresponds to a bunch of information such as difficulty level, topic, and assessment objective. ")
        st.write(" ")

        st.image("./images/exam_res.png", caption="Students' Exam Responses")
        st.write("Finally, students' responses for each question in the test are used for analysis. Above is a .csv file to use in our exam reader function. ")
        st.write(" ")

        col1,col2,col3 = st.columns([4,19,1])
        col2.image("./images/student_res_bar.jpg", caption="Analysis of Test")
        st.write("Our system can evaluate tests and provide graphical analyses of the test, however, it is important to provide formative feedback to students about the overall test. Below you will find the AI Tutor in action for these feedbacks.")

    with st.expander("A Test Report"):

        st.markdown("---")

        student = student_responses["Test"]["Student"]

        col1, col2, col3, col4 = st.columns([1,1,1,1])
        col1.caption("Student Name")
        col1.write(student["Student_name"])
        col2.caption("Test Subject")
        col2.write(student["Subject"])
        col3.caption("Grade Level")
        col3.write(student["Group"])
        col4.caption("Class")
        col4.write(student["Class"])

        overall = student_responses["Test"]["Overall_Score"]
        bloom = student_responses["Test"]["Bloom_class"]
        topic = student_responses["Test"]["Topics"]
        diff = student_responses["Test"]["Diff_level"]

        st.caption("Overall Score")
        st.dataframe(overall)
        st.caption("Test Result by Topics")
        st.dataframe(topic, width=500)
        st.caption("Test Result by Cognitive Learning Class")
        st.dataframe(bloom, width=800)
        st.caption("Test Result by Question Difficulty Level")
        st.dataframe(diff, width=500)

        st.markdown("---")
        st.markdown("These summative test results are amazing insights and **provide invaluable information** about the learning process of a student. These tables are even **more effective and readable when presented on appropriate graphs** in dashboards. However, providing **formative feedback about these results** is another dimension.")

    with st.expander("AI Tutor to evaluate test"):
        st.markdown("---")
        st.markdown("Here the AI Tutor will receive the test results of a student and provide comprehensive feedback to him about the test. This is a hard task for humans but not for an LLM.")
        st.markdown("---")

        with st.form("form6"):

            submitted = st.form_submit_button("Evaluate the Test")         

            if submitted:
                
                # response = test_evaluation(student_responses["Test"])
                response = "Tommy, your overall performance in Math Exam 1 is commendable, with a solid 68% correct answers, though there's room for improvement in reducing the 30% incorrect and 2% unanswered questions. Your strengths are evident in the 'Applying' and 'Analyzing' categories of Bloom's taxonomy, where you scored above 80%, showcasing a strong ability to use and dissect information. However, 'Understanding' and 'Evaluating' require attention, as seen by lower scores, particularly the 20% of questions left blank in 'Evaluating'. Difficulty-wise, you maintained a consistent performance across levels, with a slight dip in level 3 questions. Topic-wise, you excelled in 'Geometry' and 'Number', but 'Algebra' seems to be a challenge, with nearly half of the questions incorrect. Focusing on conceptual clarity in 'Algebra' and reinforcing your 'Understanding' and 'Evaluating' skills will likely boost your overall performance and mastery of the subject. Keep up the good work, and with targeted efforts, you can achieve even higher scores."               
                
                text = """**Here is the evaluation of the test in different perpective.**"""
                st.markdown(text)
                st.markdown("---")

                st.markdown(f"""#### Feedback """)
                st.markdown(f"{response}")

                st.markdown("---")

                st.write("")              
