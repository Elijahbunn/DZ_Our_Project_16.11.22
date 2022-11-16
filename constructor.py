import EXWriting
import md_writer
import Creat2

def character_creater():
    names = ['Jo', 'Ely', 'Karl', 'Will', 'Mike', 'Los', 'Chek']
    surname = ['Holl', 'Rollins', 'Reins', 'Ambrose', 'Cena', 'Hogan', 'Orton']
    race = ['human', 'elf', 'dwarf', "giant", "insect", "slime", "technocrat", "deity", "spirit"]
    age = [21, 43, 34, 546, 12, 867, 54, 32, 56]
    growth = [189, 134, 200, 75, 354, 170, 160, 240, 88]
    clothes = ["frock coat", "Blazer", "rags", "military uniform", "naked", "beach suit"]
    facialfeatures = [i for i in range(10)]
    appearancefeatures = [i for i in range(10)]
    strength = [i for i in range(10)]
    intelligence = [i for i in range(10)]
    skills = [i for i in range(10)]
    speed = [i for i in range(10)]
    agikity = [i for i in range(10)]
    magic = [i for i in range(10)]
    
    count = 1

    while len(names) > 1:
        character = []
        Creat2.variable_creat(character, names)
        Creat2.variable_creat(character, surname)
        Creat2.variable_creat(character, race)
        Creat2.variable_creat(character, age)
        Creat2.variable_creat(character, growth)
        Creat2.variable_creat(character, clothes)
        Creat2.variable_creat(character, facialfeatures)
        Creat2.variable_creat(character, appearancefeatures)
        Creat2.variable_creat(character, strength)
        Creat2.variable_creat(character, intelligence)
        Creat2.variable_creat(character, skills)
        Creat2.variable_creat(character, speed)
        Creat2.variable_creat(character, agikity)
        Creat2.variable_creat(character, magic)
        

        EXWriting.Excel_file_writing(count, character)
        md_writer.text_md(character)
        count +=1