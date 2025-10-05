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
* WiFi


### Welcome to AINoon!

Hands up if you've ever:

::: incremental

* Used Google's "AI Overview" instead of opening search results?
* Asked ChatGPT a question?
* Used AI to automate a task?
* Used AI to build an app or write code?

:::

<aside class="notes">

* Introduce yourself and your background with AI

</aside>

### Why AINoon?

::: incremental

* **Generative AI is a powerful tool**
  <br>- It unlocks new opportunities for productivity
* **It has limitations we're not used to**
  <br>- Risk of misuse and over-trusting
* **There are many valid concerns**
  <br>- Important to understand risks and issues
* **There's a lot of hype**
  <br>- It's hard to know where to start!

:::

### What we'll cover in AINoon

::: incremental

* **Hands-on practice** with Generative AI
* **Leading applications** of Generative AI
  <br>- Be equipped to spot opportunities
* **Demystifying** how Generative AI works
  <br>- Understand its strengths and limitations
* **Risks and issues** to consider when using AI
* **Providing a forum** for questions and assistance

:::

### What to expect from AINoon

Four lessons, each including:

* **Presentation** on important AI concepts
* **Follow-along tutorial** to get hands-on with AI
* *Optional homework* if you want to go further

Get all the slides, tutorials, and homework from:

[**technoon.org/ainoon**](https://technoon.org/ainoon)

### AINoon Structure

<div style="font-size: 0.8em;">

* **Lesson 1:**
  * *Presentation:* Intro to AI: terminology and business use-cases
  * *Tutorial:* Using a chatbot for business use-cases
* **Lesson 2:**
  * *Presentation:* How AI works
  * *Tutorial:* Building a chatbot on your documents with [Chatbase](https://chatbase.co/)
* **Lesson 3:**
  * *Presentation:* Common patterns: RAG, tools, and agents
  * *Tutorial:* Building an agent with [Zapier](https://zapier.com/)
* **Lesson 4:**
  * *Presentation:* AI risks and challenges
  * *Tutorial:* "Vibe-coding" an app with [Replit](https://replit.com/)

<span style="font-size: 0.7em;">We'll use convenient tools in tutorials, but the focus is on principles that will apply in any tool</span>

<aside class="notes">

* We're leaving AI risks quite late, given I'm sure you'll have a lot
  of questions relating to that.
* However, it will be easier to have a more grounded conversation
  about the risks once we have a shared understanding of:
  * What AI actually is
  * How it works
  * and what it is capable of

</aside>

</div>

### How to get the most out of AINoon

* As much as possible, **don't do emails and work**
  * A lot of the value comes from carefully considering ideas and
    engaging in the conversation
* **Follow along with the tutorials**
  * Even if you've used a tool before, look at the results in light of
    the ideas we're discussing

### Questions?


### Intro to AI

* Establish a common vocabulary
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
<li>E.g. Recognising objects in images, topic-labelling of text</li>
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

* **Drafting** emails and documents
* **Summarising** documents and meetings
* **Brainstorming** a wide variety of ideas
* **Personalised tutoring** for learning new subjects
* **Generating code** to assist programmers
* **Data extraction and transformation**
  * Turn unstructured text and images into structured data
  * E.g. Identify which team an IT ticket should go to
* **Custom agents**: chatbots that retrieve info and take action
  * Answering questions from organisation knowledge bases
  * Personalised customer service
  * Automated handling of events - e.g. IT tickets

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
<ul>
<li>E.g. Llama (Meta), gpt-oss (OpenAI), DeepSeek</li>
<li>Most require specialised hardware, but less powerful chatbots can run on a laptop</li>
<li>Check whether licenses allow commercial use</li>
</ul>
</li>
</ul>

</div>

### Tutorial Objectives

1. Using a chatbot for business use cases:
   * Brainstorming and drafting
   * Automating web searches
   * Summarising documents
2. Identifying important issues to keep in mind
3. Tips for effective prompting


### Tips for crafting better prompts

<div style="font-size: 0.9em;">

::: incremental

* Each prompt should request **one thing**
* Start prompts with a **persona**
  * E.g. "You are an expert in project management..."
* Ask it to "explain **step-by-step**"
  * Can get better answers to more complex questions
* When it's not doing what you want, **be more specific**
  * Though it won't always follow instructions exactly!
* **Seek more tips** online for specific use-cases
  * It's all art/craft, not science/engineering
  * Advice will likely change as models change

:::

</div>

### The Golden Rule of AI

> Don't trust the output of an AI unless you can verify it

* **Bad:** Summarising a document you *haven't* read
* **Good:** Summarising a document you *have* read
* **But:** For some use cases, speed may be more important than accuracy

### Homework

<div style="font-size: 0.75em;">

**Remember:** Don't use private data with public models!

* **Practice prompting**
  * Describe a photo with text to prompt ChatGPT to replicate it
  * Keep refining your prompt to more closely match the photo
* **Generate a video** with Google's [Flow](https://labs.google/fx/tools/flow)
  * Look at the gallery on
    [Midjourney](https://www.midjourney.com/explore) - note the detail
    in the prompts
* **Generate speech from text** with [ElevenLabs](https://elevenlabs.io/)

</div>
