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
    
 
    
    prompt += relationship_spec[relation_type]['output']

        # A sample output line is as follows:
        # [Jane Doe| Work_For| Core Rock]
    prompt += """

        Your task begins now.
        Given the following sentence, extract all instances of a '{}' relationship that you can find:
        '{}'

        """.format(relation_type, sentence)

    return prompt
