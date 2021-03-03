 # Data 
- 170 posts for hot and new for each subbreddit per day (add date from the filename)
- Chose to divide the data into hot and new to diversify our data
- Extracted data at exact times for 3 consective days to stay consistent with the results
- So ended up with 2040 posts
- filtered out the biden and trump mentions ( check count from the submitted)
- kept the original 2040 posts for tfidf


# Methods
- Wrote code to extract all the data from hot and new
- Explain coding of decisions you made
- For example, used regex for Biden and Trump
- Considered cases where Joe or Donald where written seperately
- Proof readed the extracted posts to see if a different context was added
- Another person wrote another code to get the same exact output
- Compared the results of both outputs to see if they match with the expected output
- removing duplicates from 12 csv files 
- To allow a single user to make multiple different posts, wrote code to remove rows with identical userids and posts
- To calculate accurate tfidf, also considered this fact for non-biden non-trump
- For tftdf, wrote code - 

# Results
## * List of topics 
#### 1. Biden Campaign:
        - Any statement which seems to be from a Biden Supporter. It Could include bashing Trump, speaking up for Biden and supporting Biden in the election run
        - Any statement/post from a Republican representative describing their election campaign
        Examples: Add 2 for each
#### 2. Trump Campaign:
        - Any statement which seems to be from a Biden Supporter. It Could include bashing Trump, speaking up for Biden and supporting Biden in the election run
        - Any statement/post from a Republican representative describing their election campaign
#### 3. Media:
        - Any update/post about the elections from any social media or television channels.(add accordingly) 
#### 4. Biden Tenure:
           - Any steps that Biden or the newly appointed government is taking after taking leadership
           - Suggestions on the new role
           - Expectations from the new roles
           - Newly appointed members 
           - Biden's plans after taking charge example take on climate change
#### 5. Covid 19:
        - Any posts related to the pandamic and how it is effecting the elections
#### 6. Trump Controversy:
       - Any update/post on problems that Trump has indulged into
            - Him not leaving the white house
            - Illegal activities and law suits on him
#### 7. Voting:
       - Any posts resulting in the counting of votes
       
#### Make sure to add an example for all the topics
# Discussions:

- Discussion of topics and its impact on each sub-topics
- TFIDF findings

## Group Members
#### Ibrahim:
#### Saad:
#### Vasu: 

