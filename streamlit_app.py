
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
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
