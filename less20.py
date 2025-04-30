def dictionary (name, surname, birth_year, birth_place, e_mail=None, tel_number=None):
    data = {'name': name,
            'surname':surname, 
            'birth_year':birth_year, 
            'birth_place':birth_place, 
            'e_mail':e_mail, 
            'tel_number':tel_number,
            'age':2025-birth_year}
    return data
print(dictionary('Rustem','Rakhmanov', 1992, 'Tashkent'))
