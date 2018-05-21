from prac_07.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python)

programming_list = [ruby, python, visual_basic]
print('The dynamically typed languages are:')
for language in programming_list:
    if language.typing == 'Dynamic':
        print(language.name)
