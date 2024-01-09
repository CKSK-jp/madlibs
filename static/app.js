// handle when user selects a story and updates story_chosen and query string
function selectStory(story) {
  window.location.href = `/get_prompts/${story}?story_chosen=true`;
}