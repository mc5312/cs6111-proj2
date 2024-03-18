def gemini_prompt_generate(relation_type, sentence):
    return """
Given a sentence, extract all instances of a relationship type specified by the user that you can find in the sentence:
the possible relationship types are: "Schools_Attended", "Work_For", "Live_In", "Top_Member_Employees"

If the user specifies "Schools_Attended", the output should have the following format:
[PERSON| RELATIONSHIP| ORGANIZATION]

For example, the output of a certain sentence could be:
'["Jeff Bezos"| "Schools_Attended"| "Princeton University"]'	

If the user specifies "Work_For", the output should have the following format:
[PERSON| RELATIONSHIP| ORGANIZATION]

For example, the output of a certain sentence could be:
'["Alec Radford"| "Work_For"| "OpenAI"]'

If the user specifies "Live_In", the output should have one of the following formats:
[PERSON| RELATIONSHIP| LOCATION], 
[PERSON| RELATIONSHIP| CITY], 
[PERSON| RELATIONSHIP| STATE_OR_PROVINCE] 
[PERSON| RELATIONSHIP| COUNTRY]

For example, the output of a certain sentence could be:
 '["Mariah Carey"| "Live_In"| "New York City"]'

If the user specifies "Top_Member_Employees", the output should have the following format:
[ORGANIZATION| RELATIONSHIP| PERSON]

If the user specifies "Top_Member_Employees", the output should have the following format:
[ORGANIZATION| RELATIONSHIP| PERSON]

For example, for Top_Member_Employees, the output of the sentence:
"In 1975, he and Allen founded Microsoft in Albuquerque, New Mexico."

should be: '["Microsoft"| "Top_Member_Employees"| "Allen"]'

Each extracted relation should be on its own line. Also, retrieve as many relationships as possible!

extract "{}" relationships from the following sentence: "{}"

""".format(relation_type, sentence)