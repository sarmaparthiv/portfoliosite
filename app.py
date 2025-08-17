import streamlit as st
from base64 import b64encode

def web_portfolio():
    #page configuratins
    st.set_page_config(page_title="Parthiv Sarma Portfolio",page_icon="★")

    st.write(f"""
    <div class="title" style="text-align: center;">
    <span style='font-size: 32px;'>HELLO! I AM PARTHIV SARMA</span>
    </div>
    """, unsafe_allow_html=True)
    #setting the title a bit up
    st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)


    #get profile pic
    #loading dp in binary form
    with open("profile-pic.png","rb") as img_file:
        img="data:image/png;base64,"+ b64encode(img_file.read()).decode()#encoding binary content of the image in base64 string,then convert b64 strng to regular string using decode


   #reading profile
    with open("ParthivSarma_CV_.pdf","rb") as pdf_file:
     pdf_bytes=pdf_file.read()

   ####

    st.write(f"""
    <div style="display:flex;justify-content:center;">
    <div class="box">
    <img src="{img}" alt="Parthiv" style="width:280px;height:280px">
    </div>
    </div>                  
    """,
    unsafe_allow_html=True)

    ###setting the title
    st.write(f""" 
           <div class=
           "subtitle" style="text-align:center;">Computer Science & Enginnering Graduate</div>  
            """,unsafe_allow_html=True)
    ##adding socials
    social_icons_data={
        "LinkedIn":["https://www.linkedin.com/in/sarmaparthiv/","https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
        "Github":["https://github.com/sarmaparthiv/","https://cdn-icons-png.flaticon.com/128/733/733553.png"],
        "Email":["mailto:parthivk2@gmail.com","https://cdn-icons-png.flaticon.com/128/5968/5968534.png"],
        # "X":["https://x.com/parthiv_sarma","https://cdn-icons-png.flaticon.com/128/14417/14417460.png"]
    }

    ##doing list comprhension for adding the socials\
    social_icons_html=[
    f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right:10px;'>"
    f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'"
    f"style='width:25px; height:25px;'></a>"
    for platform in social_icons_data
    ]


    st.write(f""" 
    <div style="display:flex; justify-content:center;margin-bottom:20px;">
    {''.join(social_icons_html)}
    </div>""",unsafe_allow_html=True)

    ##level2 heading
    # st.write("##")

    #about me section
    st.subheader("About Me")
    st.markdown("""Hey! 👋 I’m Parthiv Sarma, a curious developer who loves solving problems with code and creating projects that make a difference. I graduated in Computer Science and Engineering from Gauhati University Institute of Science and Technology, and ever since, I’ve been exploring everything from chatbots 🤖 to hackathon projects 🚀 to Machine Learning like sentiment analysis with NLP 📊.
                
I have built projects across domains—from developing a chatbot for efficient public interaction, to building a hackathon-winning e-market platform, to conducting sentiment analysis on large-scale datasets. My technical skill set extends to Machine Learning,NLP,Deep Learning,Linux,Databases(SQL),and GitHub.

I bring not only technical knowledge but also strong communication, leadership, and collaboration skills, enabling me to thrive in both independent and team-driven environments. I am eager to apply my skills to impactful projects and continuously grow as an engineer.
    """)

    #download resume button
    # st.download_button(label="📝 Download my CV",data=pdf_bytes,file_name="Parthiv_Sarma_CV.pdf",mime="application/pdf",)

    # st.write(f"""
    # <div class="subtitle" style="text-align:center;">_______________________________________________________________________________________________
    #           </div>
    #  """,unsafe_allow_html=True)


    #education
    st.subheader("Qualifications🎓")
    st.write("""
    **✅B.TECH-COMPUTER SCIENCE & ENGINEERING(CSE)**
             
    *➜ Gauhati University Institute of Science & Technology(2019-2023)*
             
    *➜ GPA:8.84/10*

    **✅12TH-SCIENCE(PCMB)**

    *➜  KV RRL Jorhat(2017-2019)*

    *➜  Percentage:73.6%*

    **✅MATRICULATION(10th)**

    *➜  Hemalata Handiqui Memorial Institute(2017)*  

    *➜  GPA:10/10*                          
                                                                                 
    """,unsafe_allow_html=True)

    # st.write(f"""
    # <div class="subtitle" style="text-align:center;">_______________________________________________________________________________________________
    #           </div>
    #  """,unsafe_allow_html=True)

    #PROJECTS

    st.subheader("Projects🗂️")

    st.markdown("""
      
            **💼[Sentiment Analysis of Amazon Kindle Reviews](https://github.com/sarmaparthiv/Kindle-Reviews-Sentiment-Analysis)**

             *➜Preprocessed and analyzed 12,000+ Amazon Kindle reviews for sentiment classification,
             using Bag of Words and TF-IDF method*

             *➜Demonstrated ability to handle NLP tasks from preprocessing to model evaluation using 
             Python and open-source tools*

             **💼[Markett Connect E-Commerce Platform](https://github.com/sarmaparthiv/Markett-Connect)**

             *➜Project for a 24 hour Hackathon called Utkranti 4.0 held in our University,
             for which our team won the 3rd prize.*

             *➜Developed an idea for an one stop e-market platform to get various services
             online in a hussle free way.*

             **💼[GUIST-Query Bot](https://github.com/sarmaparthiv/guistbot)**

             *➜Co-Developed a chat-bot which answers some simple questions regarding our institute
             -a model for efficient public interface design.*

            """)
    # st.write(f"""
    # <div class="subtitle" style="text-align:center;">_______________________________________________________________________________________________
    #           </div>
    #  """,unsafe_allow_html=True)
    
    st.subheader("Skills👨🏻‍💻")
    st.markdown("""
            **Languages**:Python,Javascript,C.
                
            **Technologies**:SQL,Linux,Github,Google Collab,Pandas,NumPy,Sckit-Learn,NLTK,Matplotlib
                
            **Interpersonal Skills**:Communication, Leadership, Team Collaboration, Problem-Solving, Decision Making       
           
      """)
    
    #download resume button
    
    st.download_button(label="📝 Download my CV",data=pdf_bytes,file_name="Parthiv_Sarma_CV.pdf",mime="application/pdf",)

   


    #ending
    st.write("#")
    st.write(f"""
    <div class="subtitle" style="text-align:center;">Thankyou for visting!🤗
              </div>
     """,unsafe_allow_html=True)
    st.write("#")
  
    st.write(f"""
    <div class="subtitle" style="text-align:center;">⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
              </div>
     """,unsafe_allow_html=True)





    
if __name__=="__main__": 
    web_portfolio()
                       
                       
                       