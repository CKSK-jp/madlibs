import os
import re

from flask import Flask, render_template, request

from stories import Story

app = Flask(__name__)


# default landing page for user
@app.route("/")
def story_selection():
    return render_template("home.html")


# handles user story selection.
@app.route("/get_prompts/<selected_story>")
def get_prompts(selected_story):
    story_chosen = request.args.get("story_chosen") == "true"

    file_path = os.path.join("data", f"{selected_story}.txt")
    print(selected_story)

    with open(file_path, "r") as file:
        template = file.read()

    prompts = re.findall(r"{(.*?)}", template)

    # should return story-chosen to hide story section and dynamically allow for form to be rendered based on story choice
    return render_template(
        "home.html",
        selected_story=selected_story,
        prompts=prompts,
        story_chosen=story_chosen,
    )


# receive request from the submitted form and instantialize a story
@app.route("/story/<selected_story>", methods=["POST"])
def generate_story(selected_story):
    file_path = os.path.join("data", f"{selected_story}.txt")
    prompts = request.form.to_dict()

    with open(file_path, "r") as file:
        text = file.read()

    new_story = Story(prompts.keys(), text)

    completed_story = new_story.generate(prompts)

    # return dynamically loaded completed story and the selected story to help with background rendering
    return render_template(
        "story_result.html", story=completed_story, selected_story=selected_story
    )


if __name__ == "__main__":
    app.run(debug=True)
