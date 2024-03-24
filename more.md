---
layout: page
title: More about TechNoon
permalink: /more/
---

* [Who We Are](#who-we-are)
* [Resources](#resources)

---

## Who We Are

{% if site.data.people.instructors %}
<div>
    <!-- <h2>Instructors</h2> -->
    <!-- <div class="image--cover-container">
        <img src="{{site.data.people.instructor.profile_pic | prepend: site.baseurl }}" class="image--cover">
        <p>{{site.data.people.instructor.name}}</p>
    </div> -->

    <div class="profile-pic-gallary">
        <div class="instructor-list">
            {% for ins in site.data.people.instructors %}
            <div class="image--cover-container">
                <div class="profile-pic">
                    <img src="{{ins.profile_pic | prepend: site.baseurl }}" class="image--cover">
                    {% if ins.webpage %}
                    <p><a href="{{ ins.webpage }}">{{ins.name}}</a></p>
                    {% else %}
                    <p>{{ins.name}}</p>
                    {% endif %}
                </div>
                <p class="bio">{{ins.bio}}</p>
            </div>
            {% endfor %}
        </div>
    </div>
</div>
{% endif %}

{% if site.data.people.teaching_assistants %}
<div style="width:65%; float: left">
    <div class="profile-pic-gallary ">
        <h2>Teaching Assistants</h2>
        {% for ta in site.data.people.teaching_assistants %}
        <div class="image--cover-container">
            <img src="{{ta.profile_pic | prepend: site.baseurl }}" class="image--cover">
            {% if ta.webpage %}
            <p><a href="{{ ta.webpage }}">{{ta.name}}</a></p>
            {% else %}
            <p>{{ta.name}}</p>
            {% endif %}
        </div>
        {% endfor %}
    </div>
</div>
{% endif  %}

---

## Resources

* [Auckland Tech Hub Challenges – TechNoon Solutions](/static-files/technoon_auckland-tech-hub.pdf){:target="_blank"}{:rel="noopener"}
  * How TechNoon addresses the skills gap of the
    [Auckland Tech Hub](https://aucklandchamber.co.nz/2024/01/25/three-sectors-can-transform-auckland-into-a-global-tech-hub-report/){:target="_blank"}{:rel="noopener"}
    vision
* [What can industry do to benefit from TechNoon?](/static-files/technoon_industry-action.pdf){:target="_blank"}{:rel="noopener"}
  * Shareable slide with practical steps that business can take to benefit from TechNoon.
* [Boosting NZ Digital Skills - Slide Deck](/static-files/technoon_boosting-nz-digital-skills.pdf){:target="_blank"}{:rel="noopener"}
  * Presentation on improving digital skills training in New Zealand -
    ideas that led to the development of TechNoon.
