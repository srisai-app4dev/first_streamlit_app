
import streamlit
streamlit.title('Hi, My name is Aishvariya. I Love Sri very much')
streamlit.header('My mom\'s healthy diner breakfast recipes')
streamlit.text('🥣 Omega 3 & Blueberry Oatmestreamlit.dataframe(my_fruit_list)al')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie or milkshakes 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Pineapple','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
#new section to display fruityvice api response

streamlit.header('Fruityvice Fruit Advice!')
fruit_choice=streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered',fruit_choice)
import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

add_my_fruit=streamlit.text_input('what fruit would you like to add?','apple')
streamlit.write('The user entered the 2nd fruit as',add_my_fruit)

fruityvice2_response=requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)
fruityvice2_normalized=pandas.json_normalize(fruityvice2_response.json())
streamlit.dataframe(fruityvice2_normalized)
streamlit.text('Thanks for adding', add_my_fruit)
