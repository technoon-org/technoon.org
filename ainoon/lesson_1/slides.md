---
title: AINoon Lesson 1
---

### Get Ready for AINoon!

* Open [technoon.org/ainoon](https://technoon.org/ainoon)
* Log in with a free account to [chatgpt.com](https://chatgpt.com)

### Thanks

* To the host for the great venue!
* To our sponsors

### Administrivia

* Fire escapes
* Toilets
* Cleaning up after ourselves
* Wi-Fi


### <span style="font-size: 2em;">Welcome to AINoon!</span>

<aside class="notes">

* *Introduce yourself and your background with AI*

</aside>

### Hands up if you've ever:

::: incremental

* Used Google's "AI Overview" instead of opening search results?
* Asked ChatGPT a question?
* Used AI to automate a task?
* Used AI to build an app or write code?

:::

### What we'll cover in AINoon

::: incremental

* **Leading applications** of Generative AI
  <br>- Spot opportunities to increase productivity
* **Hands-on practice** in follow-along tutorials
* **Demystifying** how Generative AI works
  <br>- Understand strengths and limitations
* **Risks and issues** to consider when using AI
* **Providing a forum** for questions and assistance

:::

### How to get the most out of AINoon

::: incremental

* As much as possible, **don't do emails and work**
* **Follow along with the tutorials**
  * We have a mix of experience levels
  * If you've used a tool before, consider the results in
    the context of ideas we're discussing
  * You might still learn a new tip or trick!

:::

### AINoon Structure

<div style="font-size: 0.7em;">

* **Lesson 1:**
  * *Presentation:* Terminology and business use-cases
  * *Tutorial:* Chatbots for business
* **Lesson 2:**
  * *Presentation:* How AI works
  * *Tutorial:* Build a chatbot on your documents with [Chatbase](https://chatbase.co/)
* **Lesson 3:**
  * *Presentation:* Common patterns: RAG, tools, and agents
  * *Tutorial:* Build an agent with [Zapier](https://zapier.com/)
* **Lesson 4:**
  * *Presentation:* AI risks and challenges
  * *Tutorial:* "Vibe-coding" an app with [Gemini](https://gemini.google.com/)

All slides, tutorials, and optional homework on [**technoon.org/ainoon**](https://technoon.org/ainoon)

<aside class="notes">

* Each lesson includes a presentation and a follow-along tutorial
* We'll use convenient tools in tutorials, but the focus is on
  principles that will apply in any tool
* We're leaving AI risks quite late, given I'm sure you'll have a lot
  of questions relating to that
* However, it will be easier to have a more grounded conversation
  about the risks once we have a shared understanding of:
  * What AI actually is
  * How it works
  * and what it is capable of

</aside>

</div>

### <span style="font-size: 2em;">Questions?</span>


### <span style="font-size: 1.5em;">Intro to Generative AI</span>

* Establishing a common vocabulary
* Who's who in the zoo: companies and services
* How generative AI is being used by businesses

### AI Terminology

<style>
.venn {
    border: 5px solid black;
    text-align: left;
    padding: 10px 0 0 10px;
}
.venn h4 {
    font-size: 0.7em;
    margin-bottom: 0px;
}
.venn ul {
    font-size: 0.6em;
    margin-top: 0px;
    margin-bottom: 0px;
}
.venn .venn {
    margin-top: 10px;
    margin-left: 50px;
    border-bottom: none;
    border-right: none;
}
</style>
<div class="venn">
<h4>Artificial Intelligence (AI) ~1950s</h4>
<ul>
<li>General term for computers making "intelligent" decisions</li>
<li>E.g. Hand-crafted programs that can play checkers</li>
</ul>
<div class="venn fragment">
<h4>Machine Learning (ML) ~1980s</h4>
<ul>
<li>Approach to AI where computers "learn" from patterns in data</li>
<li>E.g. Learning from many past emails to identify spam</li>
</ul>
<div class="venn fragment">
<h4>Deep Learning (DL) ~2000s</h4>
<ul>
<li>Approach to ML based on very large (artificial) "neural networks"</li>
<li>E.g. Recognising objects in images, text translation</li>
</ul>
<div class="venn fragment">
<h4>Generative AI (GenAI) ~2020s</h4>
<ul>
<li>Application of DL to generate text, images, audio, video, etc.</li>
<li>What most people mean by "AI" these days</li>
<li class="fragment"><strong>The focus of this course</strong></li>
</ul>
</div>
</div>
</div>
</div>
<p style="font-size: 0.4em;">Source: <a href="https://blogs.nvidia.com/blog/whats-difference-artificial-intelligence-machine-learning-deep-learning-ai/">blogs.nvidia.com/blog/whats-difference-artificial-intelligence-machine-learning-deep-learning-ai/</a></p>

<aside class="notes">

* Except where noted, "AI" will refer to "Generative AI" in this course

</aside>

### Chatbots are the most prominent application of GenAI

* ChatGPT (OpenAI)
* Claude (Anthropic)
* Gemini (Google)
* Microsoft Copilot (based on OpenAI tech)
* Grok (X)
* DeepSeek

<aside class="notes">

* Ask the audience if they can name any others?

</aside>

### What can chatbots do for business?

<div style="font-size: 0.8em;">

<ul>
<li>**Drafting** emails and documents</li>
<li>**Summarising** documents and meetings</li>
<li>**Brainstorming** a wide variety of ideas</li>
<li class="fragment">**Generating code** to assist programmers</li>
<li class="fragment">**Data extraction and transformation**
  <ul>
  <li>Turn unstructured text and images into structured data</li>
  <li>E.g. Identify which team an IT ticket should go to</li>
  </ul>
</li>
<li class="fragment">**Custom agents**: chatbots that retrieve info and take action
  <ul>
  <li>Answering questions from organisation knowledge bases</li>
  <li>Personalised customer service</li>
  <li>Automated handling of events - e.g. IT tickets</li>
  </ul>
</li>
</ul>


</div>

### Using chatbots for business

<div style="font-size: 0.9em;">

<ul>
<li class="fragment">
**Public chatbots** train future chatbots with your data
</li>
<li class="fragment">
Companies deploy **internal chatbots** to protect data
<ul>
<li>Often using business-to-business service offerings</li>
<li>E.g. From Microsoft, Amazon, or Google clouds</li>
</ul>
</li>
<li class="fragment">
You can run ***open* chatbots** on your own computers
<!--
<ul>
<li>E.g. Llama (Meta), gpt-oss (OpenAI), DeepSeek</li>
<li>Most require specialised hardware, but less powerful chatbots can run on a laptop</li>
<li>Check whether licenses allow commercial use</li>
</ul>
-->
</li>
</ul>

</div>

### Tutorial Objectives

1. Using a chatbot for business use cases:
   * Brainstorming and drafting
   * Automating web searches
   * Summarising documents
2. Common accuracy issues to be aware of
3. Tips for effective prompting


### Tips for crafting better prompts

<div style="font-size: 0.9em;">

::: incremental

* Each prompt should request **one thing**
* Start prompts with a **persona**
  <br>- E.g. "You are an expert in project management..."
* Ask it to "explain **step-by-step**"
  <br>- Can get better answers to more complex questions
* When it's not doing what you want, **be more specific**
  <br>- Though it won't always follow instructions exactly!
* **Seek more tips** online for specific use-cases
  <br>- It's all art/craft, not science/engineering
  <br>- Advice will likely change as chatbots change

:::

</div>

### The Golden Rule of AI

> Don't trust the output of an AI unless you can verify it

* **Bad:** Summarising a document you *haven't* read
* **Good:** Summarising a document you *have* read
* **But:** For some use cases, speed may be more important than accuracy

### Homework

<div style="font-size: 0.75em;">

**Remember:** Don't use private data with public services!

* **Generate a video** with Google's [Flow](https://labs.google/fx/tools/flow)
  * Look at the gallery on
    [Midjourney](https://www.midjourney.com/explore) - note the detail
    in the prompts
* **Practice prompting** with the [Say What You See](https://artsandculture.google.com/experiment/say-what-you-see/jwG3m7wQShZngw) game
  * Write a prompt to replicate a provided picture
  * Keep refining your prompts to more closely match the pictures
* **Generate speech from text** with [ElevenLabs](https://elevenlabs.io/)

</div>
