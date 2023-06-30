import solara as sol

# Declare reactive variables at the top level. Components using these variables
# will be re-executed when their values change.
sentence = sol.reactive("Solara makes our team more productive.")
word_limit = sol.reactive(10)
MeatSelection = sol.reactive("beef")
Meats = "Beef Chicken Turkey".split()


@sol.component
def Page():
    # Calculate word_count within the component to ensure re-execution when reactive variables change.
    word_count = len(sentence.value.split())

    sol.SliderInt("Word limit", value=word_limit, min=5, max=20)
    sol.Markdown(f"The word limit is {word_limit}")
    sol.InputText(label="Your sentence", value=sentence, continuous_update=True)
    with sol.Row():
        sol.Button("reset", on_click=lambda: word_limit.set(10))

    # Display messages based on the current word count and word limit.
    if word_count >= int(word_limit.value):
        sol.Error(f"With {word_count} words, you passed the word limit of {word_limit.value}.")
    elif word_count >= int(0.8 * word_limit.value):
        sol.Warning(f"With {word_count} words, you are close to the word limit of {word_limit.value}.")
    else: 
        sol.Success("Great short writing!")
    #st.caption("this is a _caption_")

    sol.Select(label = "Meat", value = MeatSelection, values = Meats)
    sol.Markdown(f"the Burger protein selected is {MeatSelection.value}")


# The following line is required only when running the code in a Jupyter notebook:
Page()