import google.generativeai as genai
import os
import dotenv
import re
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain

def load_environment_variables():
    dotenv.load_dotenv()
    return os.environ.get('GOOGLE_API_KEY')

def configure_genai(api_key):
    genai.configure(api_key=api_key)

def create_llm_chain():
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    cure_template = PromptTemplate(
        input_variables=['age', 'weight', 'stress level', 'mood', 'pressure'],
        # template="Diet recommendation for a {age} year old, {weight} kg, {height} cm tall, living in the area of {country}, state {state} and city {city} with {disease}, and facing allergies to {allergies}. What should be the best 6 best breakfast, lunch, snacks, dinner, workout and the best budget friendly restaurants and tips for them? Keep it short and crisp. Also mention the exact sectors of the restaurants. You don't have to mention the calories of each category ever."
        template = '''
Given the following details:
- Age: {age} years
- Weight: {weight} kg
- Stress Level: {stress level} out of 10
- Mood: {mood}
- Pressure: {pressure}

Please provide a comprehensive mental well-being plan that includes:
1. Customized activities and practices to address the individual's stress level and mood.
2. Sleep improvement strategies tailored to the individual's current sleep quality.
3. Exercise recommendations suitable for the individual's age, weight, and current exercise frequency.
4. Dietary suggestions considering the individual's preferences and how diet can support mental well-being.
5. Social interaction advice to enhance the individual's social well-being.

FORMAT:
MENTAL ACTIVITIES: [List of activities and practices for stress and mood improvement]
SLEEP STRATEGIES: [List of sleep improvement strategies]
EXERCISE RECOMMENDATIONS: [List of suitable exercises]
DIETARY SUGGESTIONS: [List of dietary suggestions]
SOCIAL INTERACTION ADVICE: [List of advice for enhancing social interaction]

Ensure the recommendations are concise, actionable, and tailored to the individual's profile.
                        '''
            )
    return LLMChain(llm=llm, prompt=cure_template)

def invoke_chain(chain, input_dict):
    res = chain.invoke(input_dict)
    text = str(res['text'])
    cleaned_text = clean_text(text)
    return extract_data(cleaned_text)

def clean_text(text):
    cleaned_text = text.replace('\n', ' ').replace('**', '').replace('*', '').replace('-', '').replace('   ', ' ')
    print(cleaned_text)
    return cleaned_text

def extract_data(cleaned_text):
    patterns = {
        'MENTAL ACTIVITIES': r'MENTAL ACTIVITIES: (.*?) SLEEP STRATEGIES:',
        'SLEEP STRATEGIES': r'SLEEP STRATEGIES: (.*?) EXERCISE RECOMMENDATIONS:',
        'EXERCISE RECOMMENDATIONS': r'EXERCISE RECOMMENDATIONS: (.*?) DIETARY SUGGESTIONS:',
        'DIETARY SUGGESTIONS': r'DIETARY SUGGESTIONS: (.*?) SOCIAL INTERACTION ADVICE:',
        'SOCIAL INTERACTION ADVICE': r'SOCIAL INTERACTION ADVICE: (.*?)$'
    }
    data = {}
    for key, pattern in patterns.items():
        match = re.findall(pattern, cleaned_text)
        if match:
            data[key] = [name.strip() for name in match[0].strip().split('  ') if name.strip()]
        else:
            data[key] = []
    return data


def main(input_dict):
    api_key = load_environment_variables()
    configure_genai(api_key)
    chain = create_llm_chain()

    # TRIAL INPUT
    # input_dict = {
    #             'age': "45",
    #             'weight': "78",
    #             'height': "171",
    #             'country': "India",
    #             'disease': "Diabetes",
    #             'allergies': "Gluten",
    #             'state': "Haryana",
    #             'city': "Hisar",
    #         }
    data = invoke_chain(chain, input_dict)
    output_lines = []
    for key, value in data.items():
        line = f"{key.capitalize()}: {', '.join(value)}"
        output_lines.append(line)
    return '\n'.join(output_lines)

if __name__ == "__main__":
    main()