import re
text = "AidarIsAGreatStudentOfAGreatUniversity"
print(re.findall('[A-Z][^A-Z]*', text))