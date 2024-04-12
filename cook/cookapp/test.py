# # import google.generativeai as genai
# # import os
# # import dotenv

# # dotenv.load_dotenv()
# # key = os.environ.get('GOOGLE_API_KEY')
# # genai.configure(api_key=key)
# # # model = genai.GenerativeModel('gemini-pro')
# # # ques: str = input("Enter your question: ")
# # # response = model.generate_content(ques)
# # # print(response.text)


# # from langchain.prompts import PromptTemplate
# # from langchain_google_genai import ChatGoogleGenerativeAI
# # from langchain.chains import LLMChain

# # llm = ChatGoogleGenerativeAI(model="gemini-pro")
# # cure_template = PromptTemplate(
# #     input_variables = ['age', 'weight', 'height', 'country', 'disease', 'allergies', 'country', 'state', 'city'],
# #     template = "Diet recommendation for a {age} year old, {weight} kg, {height} cm tall, living in the area of {country}, state {state} and city {city} with {disease}, and facing allergies to {allergies}. What should be the best 6 best breakfast, lunch, snacks, dinner, workout and the best budget friendly restraunts and tips for them? Keep it short and crisp. Also mention the exact sectors of the restraunts. You dont have to mention the calories of each category ever."
# # )
# # chain_cure = LLMChain(llm = llm, prompt = cure_template)
# # input_dict = {
# #     'age': '30',
# #     'weight': '70',
# #     'height': '170',
# #     'country': 'India',
# #     'state': 'Haryana',
# #     'city': 'Gurgaon',
# #     'disease': 'diabetes',
# #     'allergies': 'gluten',
# # }
# # res = chain_cure.invoke(input_dict)
# # text = str(res['text'])
# # cleaned_text = text.replace('\n', ' ')
# # cleaned_text = cleaned_text.replace('**', '')
# # cleaned_text = cleaned_text.replace('*', '')
# # cleaned_text = cleaned_text.replace('-', '')
# # cleaned_text = cleaned_text.replace('   ', ' ')

# # import re

# # city = input_dict['city']
# # breakData = re.findall(r'Breakfast: (.*?) Lunch:', cleaned_text)
# # lunchData = re.findall(r'Lunch: (.*?) Snacks:', cleaned_text)
# # snacksData = re.findall(r'Snacks: (.*?) Dinner:', cleaned_text)
# # dinnerData = re.findall(r'Dinner: (.*?) Workout:', cleaned_text)
# # workoutData = re.findall(r'Workout: (.*?) BudgetFriendly Restaurants' + ' in ' + city + ":", cleaned_text)
# # restaurantData = re.findall(r'BudgetFriendly Restaurants' + ' in ' + city + ": (.*?) Tips:", cleaned_text)

# # breakFast = [name.strip() for name in breakData[0].strip().split('  ') if name.strip()] if breakData else []

# # lunch = [name.strip() for name in lunchData[0].strip().split('  ') if name.strip()] if lunchData else []

# # snacks = [name.strip() for name in snacksData[0].strip().split('  ') if name.strip()] if snacksData else []

# # dinner = [name.strip() for name in dinnerData[0].strip().split('  ') if name.strip()] if dinnerData else []


# # workout = [name.strip() for name in workoutData[0].strip().split('  ') if name.strip()] if workoutData else []

# # restaurant = [name.strip() for name in restaurantData[0].strip().split('  ') if name.strip()] if restaurantData else []

# from views import cure_recipes

# a = cure_recipes().input_dict

# Data provided
data = """
Breakfast: Oatmeal with berries and nuts, Glutenfree toast with peanut butter, Scrambled eggs with wholewheat toast, Yogurt with fruit and sugarfree granola, Smoothies made with fruits, vegetables, and glutenfree protein powder
Lunch: Salad with grilled chicken, quinoa, and vegetables, Glutenfree sandwich with lean protein, vegetables, and hummus, Lentil soup with glutenfree bread, Leftovers from dinner, Bean burritos with brown rice
Snacks: Fruit (apple, banana, orange), Vegetable sticks (carrots, celery), Glutenfree crackers with cheese, Yogurt, Trail mix with nuts and seeds
Dinner: Grilled salmon with roasted vegetables, Chicken stirfry with brown rice, Lentil tacos with corn tortillas, Shepherd's pie with glutenfree mashed potatoes, Vegetarian chili with glutenfree cornbread
Workout: Brisk walking for 30 minutes daily, Cycling for 20 minutes daily, Swimming for 30 minutes twice a week, Resistance band exercises (3 sets of 1012 reps for each exercise), Sports activities like basketball or soccer
Restaurant: Sector 4: Shagun Restaurant (Pure Vegetarian), Sector 5: Food Buzz (North Indian, Chinese), Sector 7: The Food Hub (Multicuisine), Sector 8: Punjabi Rasoi (Punjabi), Sector 10: Pizza Hut (Pizza, Pasta)
Tips: Monitor blood sugar levels regularly., Choose whole, unprocessed foods over sugary and processed options., Read food labels carefully to avoid glutencontaining ingredients., Consult with a registered dietitian or healthcare professional for personalized guidance., Stay hydrated by drinking plenty of water throughout the day., Get enough sleep (810 hours)., Manage stress through activities like yoga, meditation, or spending time in nature., Seek support from family, friends, or a support group to stay motivated.
"""

# Splitting the data into categories
categories = data.split('\n')

# Initializing lists for each category
Breakfast = []
Lunch = []
Snacks = []
Dinner = []
Workout = []
Restaurant = []
Tips = []

# Function to parse and assign data to lists
def parse_data(categories):
    for category in categories:
        if category.startswith("Breakfast:"):
            Breakfast.extend(category.replace("Breakfast:", "").split(", "))
        elif category.startswith("Lunch:"):
            Lunch.extend(category.replace("Lunch:", "").split(", "))
        elif category.startswith("Snacks:"):
            Snacks.extend(category.replace("Snacks:", "").split(", "))
        elif category.startswith("Dinner:"):
            Dinner.extend(category.replace("Dinner:", "").split(", "))
        elif category.startswith("Workout:"):
            Workout.extend(category.replace("Workout:", "").split(", "))
        elif category.startswith("Restaurant:"):
            Restaurant.extend(category.replace("Restaurant:", "").split(", "))
        elif category.startswith("Tips:"):
            Tips.extend(category.replace("Tips:", "").split(", "))

# Parsing the data
parse_data(categories)

# Example of accessing the lists
print("Breakfast items:", Breakfast)
print("Lunch items:", Lunch)
# Continue for other categories as needed
