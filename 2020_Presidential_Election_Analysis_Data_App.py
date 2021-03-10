# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:14:00 2021

@author: Lenovo
"""

import streamlit as st
import pandas as pd
import matplotlib.image as mpimg

pd.set_option('display.max_colwidth', -1)
dfs1 = pd.read_csv('JoeBidenTweets.csv')
dfs2 = pd.read_csv('DonaldTrumpTweets.csv')

pos_max1 = dfs1.loc[dfs1['Compound Score']==max(dfs1['Compound Score'])]
neg_max1 = dfs1.loc[dfs1['Compound Score']==min(dfs1['Compound Score'])]

gp1 = dfs1.groupby(by=['Sentiment'])

positive_tweets1 = gp1.get_group('Positive')
negative_tweets1 = gp1.get_group('Negative')
neutral_tweets1 = gp1.get_group('Neutral')

pos_max2 = dfs2.loc[dfs2['Compound Score']==max(dfs2['Compound Score'])]
neg_max2 = dfs2.loc[dfs2['Compound Score']==min(dfs2['Compound Score'])]

gp2 = dfs2.groupby(by=['Sentiment'])

positive_tweets2 = gp2.get_group('Positive')
negative_tweets2 = gp2.get_group('Negative')
neutral_tweets2 = gp2.get_group('Neutral')

image1 = mpimg.imread('uss5.jpg')
imaged = mpimg.imread('uss3.jpg')
imagej = mpimg.imread('uss4.jpg')

image2 = mpimg.imread('JB_sentiment_distribution.png')
image3 = mpimg.imread('JB_total_tweets_wc.png')
image4 = mpimg.imread('JB_total_tweets_wf.png')

image5 = mpimg.imread('JB_positive_tweets_wc.png')
image6 = mpimg.imread('JB_positive_tweets_wf.png')

image7 = mpimg.imread('JB_neutral_tweets_wc.png')
image8 = mpimg.imread('JB_neutral_tweets_wf.png')

image9 = mpimg.imread('JB_negative_tweets_wc.png')
image10 = mpimg.imread('JB_negative_tweets_wf.png')

image11 = mpimg.imread('DT_sentiment_distribution.png')
image12 = mpimg.imread('DT_total_tweets_wc.png')
image13 = mpimg.imread('DT_total_tweets_wf.png')

image14 = mpimg.imread('DT_positive_tweets_wc.png')
image15 = mpimg.imread('DT_positive_tweets_wf.png')

image16 = mpimg.imread('DT_neutral_tweets_wc.png')
image17 = mpimg.imread('DT_neutral_tweets_wf.png')

image18 = mpimg.imread('DT_negative_tweets_wc.png')
image19 = mpimg.imread('DT_negative_tweets_wf.png')

st.title('2020 US Presidential Election Analysis Data App')

category = ["2020 Presidential Election App","Source Code"]
choice = st.sidebar.radio("Select Your Category", category)

if choice == "2020 Presidential Election App":
    
    st.image(image1, height = 750, width = 750)
    st.info("I analyzed the Tweets of the 2020 US Presidential Election Candidates, Joe Biden and Donald Trump, during their Election Campaign, to find out what exactly where they saying ")
    
    
    Candidate_Choice = st.sidebar.radio("Select the Candidate", ["President Joe Biden","Former President Donald Trump"])
            
    if Candidate_Choice == "President Joe Biden":
        
         
        st.subheader("This is the Analysis of US President Joe Biden's Twitter Account during the 2020 Presidential Election.")  
        st.image(imagej, height = 750, width = 750)                                              
        st.info("The Analysis has been performed on 3237 tweets sent from US President Joe Biden's Twitter Account during his Election Campaign.")
        
        st.subheader("The functions performed by the Data Analysis App are :")
        
        st.write("1. Displays the Tweets of President Joe Biden")
        st.write("2. Displays the Sentiment Distribution of his Tweets")
        st.write("3. Generates a wordcloud for all the Tweets")
        st.write("4. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Tweets of President Joe Biden","Display the Sentiment Distribution of his Tweets","Generate a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"])
                                                                         
        if st.button("Analyze"):
        
            if Analyzer_choice1 == "Display the Tweets of President Joe Biden":                                                      
                
                st.write("Tweets")                                                  
                st.table(dfs1.head())
            
            elif Analyzer_choice1 == "Display the Sentiment Distribution of his Tweets":                                                      
                
                st.write("Sentiment Distribution of the Tweets")                                                  
                st.image(image2, height = 1000, width = 1000)
                    
            elif Analyzer_choice1 == "Generate a wordcloud for all the Tweets":                                                      
                
                st.write("WordCloud for All the Tweets")                                                  
                st.image(image3, height = 1000, width = 1000)              
                    
            else:                                                      
                
                st.write("Most Frequent Words used in All the Tweets")                                                  
                st.image(image4, height = 1000, width = 1000)
        
        st.write("5. Displays all the the Positive Tweets")
        st.write("6. Displays his Most Positive Tweet")
        st.write("7. Generates a wordcloud for the Positive Tweets")            
        st.write("8. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Display all the the Positive Tweets","Display his Most Positive Tweet", "Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])
                                                               
        if st.button("Analyze."):        
            
            if Analyzer_choice2 == "Display all the the Positive Tweets":                                                      
                
                st.write("Positive Tweets")
                st.table(positive_tweets1.head())
                    
            elif Analyzer_choice2 == "Display his Most Positive Tweet":                                                      
                
                st.write("Most Positive Tweet")
                st.table(pos_max1)
                    
            elif Analyzer_choice2 == "Generate a wordcloud for the Positive Tweets":                                                      
                
                st.write("WordCloud for All the Positive Tweets")                                                  
                st.image(image5, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Positive Tweets")                                                  
                st.image(image6, height = 1000, width = 1000)                
        
        st.write("9. Displays all the Neutral Tweets")
        st.write("10. Generates a wordcloud for the Neutral Tweets")
        st.write("11. Displays the Most Frequent Words used in the Neutral Tweets")
        
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Display all the the Neutral Tweets", "Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])
                                                                          
        if st.button("Analyze "): 
                
            if Analyzer_choice3 == "Display all the the Neutral Tweets":                                                      
                
                st.write("Neutral Tweets")                                                  
                st.table(neutral_tweets1.head())
                    
            elif Analyzer_choice3 == "Generate a wordcloud for the Neutral Tweets":                                                      
                
                st.write("WordCloud for All the Neutral Tweets")                                                  
                st.image(image7, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Neutral Tweets")                                                  
                st.image(image8, height = 1000, width = 1000)
        
        st.write("12. Displays the Negative Tweets")
        st.write("13. Displays the Most Negative Tweets")
        st.write("14. Generates a wordcloud for the Negative Tweets")            
        st.write("15. Displays the Most Frequent Words used in the Negative Tweets")

        Analyzer_choice4 = st.selectbox("Select the Option",  ["Display all the the Negative Tweets","Display his Most Negative Tweet", "Generate a wordcloud for the Negative Tweets", "Display the Most Frequent Words used in the Negative Tweets"])
                
        if st.button("Analyze  "):       
                    
            if Analyzer_choice4 == "Display all the the Negative Tweets":                                                      
                
                st.write(" ")                                                  
                st.table(negative_tweets1.head())
                    
            elif Analyzer_choice4 == "Display his Most Negative Tweet":                                                      
                                                                  
                st.write("Most Negative Tweet")
                st.table(neg_max1)
                    
            elif Analyzer_choice4 == "Generate a wordcloud for the Negative Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Negative Tweets")
                st.image(image9, height = 1000, width = 1000)
                    
            else:                                                      
                                                                  
                st.write("Most Frequent Words used in the Negative Tweets")
                st.image(image10, height = 1000, width = 1000)
                        
    else:
                 
        st.subheader("This is the Analysis of Former US President Donald Trump's Twitter Account during the 2020 Presidential Election.")                                                        
        st.image(imaged, height = 750, width = 750)                                    
        st.info("The Analysis has been performed on 3235 tweets sent from Former President Donald Trump's Twitter Account during his Election Campaign.")

        st.subheader("The functions performed by the Data Analysis App are :")

        st.write("1. Displays the Tweets of Former President Donald Trump")
        st.write("2. Displays the Sentiment Distribution of his Tweets")
        st.write("3. Generates a wordcloud for all the Tweets")
        st.write("4. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Tweets of Former President Donald Trump","Display the Sentiment Distribution of his Tweets","Generate a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"])
                                                                 
        if st.button("Analyze"):
        
            if Analyzer_choice1 == "Display the Tweets of Former President Donald Trump":                                                      
                
                st.write("Tweets")                                                  
                st.table(dfs2.head())
            
            elif Analyzer_choice1 == "Display the Sentiment Distribution of his Tweets":                                                      
                                                                  
                st.write("Sentiment Distribution of the Tweets")
                st.image(image11, height = 1000, width = 1000)
                    
            elif Analyzer_choice1 == "Generate a wordcloud for all the Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Tweets")
                st.image(image12, height = 1000, width = 1000)              
                    
            else:                                                      
                                                                  
                st.write("Most Frequent Words used in All the Tweets")
                st.image(image13, height = 1000, width = 1000)

        st.write("5. Displays all the the Positive Tweets")
        st.write("6. Displays his Most Positive Tweet")
        st.write("7. Generates a wordcloud for the Positive Tweets")            
        st.write("8. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Display all the the Positive Tweets","Display his Most Positive Tweet", "Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])
       
                                                               
        if st.button("Analyze."):        
            
            if Analyzer_choice2 == "Display all the the Positive Tweets":                                                      
                                                                  
                st.write("Positive Tweets")
                st.table(positive_tweets2.head())
                    
            elif Analyzer_choice2 == "Display his Most Positive Tweet":                                                      
                                                                  
                st.write("Most Positive Tweet")
                st.table(pos_max2)
                    
            elif Analyzer_choice2 == "Generate a wordcloud for the Positive Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Positive Tweets")
                st.image(image14, height = 1000, width = 1000)
                    
            else:                                                     
                                                                  
                st.write("Most Frequent Words used in the Positive Tweets")
                st.image(image15, height = 1000, width = 1000)                
        
        st.write("9. Displays all the Neutral Tweets")
        st.write("10. Generate a wordcloud for the Neutral Tweets")
        st.write("11. Displays the Most Frequent Words used in the Neutral Tweets")
        
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Display all the the Neutral Tweets", "Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])
                                                                  
        if st.button("Analyze "): 
                
            if Analyzer_choice3 == "Display all the the Neutral Tweets":                                                      
                                                                  
                st.write("Neutral Tweets")
                st.table(neutral_tweets2.head())
                    
            elif Analyzer_choice3 == "Generate a wordcloud for the Neutral Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Neutral Tweets")
                st.image(image16, height = 1000, width = 1000)
                    
            else:                                                     
                                                                  
                st.write("Most Frequent Words used in the Neutral Tweets")
                st.image(image17, height = 1000, width = 1000)
        
        st.write("12. Displays the Negative Tweets")
        st.write("13. Displays the Most Negative Tweets")
        st.write("14. Generates a wordcloud for the Negative Tweets")            
        st.write("15. Displays the Most Frequent Words used in the Negative Tweets")

        Analyzer_choice4 = st.selectbox("Select the Option",  ["Display all the the Negative Tweets","Display his Most Negative Tweet", "Generate a wordcloud for the Negative Tweets", "Display the Most Frequent Words used in the Negative Tweets"])

        if st.button("Analyze  "):       
                    
            if Analyzer_choice4 == "Display all the the Negative Tweets":                                                      
                                                                  
                st.write("Negative Tweets")
                st.table(negative_tweets2.head())
                    
            elif Analyzer_choice4 == "Display his Most Negative Tweet":                                                      
                                                                  
                st.write("Most Negative Tweet")
                st.table(neg_max2)
                    
            elif Analyzer_choice4 == "Generate a wordcloud for the Negative Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Negative Tweets")
                st.image(image18, height = 1000, width = 1000)
                    
            else:                                                      
                                                                  
                st.write("Most Frequent Words used in the Negative Tweets")
                st.image(image19, height = 1000, width = 1000)
            
else:
    
    st.image(image1, height = 750, width = 750)
    
    st.graphviz_chart("""
        digraph{
        Tweet -> Sentiment
        Sentiment -> Positive
        Sentiment -> Neutral 
        Sentiment -> Negative
        Positive -> MostPositiveTweet
        Positive -> WordCloud
        Positive -> WordFrequency
        Negative -> MostNegativeTweet
        Negative -> WordCloud
        Negative -> WordFrequency
        Neutral -> WordCloud
        Neutral -> WordFrequency
        }
        """)
    
    code = """
  
import streamlit as st
import pandas as pd
import matplotlib.image as mpimg

pd.set_option('display.max_colwidth', -1)
dfs1 = pd.read_csv('JoeBidenTweets.csv')
dfs2 = pd.read_csv('DonaldTrumpTweets.csv')

pos_max1 = dfs1.loc[dfs1['Compound Score']==max(dfs1['Compound Score'])]
neg_max1 = dfs1.loc[dfs1['Compound Score']==min(dfs1['Compound Score'])]

gp1 = dfs1.groupby(by=['Sentiment'])

positive_tweets1 = gp1.get_group('Positive')
negative_tweets1 = gp1.get_group('Negative')
neutral_tweets1 = gp1.get_group('Neutral')

pos_max2 = dfs2.loc[dfs2['Compound Score']==max(dfs2['Compound Score'])]
neg_max2 = dfs2.loc[dfs2['Compound Score']==min(dfs2['Compound Score'])]

gp2 = dfs2.groupby(by=['Sentiment'])

positive_tweets2 = gp2.get_group('Positive')
negative_tweets2 = gp2.get_group('Negative')
neutral_tweets2 = gp2.get_group('Neutral')

image1 = mpimg.imread('uss5.jpg')
imaged = mpimg.imread('uss3.jpg')
imagej = mpimg.imread('uss4.jpg')

image2 = mpimg.imread('JB_sentiment_distribution.png')
image3 = mpimg.imread('JB_total_tweets_wc.png')
image4 = mpimg.imread('JB_total_tweets_wf.png')

image5 = mpimg.imread('JB_positive_tweets_wc.png')
image6 = mpimg.imread('JB_positive_tweets_wf.png')

image7 = mpimg.imread('JB_neutral_tweets_wc.png')
image8 = mpimg.imread('JB_neutral_tweets_wf.png')

image9 = mpimg.imread('JB_negative_tweets_wc.png')
image10 = mpimg.imread('JB_negative_tweets_wf.png')

image11 = mpimg.imread('DT_sentiment_distribution.png')
image12 = mpimg.imread('DT_total_tweets_wc.png')
image13 = mpimg.imread('DT_total_tweets_wf.png')

image14 = mpimg.imread('DT_positive_tweets_wc.png')
image15 = mpimg.imread('DT_positive_tweets_wf.png')

image16 = mpimg.imread('DT_neutral_tweets_wc.png')
image17 = mpimg.imread('DT_neutral_tweets_wf.png')

image18 = mpimg.imread('DT_negative_tweets_wc.png')
image19 = mpimg.imread('DT_negative_tweets_wf.png')

st.title('2020 US Presidential Election Data Analysis App')

category = ["2020 Presidential Election App","Source Code"]
choice = st.sidebar.radio("Select Your Category", category)

if choice == "2020 Presidential Election App":
    
    st.image(image1, height = 750, width = 750)
    st.info("I analyzed the Tweets of the 2020 US Presidential Election Candidates, Joe Biden and Donald Trump, during their Election Campaign, to find out what exactly where they saying ")
    
    
    Candidate_Choice = st.sidebar.radio("Select the Candidate", ["President Joe Biden","Former President Donald Trump"])
            
    if Candidate_Choice == "President Joe Biden":
        
         
        st.subheader("This is the Analysis of US President Joe Biden's Twitter Account during the 2020 Presidential Election.")  
        st.image(imagej, height = 750, width = 750)                                              
        st.info("The Analysis has been performed on 3237 tweets sent from US President Joe Biden's Twitter Account during his Election Campaign.")
        
        st.subheader("The functions performed by the Data Analysis App are :")
        
        st.write("1. Displays the Tweets of President Joe Biden")
        st.write("2. Displays the Sentiment Distribution of his Tweets")
        st.write("3. Generates a wordcloud for all the Tweets")
        st.write("4. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Tweets of President Joe Biden","Display the Sentiment Distribution of his Tweets","Generates a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"])
                                                                         
        if st.button("Analyze"):
        
            if Analyzer_choice1 == "Tweets":                                                      
                
                st.write("Tweets")                                                  
                st.table(dfs1.head())
            
            elif Analyzer_choice1 == "Sentiment Distribution of the Tweets":                                                      
                
                st.write("Sentiment Distribution of the Tweets")                                                  
                st.image(image2)
                    
            elif Analyzer_choice1 == "WordCloud for All the Tweets":                                                      
                
                st.write("WordCloud for All the Tweets")                                                  
                st.image(image3, height = 900, width = 900)              
                    
            else:                                                      
                
                st.write("Most Frequent Words used in All the Tweets")                                                  
                st.image(image4, height = 900, width = 900)
        
        st.write("5. Displays all the the Positive Tweets")
        st.write("6. Displays his Most Positive Tweet")
        st.write("7. Generates a wordcloud for the Positive Tweets")            
        st.write("8. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Display all the the Positive Tweets","Display his Most Positive Tweet", "Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])
                                                               
        if st.button("Analyze."):        
            
            if Analyzer_choice2 == "Positive Tweets":                                                      
                
                st.write("Positive Tweets")
                st.table(positive_tweets1.head())
                    
            elif Analyzer_choice2 == "Most Positive Tweet":                                                      
                
                st.write("Most Positive Tweet")
                st.table(pos_max1)
                    
            elif Analyzer_choice2 == "WordCloud for All the Positive Tweets":                                                      
                
                st.write("WordCloud for All the Positive Tweets")                                                  
                st.image(image5, height = 900, width = 900)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Positive Tweets")                                                  
                st.image(image6, height = 900, width = 900)                
        
        st.write("9. Displays all the Neutral Tweets")
        st.write("10. Generates a wordcloud for the Neutral Tweets")
        st.write("11. Displays the Most Frequent Words used in the Neutral Tweets")
        
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Display all the the Neutral Tweets", "Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])
                                                                          
        if st.button("Analyze "): 
                
            if Analyzer_choice3 == "Neutral Tweets":                                                      
                
                st.write("Neutral Tweets")                                                  
                st.table(neutral_tweets1.head())
                    
            elif Analyzer_choice3 == "WordCloud for All the Neutral Tweets":                                                      
                
                st.write("WordCloud for All the Neutral Tweets")                                                  
                st.image(image7, height = 900, width = 900)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Neutral Tweets")                                                  
                st.image(image8, height = 900, width = 900)
        
        st.write("12. Displays the Negative Tweets")
        st.write("13. Displays the Most Negative Tweets")
        st.write("14. Generates a wordcloud for the Negative Tweets")            
        st.write("15. Displays the Most Frequent Words used in the Negative Tweets")

        Analyzer_choice4 = st.selectbox("Select the Option",  ["Display all the the Negative Tweets","Display his Most Negative Tweet", "Generate a wordcloud for the Negative Tweets", "Display the Most Frequent Words used in the Negative Tweets"])
                
        if st.button("Analyze  "):       
                    
            if Analyzer_choice4 == "Negative Tweets":                                                      
                
                st.write(" ")                                                  
                st.table(negative_tweets1.head())
                    
            elif Analyzer_choice4 == "Most Negative Tweet":                                                      
                                                                  
                st.write("Most Negative Tweet")
                st.table(neg_max1)
                    
            elif Analyzer_choice4 == "WordCloud for All the Negative Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Negative Tweets")
                st.image(image9, height = 900, width = 900)
                    
            else:                                                      
                                                                  
                st.write("Most Frequent Words used in the Negative Tweets")
                st.image(image10, height = 900, width = 900)
                        
    else:
                 
        st.subheader("This is the Analysis of Former US President Donald Trump's Twitter Account during the 2020 Presidential Election.")                                                        
        st.image(imaged, height = 750, width = 750)                                    
        st.info("The Analysis has been performed on 3235 tweets sent from Former President Donald Trump's Twitter Account during his Election Campaign.")

        st.subheader("The functions performed by the Data Analysis App are :")

        st.write("1. Displays the Tweets of Former President Donald Trump")
        st.write("2. Displays the Sentiment Distribution of his Tweets")
        st.write("3. Generates a wordcloud for all the Tweets")
        st.write("4. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Tweets of Former President Donald Trump","Display the Sentiment Distribution of his Tweets","Generates a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"])
                                                                 
        if st.button("Analyze"):
        
            if Analyzer_choice1 == "Tweets":                                                      
                
                st.write("Tweets")                                                  
                st.table(dfs2.head())
            
            elif Analyzer_choice1 == "Sentiment Distribution of the Tweets":                                                      
                                                                  
                st.write("Sentiment Distribution of the Tweets")
                st.image(image11)
                    
            elif Analyzer_choice1 == "WordCloud for All the Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Tweets")
                st.image(image12, height = 900, width = 900)              
                    
            else:                                                      
                                                                  
                st.write("Most Frequent Words used in All the Tweets")
                st.image(image13, height = 900, width = 900)

        st.write("5. Displays all the the Positive Tweets")
        st.write("6. Displays his Most Positive Tweet")
        st.write("7. Generates a wordcloud for the Positive Tweets")            
        st.write("8. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Display all the the Positive Tweets","Display his Most Positive Tweet", "Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])
       
                                                               
        if st.button("Analyze."):        
            
            if Analyzer_choice2 == "Positive Tweets":                                                      
                                                                  
                st.write("Positive Tweets")
                st.table(positive_tweets2.head())
                    
            elif Analyzer_choice2 == "Most Positive Tweet":                                                      
                                                                  
                st.write("Most Positive Tweet")
                st.table(pos_max2)
                    
            elif Analyzer_choice2 == "WordCloud for All the Positive Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Positive Tweets")
                st.image(image14, height = 900, width = 900)
                    
            else:                                                     
                                                                  
                st.write("Most Frequent Words used in the Positive Tweets")
                st.image(image15, height = 900, width = 900)                
        
        st.write("9. Displays all the Neutral Tweets")
        st.write("10. Generate a wordcloud for the Neutral Tweets")
        st.write("11. Displays the Most Frequent Words used in the Neutral Tweets")
        
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Display all the the Neutral Tweets", "Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])
                                                                  
        if st.button("Analyze "): 
                
            if Analyzer_choice3 == "Neutral Tweets":                                                      
                                                                  
                st.write("Neutral Tweets")
                st.table(neutral_tweets2.head())
                    
            elif Analyzer_choice3 == "WordCloud for All the Neutral Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Neutral Tweets")
                st.image(image16, height = 900, width = 900)
                    
            else:                                                     
                                                                  
                st.write("Most Frequent Words used in the Neutral Tweets")
                st.image(image17, height = 900, width = 900)
        
        st.write("12. Displays the Negative Tweets")
        st.write("13. Displays the Most Negative Tweets")
        st.write("14. Generates a wordcloud for the Negative Tweets")            
        st.write("15. Displays the Most Frequent Words used in the Negative Tweets")

        Analyzer_choice4 = st.selectbox("Select the Option",  ["Display all the the Negative Tweets","Display his Most Negative Tweet", "Generate a wordcloud for the Negative Tweets", "Display the Most Frequent Words used in the Negative Tweets"])

    
        if st.button("Analyze  "):       
                    
            if Analyzer_choice4 == "Negative Tweets":                                                      
                                                                  
                st.write("Negative Tweets")
                st.table(negative_tweets2.head())
                    
            elif Analyzer_choice4 == "Most Negative Tweet":                                                      
                                                                  
                st.write("Most Negative Tweet")
                st.table(neg_max2)
                    
            elif Analyzer_choice4 == "WordCloud for All the Negative Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Negative Tweets")
                st.image(image18, height = 900, width = 900)
                    
            else:                                                      
                                                                  
                st.write("Most Frequent Words used in the Negative Tweets")
                st.image(image19, height = 900, width = 900)
    
"""
    st.code(code, language='python')



st.sidebar.title("Created By:")
st.sidebar.subheader("Ashutosh Shinde")
st.sidebar.subheader("[LinkedIn Profile](https://www.linkedin.com/in/ashutoshashinde/)")
st.sidebar.subheader("[GitHub Repository](https://github.com/AshutoshAShinde/2020-US-Presidential-Election-Data-App)")         
    