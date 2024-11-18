class Player:
    
    def __init__(self, name=""):
        self.name = name
        self.current_location = "hotel"
        self.evidence_value = 0
        self.presented_sufficient_evidence = False
        self.chapter_visits = {
            "chapter1": 0,
            "chapter2": 0,
            "chapter3": 0,
            "chapter4": 0,
            "chapter5": 0
        }
        self.choices = {
            "chapter1": {"talk_to_guests": False, "examine_room": False, "investigate_body": False},
            "chapter2": {"talk_to_patrons": False, "talk_to_bartender": False, "go_back_to_hotel": False, "go_to_the_bathroom": False},
            "chapter3": {"talk_to_owner": False, "look_at_logbook": False, "call_police_contact": False, "go_back_to_hotel": False, "go_back_to_bar": False},
            "chapter4": {"talk_to_contact": False, "present_evidence": False, "go_back_to_hotel": False, "go_back_to_bar": False, "go_back_to_gun_store": False, "go_to_suspect": False},
            "chapter5": {"is_anyone_home": False, "talk_to_suspect": False, "look_around_residence": False, "arrest_suspect": False}
        }

    def add_evidence(self, points):
        self.evidence_value += points

    def mark_chapter_visited(self, chapter):
        if chapter in self.chapter_visits:
            self.chapter_visits[chapter] += 1

    def is_choice_selected(self, chapter, choice):
        return self.choices.get(chapter, {}).get(choice, False)

    def mark_choice_selected(self, chapter, choice):
        if chapter in self.choices and choice in self.choices[chapter]:
            self.choices[chapter][choice] = True
