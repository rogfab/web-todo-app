import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


# entête de la page
st.title("Calepin Rogblog")
st.write("")
st.write("Vous pouvez enregistrer et terminer des tâches dans cette application")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enregistrer une nouvelle tâche ...",
              on_change=add_todo, key='new_todo')
