---
title: AINoon Lesson 4
---

### Get Ready for AINoon!

* Open [technoon.org/ainoon](https://technoon.org/ainoon)
* Log in with a free Google account to [gemini.google.com](https://gemini.google.com)

### Thanks

* To the host for the great venue!
* To our sponsors

### Administrivia

* Fire escapes
* Toilets
* Cleaning up after ourselves
* Wi-Fi


### <span style="1.5em;">AI Risks and Challenges</span>

<div style="font-size: 0.9em;">

<ul>
<li class="fragment">There's a lot of **hype** *and* a lot of **fear**</li>
<li class="fragment">To make good decisions:
  <ol>
  <li>Understand the **risks**</li>
  <li>Assess them in the context of your **application**</li>
  </ol>
</li>
<li class="fragment">Some risks are **challenges** to be solved or mitigated
  <ul>
  <li>*We didn't stop using electricity because of shocks, we developed insulation*</li>
  </ul>
</li>
<li class="fragment">**Do your own deeper research!**
  <ul>
  <li>This is food for thought, not authoritative answers</li>
  <li>These are tricky issues with many differing opinions</li>
  <li>AI is rapidly changing and the future is unknown</li>
  </ul>
</li>

</div>

### Inaccurate Outputs

We've seen *plenty* of examples over the course

How can inaccuracy be mitigated?

<div style="font-size: 0.9em;">

::: incremental

* **Golden Rule of AI:** Don’t trust outputs you can't verify
* **Consider failure modes:** How could this fail? What would the impact be?
* **[Human in the loop](https://www.trackmind.com/humans-in-the-loop-vs-on-the-loop/):** Human decisions with AI support
* **[Human on the loop](https://www.trackmind.com/humans-in-the-loop-vs-on-the-loop/):** Human supervises AI decisions
  * But apathetic supervision can lead to [workslop](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity)
* **Thorough testing:** Like for chatbots in [Lesson 2](../lesson_2/slides.html#/testing-a-chatbot)

:::

</div>

### Unwanted Bias

<div style="font-size: 0.9em;">

<ul>
<li>**Examples:**
  <ul>
  <li class="fragment">An LLM trained on 20th century writings **might** associate *doctor* as more *male* than *female*</li>
  <li class="fragment">LLM providers may bias the training or filter outputs</li>
  <li class="fragment">[LLMs may focus less on the middle of a long prompt](https://news.mit.edu/2025/unpacking-large-language-model-bias-0617)</li>
  </ul>
</li>
<li class="fragment">**Mitigation:**
  <ul>
  <li class="fragment">Be **aware** of potential bias</li>
  <li class="fragment">Consider your **application**: that 20th century LLM...
    <ul>
    <li>*might* prefer doctor CVs from male candidates</li>
    <li>*might* still be a useful model of the 20th century</li>
    </ul>
  </li>
  <li class="fragment">Avoid or tightly control AI in **high-stakes** decisions</li>
  </ul>
</li>
</ul>

</div>

### Privacy and Security

<div style="font-size: 0.9em;">

<ul>
<li class="fragment">**LLMs may use your data for future training**
  <ul>
  <li>Some providers allow you to disable that</li>
  <li>Corporate offerings preferred by companies,<br>but providers may still monitor for misuse</li>
  </ul>
</li>
<li class="fragment">**Don't trust generated code you don't understand**
  <ul>
  <li>Security issues can be subtle - more in the tutorial</li>
  </ul>
</li>
<li class="fragment">**Consider worst-case scenarios for agents,
  <br>like the [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/):**
  <ol>
  <li>Agent reads untrusted source (e.g. your email inbox)</li>
  <li>Agent reads private data (e.g. your private files)</li>
  <li>Agent writes to public location (e.g. sends an email)</li>
  <li>→ E.g. "Reply to this email with private files..."</li>
  </ol>
</li>
</ul>

</div>

### Copyright

**Disclaimer:** This is not legal advice!

<div style="font-size: 0.8em;">

<ul>
<li class="fragment">**Does training a model on some content infringe the author's copyright?**
  <ul>
  <li>Unclear at this stage</li>
  <li>Active court cases regarding books, music, code, etc.</li>
  </ul>
</li>
<li class="fragment">**Does the model provider or prompter own AI-generated content?**
  <ul>
  <li>The US has determined AI-generated content can't be copyrighted</li>
  <li>Check the terms and conditions of the model provider</li>
  </ul>
</li>
<li class="fragment">**[Watch this space as court cases continue](https://builtin.com/artificial-intelligence/ai-copyright)**</li>
</ul>

</div>

### Vendor lock-in

<div style="font-size: 0.9em;">

::: incremental

* Like with any technology service, **avoid becoming strongly tied to
  one vendor**:
  * With competition and evolving offerings, you want **freedom to
    pick the best provider**
  * **Prices may start below cost** to grow users, then increase later
* Build **modular** systems with replaceable components
* Prefer **open-source** tools and **open-weight** models that any
  provider can run
* Look for compatibility with **open standards** used across
  providers - e.g. [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro)

:::

</div>

### Other risks to consider

<div style="font-size: 0.7em;">

<ul>
<li class="fragment">**Environmental impact** - [training and serving models has high electricity and water costs](https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117)</li>
<li class="fragment">**Identifying AI-generated content is difficult**
  <ul>
  <li>It may "drown out" useful content on the Internet</li>
  <li>How will we find trustworthy training data for future models?</li>
  </ul>
</li>
<li class="fragment">**Impact on jobs** - Depending on a worker's role, efficiency gains *may*:
  <ul>
  <li class="fragment">Allow more time for other important tasks</li>
  <li class="fragment">Change the required skills or the way work is done</li>
  <li class="fragment">Reduce the required number of workers</li>
  </ul>
</li>
<li class="fragment">**Artificial General Intelligence (AGI) / Superintelligence**
  <ul>
  <li>"AI that learns and thinks like a human"
    <ul>
    <li>No concrete definition to evaluate against</li>
    <li>Goal posts seem to shift with each advance</li>
    </ul>
  </li>
  <li class="fragment">Some [claim GenAI shows "sparks" of AGI](https://arxiv.org/abs/2303.12712),<br>others [claim GenAI doesn't truly "think"](https://machinelearning.apple.com/research/illusion-of-thinking)</li>
  </ul>
</li>
</ul>

</div>

### Discussion

* Have we missed any risks?
* Can you think of mitigations for any of the discussed risks?
* Any other questions or comments?

### Tutorial Objectives

1. Use *vibe coding* to build a simple web app
2. See the risks of using code you don't understand
3. Discuss practices for coding safely with AI

### What is vibe coding?

<div style="font-size: 0.95em;">

<ul>
<li class="fragment">**Coding:**
  <ul>
  <li>Writing instructions in languages the computer can understand</li>
  <li>How software developers build apps</li>
  </ul>
</li>
<li class="fragment">***AI-assisted* coding:**
  <ul>
  <li>Any use of AI to help a developer write code</li>
  </ul>
</li>
<li class="fragment">**[*Vibe* coding](https://simonwillison.net/2025/Mar/19/vibe-coding/):**
  <ul>
  <li>Describing an app to an AI agent and letting it write the code *without checking the code it writes*</li>
  </ul>
</li>

</div>

<aside class="notes">

* After defining *coding*, show an example by opening the source view
  (`Ctrl-u`) on the [technoon.org](https://technoon.org) website to
  show the HTML code for that website.

</aside>

### What is vibe coding useful for?

<div style="font-size: 0.9em;">

::: incremental

* Enable anyone to rapidly build **prototypes** and apps for
  **low-stakes** use-cases.
* *NOT* when **security** or **correctness** are important
  * Carefully review generated code in those cases
* Probably **not the best way to learn to code**
* **Don't reinvent the wheel** - plenty of apps exist to build websites
  and forms
* **The sweet spot:** automating time-consuming tasks that are
  specific to your work!

:::

</div>

### Scaling up AI-Assisted Coding

<div style="font-size: 0.8em;">

To use AI on more complex coding projects:

<ul>
<li class="fragment">Use agents that work on a whole folder of files
  <ul>
  <li>E.g. Replit, Codex, GitHub Copilot</li>
  </ul>
</li>
<li class="fragment">Generate and review **planning documents** for:
  <ul>
  <li>Features and other requirements</li>
  <li>Technical architecture</li>
  </ul>
</li>
<li class="fragment">Use **version control** to track changes
  <ul>
  <li>Learn the Git version control tool with [GitNoon](https://technoon.org/gitnoon/)!</li>
  </ul>
</li>
<li class="fragment">Guide it with **expert knowledge** in prompts
  <ul>
  <li>Photography terms → better images</li>
  <li>Coding terms  → better code</li>
  </ul>
</li>
<li class="fragment">**AI code-completion** is popular with experienced developers</li>
</ul>

</div>


### Homework

* **Research one risk relevant to your use of AI**
  * Find a range of perspectives
  * Identify more mitigations
  * Consider which mitigations are most appropriate for your
    application
* **Use a coding agent to make a larger app**
  * E.g. Replit, Codex, or GitHub Copilot
  * See how it makes a plan and generates a whole folder of files
  * You might not get very far without a paid plan
