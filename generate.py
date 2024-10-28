from pathlib import Path
import re
import subprocess

base_url = 'https://technoon-org.github.io/gitnoon'
curriculum_dir = Path(__file__).parent

def main():
    index_markdown = f'''
# GitNoon Curriculum

Slides and tutorials for GitNoon.

## Lesson Guide for Instructors

### Before the Lesson

1. Print out the **Tutorial Speaker Notes** for the lesson so that you can read from them as you type code in a notebook
2. Familiarise yourself with the slides and speaker notes for the lesson
   * Practising the material, even by yourself, helps build confidence in the flow of the lesson!

### Slides

1. From the start of the lesson, have the initial "Get ready" or "Warm-Up Exercise" slide in the lesson's slide deck displayed on the screen.
   * Disable auto-sleep on your machine so the slides stay up even when you're not moving the mouse
   * Turn off notifications on your machine
2. Once all attendees have arrived, continue through the administration slides in the slide deck
3. If there is a **Lunch Talk** (or **DEMO-ONLY** portion of the tutorial), present that during the lunch time (allocate about 20 minutes)

### Tutorial

1. After the lunch time, show the **Tutorial Objectives** slide to outline the material that the tutorial will cover
2. You and all attendees should open a terminal from which you can `git` commands
   * Use "Git Bash" on Windows to ensure everyone has a consistent terminal environment across operating systems
   * Increase the font-size of your terminal to ensure all attendees can comfortably read it
   * Bring up the bottom of your terminal window if it won't be visible from all seats
3. Work through the **Tutorial Speaker Notes** for the lesson
   * Have the speaker notes printed out ahead of time
   * Read out (or paraphrase) written material
   * Demonstrate each command example in the terminal
   * Have attendees type along and run commands with you, and regularly check if anyone needs assistance from a helper

### Exercise and self-directed learning

1. After the tutorial, present the **Independent Work/Homework** slide
2. Direct attendees to [technoon.org/gitnoon](https://technoon.org/gitnoon) to find the lesson's slides and tutorial
3. Also offer to help with any other course-related problems that attendees may have - such as from applying what they've learned in their job

### Assets

* Find more tips for presenting from [Software Carpentry](https://carpentries.github.io/instructor-training/instructor/17-live.html#top-ten-tips-for-participatory-live-coding-in-a-workshop)

## Lessons
'''

    lesson_dirs = sorted([
        child for child in curriculum_dir.iterdir()
        if (
                child.is_dir()
                and child.name.startswith(f'lesson_')
                and not child.name.startswith('.')
        )
    ])

    for lesson_dir in lesson_dirs:
        lesson_links = []
        notebook_paths = []

        if (lesson_dir / 'slides.md').exists():
            subprocess.run([
                'pandoc',
                '-s', '-t', 'revealjs',
                '--template', str(curriculum_dir / 'revealjs' / 'pandoc.html'),
                '-o', str(lesson_dir / 'slides.html'),
                str(lesson_dir / 'slides.md'),
                '-V', 'revealjs-url=../revealjs',
            ], check=True)
            lesson_links.append(f'[Slides]({base_url}/{lesson_dir.name}/slides.html)')

        if (lesson_dir / 'tutorial.md').exists():
            subprocess.run([
                'pandoc',
                '-s', '--embed-resources',
                '--include-in-header', str(curriculum_dir / 'revealjs' / 'tutorial-head.html'),
                '--css', str(curriculum_dir / 'revealjs' / 'tutorial.css'),
                '-o', str(lesson_dir / 'tutorial.html'),
                str(lesson_dir / 'tutorial.md'),
            ], check=True)
            lesson_links.append(f'[Tutorial Speaker Notes]({base_url}/{lesson_dir.name}/tutorial.html)')

        lesson_link_bullets = '\n'.join([f'* {lesson_link}' for lesson_link in lesson_links])
        index_markdown += f'''
### {lesson_dir.name.replace('_', ' ').title()}

{lesson_link_bullets}
'''

    with Path(curriculum_dir / 'README.md').open('w') as readme_file:
        readme_file.write(index_markdown.strip())


if __name__ == '__main__':
    main()
