# --------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# --------------------------------------------------

class Skill:
    def __init__(self):
        self.skills = ["Html", "Css", "Javascript", "Python"]

    def __str__(self):
        return f"This is my Skills =>{self.skills}"

    def __len__(self):
        return len(self.skills)


profile = Skill()
print(profile)
print(len(profile))

profile.skills.append("React")
profile.skills.append("Node")
print(len(profile))

print(profile.__class__)
my_string = "Osama"
print(type(my_string))
print(my_string.__class__)
print(dir(str))
print(str.upper(my_string))
