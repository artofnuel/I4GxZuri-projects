
# class Student:
#     # [assignment] Skeleton class. Add your code here
#     def __init__(self):
#         pass


# Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# # Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()


class Student:

    def __init__(self, name, age, track, score):
        pass

        self.name = name
        self.age = age
        self.track = track
        self.score = score

    def change_name(self, n_name):
        self.name = n_name
        return self.name

    def change_age(self, n_age):
        self.age = n_age
        return self.age

    def add_track(self, n_track):
        self.track = n_track
        return self.track

    def get_score(self):
        return self.score

Bob = Student("Bob", 26, "FE, BE", 20.90)

Bob.change_name("Peter")
print (Bob.change_name)

