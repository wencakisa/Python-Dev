def matchmaking(people):
    males = []
    females = []
    matchmaked = []

    for person in people:
        if person.get('gender', None) == 'male':
            males.append(person)
        else:
            females.append(person)

    for male in males:
        for female in females:
            male_interests = set(male['interests'])
            female_interests = set(female['interests'])

            male_exs = set(male['ex'])
            female_exs = set(female['ex'])

            interests = male_interests.intersection(female_interests)
            exs = male_exs.intersection(female_exs)
            age_difference = abs(male['age'] - female['age'])

            if interests and not exs and age_difference < 6:
                matchmaked.append({
                    "male": [male['name'], male['age']],
                    "female": [female['name'], female['age']],
                    "interests": list(interests)
                })

                break

    matchmaked_sorted = sorted(matchmaked, key=lambda k: k['male'][0])
    return matchmaked_sorted


def main():
    people = [
        {
            'name': "Мария",
            'interests': [
                'пътуване', 'танци', 'плуване', 'кино'
            ],
            'age': 24,
            'gender': "female",
            "ex": ["Сиско", "Венци"],
        },
        {
            'name': "Диана",
            'interests': [
                'мода', 'спортна стрелба', 'четене', 'скандинавска поезия'
            ],
            'age': 21,
            'gender': "female",
            "ex": [],
        },
        {
            'name': "Дарина",
            'interests': [
                'танци', 'покер', 'история', 'софтуер'
            ],
            'age': 34,
            'gender': "female",
            "ex": ["Борис"],
        },
        {
            'name': "Лилия",
            'interests': [
                'покер', 'автомобили', 'танци', 'кино'
            ],
            'age': 36,
            'gender': "female",
            "ex": [],
        },
        {
            'name': "Галя",
            'interests': [
                'пътуване', 'автомобили', 'плуване', 'баскетбол'
            ],
            'age': 18,
            'gender': "female",
            "ex": ['Димитър'],
        },
        {
            'name': "Валерия",
            'interests': [
                'плуване', 'покер', 'наука', 'скандинавска поезия'
            ],
            'age': 27,
            'gender': "female",
            "ex": [],
        },
        {
            'name': "Ина",
            'interests': [
                'кино', 'лов със соколи', 'пътуване', 'мода'
            ],
            'age': 20,
            'gender': "female",
            "ex": [],
        },
        {
            'name': "Кирил",
            'interests': [
                'баскетбол', 'автомобили', 'кино', 'наука'
            ],
            'age': 19,
            'gender': "male",
            'ex': ["Мария"],
        },
        {
            'name': "Георги",
            'interests': [
                'автомобили', 'футбол', 'плуване', 'танци'
            ],
            'age': 32,
            'gender': "male",
            'ex': [],
        },
        {
            'name': "Андрей",
            'interests': [
                'футбол', 'скандинавска поезия', 'история', 'танци'
            ],
            'age': 26,
            'gender': "male",
            'ex': ["Мария"],
        },
        {
            'name': "Емил",
            'interests': [
                'летене', 'баскетбол', 'софтуер', 'наука'
            ],
            'age': 34,
            'gender': "male",
            'ex': ['Дарина'],
        },
        {
            'name': "Димитър",
            'interests': [
                'футбол', 'лов със соколи', 'автомобили', 'баскетбол'
            ],
            'age': 22,
            'gender': "male",
            'ex': ['Галя'],
        },
        {
            'name': "Петър",
            'interests': [
                'пътуване', 'покер', 'баскетбол', 'лов със соколи'
            ],
            'age': 23,
            'gender': "male",
            'ex': ["Мария"],
        },
        {
            'name': "Калоян",
            'interests': [
                'кино', 'покер', 'пътуване', 'автомобили'
            ],
            'age': 29,
            'gender': "male",
            'ex': [],
        },
    ]

    matchmaked = matchmaking(people)

    for i in range(len(matchmaked)):
        print('* Couple #{}'.format(i + 1))

        for k, v in matchmaked[i].items():
            if k == 'male' or k == 'female':
                print('\t{}{}: \n\t\t-> Name: {} \n\t\t-> Age: {}'.format(
                    k[0].upper(), k[1:len(k)], v[0], v[1]))
            else:
                print('\tInterests: ')
                for interest in v:
                    print('\t\t-> {}'.format(interest))

if __name__ == '__main__':
    main()
