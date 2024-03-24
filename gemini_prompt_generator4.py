def gemini_prompt_generate(relation_type, sentence):
    prompt = ""
    
    relationship_spec = {
        'Schools_Attended': {
            'description': """
                A 'Schools_Attended' relationship type captures relationships that a PERSON attended for an educational ORGANIZATION, e.g. a school or a university.
                """,
            'output': """
                The extracted relation should be in this format: "[PERSON| RELATIONSHIP| ORGANIZATION]"
                Skip an instance if the name of ORGANIZATION is not provided in the sentence.
                """
        },
        'Work_For': {
            'description': """
                A 'Work_For' relationship type captures relationships that a PERSON works for an ORGANIZATION.
                """,
            'output': """
                The extracted relation should be in this format: "[PERSON| RELATIONSHIP| ORGANIZATION]"
                """
        },
        'Live_In': {
            'description': """
                A 'Live_In' relationship type captures relationships that a PERSON lives in a place, which can be a LOCATION, CITY, STATE_OR_PROVINCE, COUNTRY.
                """,
            'output': """
                The extracted relation should be in one of these formats: 
                "[PERSON| RELATIONSHIP| LOCATION]" or 
                "[PERSON| RELATIONSHIP| CITY]" or 
                "[PERSON| RELATIONSHIP| STATE_OR_PROVINCE]" or 
                "[PERSON| RELATIONSHIP| COUNTRY]"
                """ 
        },
        'Top_Member_Employees': {
            'description': """
                A 'Top_Member_Employees' relationship type captures relationships that an ORGANIZATION has a PERSON as one of the top member employees.
                """,
            'output': """
                The extracted relation should be in this format: "[ORGANIZATION| RELATIONSHIP| PERSON]"
                """
        }
    }


    prompt += """
        Your task is to extract one or more relationship instances from a given sentence.
        There can be more than one relationship instance in a sentence. Extract as many as possible.

        Each RELATIONSHIP instance should be output in a new line.
        A sample output for extracting 'Work_for' relationship in sentence 'Bill and Carl both work for Twitter' is as follows:
        [Bill| Work_For| Twitter]
        [Carl| Work_For| Twitter]
        """ 
    
    prompt += relationship_spec[relation_type]['description']
    

    # prompt += """
    #     Your task is to extract multiple relationship instances from a given sentence.
    #     There can be more than one relationship instance in one sentence. Extract as many as possible.

    #     The extracted relation will be in the format of '[Subject| Relationship| Object]'
    #     Only extract relation in which both 'Subject' and 'Object' are present in the sentence.
    #     Each extracted relation should be on its own line.

    #     A sample output for extracting 'Work_for' relationship in sentence 'Bill and Carl both work for Twitter' is as follows:
    #     [Bill| Work_For| Twitter]
    #     [Carl| Work_For| Twitter]
    #     """ 
    
    prompt += relationship_spec[relation_type]['output']

        # A sample output line is as follows:
        # [Jane Doe| Work_For| Core Rock]
    prompt += """

        Your task begins now.
        Given the following sentence, extract all instances of a '{}' relationship that you can find:
        '{}'

        """.format(relation_type, sentence)

    return prompt
#     return """
# Given a sentence, extract all instances of a relationship type specified by the user that you can find in the sentence:
# the possible relationship types are: "Schools_Attended", "Work_For", "Live_In", "Top_Member_Employees"

# Note that for all text below: PERSON, RELATIONSHIP, LOCATION, STATE_OR_PROVINCE, COUNTRY, ORGANIZATION all correspond to entities
# that would be found by named-entity recognition.

# If the user specifies "Schools_Attended", the output should have the following format:
# [PERSON| RELATIONSHIP| ORGANIZATION]

# For example, for "Schools_Attended", the output of the sentence:
# "He was born to parents John Doe and Jane Doe, who both attended University of Florida"

# should be :
# '["John Doe"| "Schools_Attended"| "University of Florida"]
# ["Jane Doe"| "Schools_Attended"| "University of Florida"]'

# As another example, for "Schools_Attended", the output of the sentence:
# "University of Florida student Jane Doe studies Biology"

# should be: '["Jane Doe"| "Schools_Attended"| "University of Florida"]'

# As another example, for "Schools_Attended", the output of the sentence:
# "Professor Emeritus John Doe of University of Florida still loves hiking at the age of 87"

# should be: '["John Doe"| "Schools_Attended"| "University of Florida"]'


# If the user specifies "Work_For", the output should have the following format:
# [PERSON| RELATIONSHIP| ORGANIZATION]

# For example, for "Work_For", the output of the sentence:
# "Core Rock was managed by Jane Doe before she left for a new opportunity at Tesla"

# should be:
# '["Jane Doe"| "Work_For"| "Core Rock"]'
# ["Jane Doe"| "Work_For"| "Tesla"]'

# If the user specifies "Live_In", the output should have one of the following formats:
# [PERSON| RELATIONSHIP| LOCATION], 
# [PERSON| RELATIONSHIP| CITY], 
# [PERSON| RELATIONSHIP| STATE_OR_PROVINCE] 
# [PERSON| RELATIONSHIP| COUNTRY]

# The "Live_In" relation captures the relationship between a PERSON who is currently living, or has lived, 
# in a certain LOCATION, CITY, STATE_OR_PROVINCE, or COUNTRY. The sentence must provide evidence that the person lived in
# the place for a sustained period of time, and wasn't simply visiting.

# For example, for "Live_In", the output of the sentence:
# "John Doe was born in Austin" 

# should be:
# '["John Doe"| "Live_In"| "Austin"]'

# If there is no explicit statement that the person lived or ever lived in a certain place, then do not include that relation for "Live_in"

# If the user specifies "Top_Member_Employees", the output should have the following format:
# [ORGANIZATION| RELATIONSHIP| PERSON]

# For example, for Top_Member_Employees, the output of the sentence:
# "In 1975, he and Allen founded Microsoft in Albuquerque, New Mexico."

# should be: '["Microsoft"| "Top_Member_Employees"| "Allen"]'

# Each extracted relation should be on its own line. Also, retrieve as many relationships as possible!

# extract "{}" relationships from the following sentence: "{}"

# """.format(relation_type, sentence)
