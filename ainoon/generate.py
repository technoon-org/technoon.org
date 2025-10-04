from pathlib import Path
import re
import subprocess

base_url = 'https://technoon.org/ainoon'
curriculum_dir = Path(__file__).parent

def main():
    index_markdown = f'''---
layout: default
title: AINoon Curriculum
---

# AINoon Curriculum

Slides and tutorials for AINoon.

## Lesson Guide for Instructors

### Before the Lesson

1. Print out the **Tutorial Speaker Notes** for the lesson so that you can read from them as you demonstrate on your screen
2. Familiarise yourself with the slides and speaker notes for the lesson
   * Practising the material, even by yourself, helps build confidence in the flow of the lesson!
3. Ensure attendees have created accounts for any online tools they'll be using in the tutorials

### Slides

1. From the start of the lesson, have the initial "Get ready" or "Warm-Up Exercise" slide in the lesson's slide deck displayed on the screen.
   * Use multiple displays to view slide notes on your screen while presenting the slides to attendees
     * Press "s" while viewing the slides to launch the slide notes
   * Disable auto-sleep on your machine so the slides stay up even when you're not moving the mouse
   * Turn off notifications on your machine
2. Once all attendees have arrived, continue through the administration slides in the slide deck
3. Present the **Lunch Talk** during the lunch time (allocate about 30 minutes)

### Tutorial

1. After the lunch time, show the **Tutorial Objectives** slide to outline the material that the tutorial will cover
2. Work through the **Tutorial Speaker Notes** for the lesson
   * Switch to screen mirroring so that you can work from your screen while also showing attendees
   * Increase the font-size of your terminal to ensure all attendees can comfortably read it
   * Bring up the bottom of your window if it won't be visible from all seats
   * Have the speaker notes printed out ahead of time
   * Read out (or paraphrase) written material
   * Demonstrate each step in the tutorial
   * Have attendees follow along with you, and regularly check if anyone needs assistance

### Exercise and self-directed learning

1. After the tutorial, present the **Independent Work/Homework** slide
2. Direct attendees to [technoon.org/ainoon](https://technoon.org/ainoon) to find the lesson's slides and tutorial
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

        prep_text = ''
        if (lesson_dir / 'prep.md').exists():
            with open(lesson_dir / 'prep.md') as prep_file:
                prep_text = prep_file.read().strip() + '\n'

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

{prep_text}
{lesson_link_bullets}
'''

    with Path(curriculum_dir / 'course-material.md').open('w') as readme_file:
        readme_file.write(index_markdown.strip())


if __name__ == '__main__':
    main()
