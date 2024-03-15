# Website Template

## How to test your website locally
1. Install [Docker](https://docs.docker.com/engine/install/) and
   [Docker Compose](https://docs.docker.com/compose/install/)
2. Clone your repo
3. Watch your website while editing: `make serve`

## How to customize

### Changing the names
- Open `_config.yml`
- Update `course_name`, `course_semester`, and `course_description` (this will appear in the home page).
- Update `schoolname`, `schoolurl`, `twitter_username`, and `address` accordingly.
- (Optional) Enter your Google Analytics tracking ID in the `google_analytics` field (Remember to uncomment it).
- Add more content to your home page: Update `index.md` (it supports Markdown!)
- Update course staff info at `_data/people.yml` (You may need to upload the profile pics to `_images` folder.
- (Optional) Open `_data/previous_offering.yml` and update the data if needed.

### Change the looks
- Open `_sass/_user_vars.scss`
- You can change the colors manually to match your branding
### Contents
#### Lectures
To add a new lecture, create an empty file with `.md` postfix in `_lectures/` directory. fill it using below template:
```markdown
---
type: lecture
date: 20xx-xx-xxTx:xx:xx+4:30
title: <Title of this lecture>

# optional
# please use /static_files/notes directory to store notes
thumbnail: /static_files/path/to/image.jpg

# optional
tldr: "What is AI? How does it impact our lives? The current state of the art."

# optional
# set it to true if you dont want this lecture to appear in the updates section
hide_from_announcments: false

# optional
links:
    - url: /static_files/presentations/lec.zip
      name: notes
    - url: /static_files/presentations/code.zip
      name: codes
    - url: https://google.com
      name: slides
    - url: https://example.com
      name: other
---
<!-- Other additional contents using markdown -->
**Suggested Readings:**
- [Readings 1](http://example.com)
- [Readings 2](http://example.com)
```

#### Assignments
To add a new assignments, create an empty file with `.md` postfix in `_assignments/` directory. fill it using below template:
```markdown
---
type: assignment
date: 20xx-xx-xxTx:xx:xx+4:30
title: <Assignment title (e.g. Assignment #1>

# optional
pdf: /static_files/assignments/assign_01.pdf

# optional
solutions: /static_files/assignments/assign_01_solutions.pdf

# optional
attachment: /static_files/assignments/assign_01_attachment.zip

# optional
# set it to true if you don't want this assignment to appear in the announcements section
hide_from_announcments: false

due_event:
    type: due
    date: 20xx-xx-xxTx:xx:xx+4:30
    description: 'Assignment #1 due'
---
<!-- Other additional contents using markdown -->
```

#### Dues & Deadlines
Use `_events/` directory to add new a deadline, use `type: due`. These events will apear at the schedule page.
```markdown
---
type: due
date: 20xx-xx-xxTx:xx:xx+4:30
description: <Description of deadline (e.g. 'Final report due')>

# optional
# set it to true if you don't want this event to appear in the announcements section
hide_from_announcments: false
---
```

#### Exams
Use `_events/` directory to add new Exam alert, use `type: exam`. These events will apear at the schedule page.
```markdown
---
type: exam
date: 20xx-xx-xxTx:xx:xx+4:30
description: <Description of the exam (e.g. 'The midterm exam')>

# optional
# set it to true if you don't want to this event appear in the announcements section
hide_from_announcments: false
---
```

#### Custom Events
Use `_events/` directory to add new custom events, use `type: raw_event`. These events will apear at the schedule page.
```markdown
---
type: raw_event
name: <Event name>
date: 20xx-xx-xxTx:xx:xx+4:30
description: <Event description>

# optional
# if you want to hide time in Schedule, set this to true
hide_time: false

# optional
# set it to true if you don't want this event appear to in the announcements section
hide_from_announcments: false
---
<!-- you can create custom content using markdown. this section will be placed in "Course Materials (in schedule section)" -->
## Hello
this is a custom event with `code`
```


#### Updates/Announcements
All contents here appear in at the home page
Use `_announcements/` directory to create new Announcement
```markdown
---
date: 20xx-xx-xxTx:xx:xx+4:30
---
<put a short announcement here, you can use all markdown features>
```

### Advanced Customization
You can add custom contents to each section (lectures, assignments, schedule, materials, and project)
- Lectures: Edit `lectures.md`
- Assignments: Edit `assignments.md`
- Schedule: Edit `schedule.md`
- Materials: Edit `materials.md`
- Project: Edit `project.md`

Additionally, you can update navigation menus (the menu at the top of the website) by editing `_data/nav.yml`

To add new section, add new navigation menu. Then create a new file in website's root directory using the following template:
```markdown
---
layout: page
title: Page Title
permalink: /page-address/
---
```

## Acknowledgement

Based on website template
https://github.com/kazemnejad/jekyll-course-website-template; used
under the following MIT License:

```
MIT License

Copyright (c) 2017 Steven V. Miller

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
