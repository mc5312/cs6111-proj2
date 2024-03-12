def gemini_prompt_generate(relation_type, sentence):
    return """
Given a paragraph, extract all instances of a relationship type specified by the user that you can find in the paragraph:
the possible relationship types are: "Schools_Attended", "Work_For", "Live_In", "Top_Member_Employees"

In the directions below, PERSON represents any person, RELATIONSHIP represents one of the user-specified relationships, and ORGANIZATION represents any entity, 
including a company, government, or any organization in general

If the user specifies "Schools_Attended", the output should have the following format:
[PERSON| RELATIONSHIP| ORGANIZATION]

For example, the output of a certain paragraph could be:
'["Jeff Bezos"| "Schools_Attended"| "Princeton University"]'	

If the user specifies "Work_For", the output should have the following format:
[PERSON| RELATIONSHIP| ORGANIZATION]

For example, the output of a certain paragraph could be:
'["Alec Radford"| "Work_For"| "OpenAI"]'

If the user specifies "Live_In", the output should have one of the following formats:
[PERSON| RELATIONSHIP| LOCATION], 
[PERSON| RELATIONSHIP| CITY], 
[PERSON| RELATIONSHIP| STATE_OR_PROVINCE] 
[PERSON| RELATIONSHIP| COUNTRY]

For example, the output of a certain paragraph could be:
 '["Mariah Carey"| "Live_In"| "New York City"]'

If the user specifies "Top_Member_Employees", the output should have the following format:
[ORGANIZATION| RELATIONSHIP| PERSON]

For example, the output of a certain paragraph could be:
'["Nvidia"| "Top_Member_Employees"| "Jensen Huang"]'

Each extracted relation should be on its own line. Also, retrieve as many relationships as possible!

extract "{}" relationships from the following Paragraph: "{}"

""".format(relation_type, sentence)
