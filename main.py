def bio_data():
    first_name = input("Enter first name: ")
    second_name = input("Enter second name")
    gender = input("Enter gender: ")
    city = input("Enter city: ")
    country = input("Enter country")
    course_study = input('enter course study')
    return f"My name is  {first_name} {second_name}, I am a {gender} and leave in {city} {country}. I am in Pora Academy to study {course_study}"

print(bio_data())
