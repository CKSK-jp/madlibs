import os
import re

from flask import Flask, render_template, request

from stories import Story

app = Flask(__name__)


@app.route("/")
def story_selection():
    return render_template("home.html")


@app.route("/get_prompts/<selected_story>")
def get_prompts(selected_story):
    story_chosen = request.args.get("story_chosen") == "true"

    file_path = os.path.join("data", f"{selected_story}.txt")
    print(selected_story)

    with open(file_path, "r") as file:
        template = file.read()

    prompts = re.findall(r"{(.*?)}", template)

    return render_template(
        "home.html",
        selected_story=selected_story,
        prompts=prompts,
        story_chosen=story_chosen,
    )


@app.route("/story/<selected_story>", methods=["POST"])
def generate_story(selected_story):
    file_path = os.path.join("data", f"{selected_story}.txt")
    prompts = request.form.to_dict()

    with open(file_path, "r") as file:
        text = file.read()

    new_story = Story(prompts.keys(), text)

    completed_story = new_story.generate(prompts)

    return render_template("story_result.html", story=completed_story)


if __name__ == "__main__":
    app.run(debug=True)
