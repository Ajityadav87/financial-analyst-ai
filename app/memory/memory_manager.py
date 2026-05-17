chat_history = []


def add_to_memory(
    question,
    answer
):

    chat_history.append(
        {
            "question": question,
            "answer": answer
        }
    )


def get_memory():

    history_text = ""

    for item in chat_history:

        history_text += (
            f"User: {item['question']}\n"
        )

        history_text += (
            f"Assistant: {item['answer']}\n\n"
        )

    return history_text