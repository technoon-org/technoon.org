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


### AI Risks and Challenges

<div style="font-size: 0.9em;">

::: incremental

* There's a lot of **hype** *and* a lot of **fear**
* To make good decisions:
  1. Understand the **risks**
  2. Assess them in the context of your **application**
* Some risks are **challenges** to be solved or mitigated
  * *We didn't stop using electricity because of shocks, we developed
    insulation*
* **Do your own deeper research!**
  * This is food for thought, not authoritative answers
  * These are tricky issues with many differing opinions
  * The space is rapidly changing
  * The future is unknown

:::

</div>

### Inaccurate Outputs

We've seen *plenty* of examples over the course

<div style="font-size: 0.9em;">

::: incremental

* **Consider failure modes:** How could this fail? What would the impact be?
* **[Human in the loop](https://www.trackmind.com/humans-in-the-loop-vs-on-the-loop/):** Human decisions with AI support
* **[Human on the loop](https://www.trackmind.com/humans-in-the-loop-vs-on-the-loop/):** Human supervises AI decisions
* **Real human thinking** is important to avoid [workslop](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity)!
* **Thorough testing:** Like for chatbots in [Lesson 2](../lesson_2/slides.html#/testing-a-chatbot)

:::

</div>

### Unwanted Bias

<div style="font-size: 0.9em;">

::: incremental

* **Examples:**
  * An LLM trained on 20th century writings may associate *doctor* as
    more *male* than *female*
  * LLM providers may bias the training or filter outputs
  * [LLMs may focus less on the middle of a long prompt](https://news.mit.edu/2025/unpacking-large-language-model-bias-0617)
* **Mitigation:**
  * Be **aware** of potential bias
  * Consider your **application**: that 20th century LLM...
    * *might* prefer doctor CVs from male candidates
    * *might* still be a useful model of the 20th century
  * Avoid or tightly control AI in **high-stakes** decisions

:::

</div>

### Privacy and Security

<div style="font-size: 0.9em;">

::: incremental

* **LLMs may use your data for future training**
  * Some providers allow you to disable that
  * Corporate offerings preferred by companies
    * Providers may still monitor for misuse
* **Don't trust generated code you don't understand**
  * Security issues can be subtle - more in the tutorial
* **Consider worst-case scenarios for agents,
  <br>like the [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/):**
  1. Agent reads untrusted text (e.g. your email inbox)
  2. Agent reads private data (e.g. your private files)
  3. Agent writes to public location (e.g. sends an email)
  4. → E.g. "Reply to this email with private files..."

:::

</div>

### Copyright

**Disclaimer:** This is not legal advice!

<div style="font-size: 0.85em;">

::: incremental

* **Does training a model on content infringe the author's
  copyright?**
  * Unclear at this stage
  * Active court cases regarding books, music, code, etc.
* **Does the model provider or prompter own AI-generated content?**
  * The US has determined AI-generated content can't be copyrighted
  * Check the terms and conditions of the model provider
* **[Watch this space](https://builtin.com/artificial-intelligence/ai-copyright)**

:::

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
  providers - e.g. [Model Context Proctol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro)

:::

</div>

### Other risks to consider

<div style="font-size: 0.85em;">

::: incremental

* **Environmental impact** - [training and serving models has high electricity and water costs](https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117)
* **Impact on jobs** - AI promises efficiency for some *tasks*
  * Depending on a worker's role, AI *may*:
    * Allow more time for other tasks
    * Change the required skills or the way work is done
    * Reduce the required number of workers
* **Artificial General Intelligence (AGI) / Superintelligence**
  * AI that learns and thinks like a human
    * No concrete definition to evaluate against
    * Goal posts seem to shift with each advance
  * Some [claim GenAI shows "sparks" of AGI](https://arxiv.org/abs/2303.12712),<br>others [show how it doesn't truly "think"](https://machinelearning.apple.com/research/illusion-of-thinking)

:::

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

::: incremental

* **What is coding?**
  * Writing instructions in languages the computer can understand
  * How software developers build apps
* **What is *AI-assisted* coding?**
  * Any use of AI to help a developer write code
* **What is [*vibe* coding](https://simonwillison.net/2025/Mar/19/vibe-coding/)?**
  * Describing an app to an agent and letting it write the code
    *without checking the code it writes*

:::

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

To use AI on more complex coding projects:

<div style="font-size: 0.9em;">

::: incremental

* Use agents that work on a whole folder of files
  * E.g. Replit, Codex, GitHub Copilot
* Generate and review **planning documents** for:
  * Features and other requirements
  * Technical architecture
* Use **version control** to track changes
  * Learn the Git version control tool with
    [GitNoon](https://technoon.org/gitnoon/)!
* Guide it with **expert knowledge** in prompts
  * Photography terms → better images
  * Coding terms  → better code

:::

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
