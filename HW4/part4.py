def choosePartyPeople(personList, relations):
    total = len(personList)
    if total < 11:
        return None
    
    relationMap = {}
    
    # Following loop creates a relationMap that has relativeList as value for every person in list
    for person in personList:
        for relation in relations:
            if person == relation[0] or person == relation[1]:
                if person == relation[0]:
                    relationMap = addToMapSet(relationMap, person, relation[1])
                else:
                    relationMap = addToMapSet(relationMap, person, relation[0])
        
    
    partyPeople = set()
    # Using relationMap we add every possible candidates for our party according to their known unknown count and adding their relatives to meet that requirement
    for person in relationMap.keys():       
        known = len(relationMap[person]) 
        if known >= 5 and total - known - 1 >= 5:
            partyPeople.add(person)
            for relative in relationMap[person]:
                partyPeople.add(relative)
    
    # After creating initial partyPeople list with all relatives according to known / unknown rate we also need to double check people we added as relatives
    # To do that we constantly iterate over the list until it is valid.
    i = 0
    initialPartyLength = len(partyPeople)
    while len(partyPeople) > 0:
        isValid = True
        peopleToRemove = set()

        for person in partyPeople:
            peopleToRemoveFromRelation = set()
            for relative in relationMap[person]:
                if not partyPeople.__contains__(relative):
                    peopleToRemoveFromRelation.add(relative)  # we need to remove them if they're not in party list.
            for relative in peopleToRemoveFromRelation:
                relationMap[person].remove(relative)
            
            known = len(relationMap[person])
            if known < 5 or total - known - 1 < 5:
                peopleToRemove.add(person)
                isValid = False

        if isValid and i > initialPartyLength:
            break
        else: 
            for person in peopleToRemove:
                partyPeople.remove(person) # remove non legal party people

        i += 1

    return partyPeople



def addToMapSet(map, key, value):
    if map.keys().__contains__(key):
        map[key].add(value)
    else:
        map[key] = set()
        map[key].add(value)
    return map

def main():
    people = ["Onur", "Ali", "Ahmet", "Enes", "Halil", "Mehmet", "Veli", "Rıza", "Ergani", "Öztürk", "Erdoğan", "Çeçen", "Barış", "Rıza" ]

    # Relations inserted with loop to the list of 2 element lists
    relations = []
    z = 0
    for i in range(len(people)):
        if z == 5:
            break
        person = people[i]
        for j in range(5):
            index = (i + j + 1) % len(people)
            relations.append([person, people[index]])
        z += 1

    print(choosePartyPeople(people, relations))

main()