---
title: AINoon Lesson 2
---

### Thanks

* To the host for the great venue!
* To our sponsors

### Administrivia

* Fire escapes
* Toilets
* Cleaning up after ourselves
* WiFi

### Demystifying AI

How generative AI works and how that informs how to best use it

### How does a chatbot generate text?

<style>
.neural-network-diagram > p {
    display: grid;
}
.neural-network-diagram img {
    margin: 0;
    grid-area: 1 / 1;
    background: white;
}
</style>
<div class="r-stack neural-network-diagram">
<img src="assets/neural-network-1.png">
<img src="assets/neural-network-2.png" class="fragment">
<img src="assets/neural-network-3.png" class="fragment">
<img src="assets/neural-network-4.png" class="fragment">
<img src="assets/neural-network-5.png" class="fragment">
<img src="assets/neural-network-6.png" class="fragment">
<img src="assets/neural-network.png" class="fragment">
</div>

<aside class="notes">

<div style="font-size: 0.9em;">

* The chatbot predicts what text comes next, one word at a time
* The prompt is split into tokens (words or parts of words)
  * Image and audio inputs can similarly be split into chunks to act as tokens
* Tokens passed into an LLM, with each token represented as a number
* Those numbers are processed by layers of "neurons"
* The final layer outputs a number for each possible token representing the probability that token comes next
* A token is randomly picked based on those probabilities
  * Some chatbots let you choose a temperature - a lower temperature is less random
  * i.e. The highest probability is more likely to be picked with a lower temperature
* The chosen token is added to the prompt, and the whole process is repeated to get the next token
* Each neuron multiplies each input by a weight, sum the result, and applies a transformation to produce a single output number
  * Loosely inspired by a neuron in the brain
* Millions of neurons are connected in a special pattern called a "transformer"
  * The transformer architecture was the breakthrough that led to ChatGPT
  * When someone says "OpenAI's GPT-3 has 175 billion parameters", they're counting the weights
  * Models keep getting bigger, which lets them more accurately predict which token comes next

</div>

</aside>

### Where do LLM weights come from?

<div style="font-size: 0.85em;">

::: incremental

* Weights start as random numbers
* Weights are updated by a process called **pre-training**:
  * Uses millions of *training examples* from **general sources**,
    like the internet and books
  * E.g. Leave-one-word-out examples:
    <br><span style="font-size: 0.9em;">`The Beatles were a ____ from England` → `band`</span>
  * For each example, weights are updated *slightly* to get closer to
    the right answer - like tuning a dial
  * This trains the LLM in **language patterns** AND **general knowledge**
* Extra training based on **human feedback** makes chatbots respond
  better to **questions** and **instructions**
  * E.g. Chatbot gives 5 answers and human picks the best

:::

</div>

### You now understand what GPT stands for!

<table>
<tr><td><strong>Generative</strong></td><td>The model generates text (or other content)</td></tr>
<tr><td><strong>Pre-trained</strong></td><td>Pre-trained on many examples from general sources</td></tr>
<tr><td><strong>Transformer</strong></td><td>The kind of neural network architecture used</td></tr>
</table>

<div style="font-size: 0.78em;">

### What does this teach us about using GenAI?

::: incremental

* The generation process is **not magic, just simple maths!**
* We know *how* AI works, but **no-one truly knows *why* it works**
  * The billions of calculations across neurons are too complex
* **AI doesn't "think" with logic** - it's predicting the best answer
  based on its training sources
  * People say AI *sometimes* "hallucinates" wrong answers - but every
    response is generated the same way
  * It generates answers that *sound* right - and it's surprising so
    many actually are right!
* **It doesn't train during your chats**
  * It "remembers" by including chat history in the prompt
  * Even "memory" features just include past chats in the prompt
  * Public chatbots may use your chats to train later models

:::

</div>

### GenAI Strengths and Limitations

<div style="text-align: left; font-size: 0.8em;">

#### Key Strengths

* Generates text that looks similar to what a human would write
* Reads lots of text really fast
* Surprisingly good responses to a wide variety of tasks

<div style="margin-top: 0.5em;"></div>

#### Key Limitations

* Everything is a hallucination - but it's correct surprisingly often
* It might not always "pay attention" to everything in the prompt
* It might not consistently give the same answer
* Different models (or model versions) can give very different
  responses to the same prompt

</div>


### Tutorial Objectives

TODO


### Homework

* TODO
* To learn more about how LLMs work, watch these videos from
  3Blue1Brown:
  * [Brief explainer](https://www.youtube.com/watch?v=LPZh9BOjkQs)
  * [Deeper dive (more maths)](https://www.youtube.com/watch?v=wjZofJX0v4M)
