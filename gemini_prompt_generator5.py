def gemini_prompt_generate(relation_type, sentence):
    prompt = ""
    
    prompt += """

The required named entity types for each relation type are as follows:
"Schools_Attended": Subject: PERSON, Object: ORGANIZATION
"Work_For": Subject: PERSON, Object: ORGANIZATION
"Live_In": Subject: PERSON, Object: one of LOCATION, CITY, STATE_OR_PROVINCE, or COUNTRY
"Top_Member_Employees": Subject: ORGANIZATION, Object: PERSON

Examples of relations:
'["Jeff Bezos"| "Schools_Attended"| "Princeton University"]'
'["Alec Radford"| "Work_For"| "OpenAI"]'
'["Mariah Carey"| "Live_In"| "New York City"]'
'["Nvidia"| "Top_Member_Employees"| "Jensen Huang"]'


Your task is to extract relation instances, as many as possible, from a given sentence.

Each relation instance should be output in a new line in the format of [SUBJECT| RELATION| OBJECT]
A sample output for extracting 'Work_for' relationship in sentence 'Bill and Carl both work for Twitter' is as follows:
["Bill"| "Work_For"| "Twitter"]
["Carl"| "Work_For"| "Twitter"]

Now, extract relation "{}" directly from the following sentence:
{}
""".format(relation_type, sentence)

    return prompt