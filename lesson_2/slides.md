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

TODO

* Training
* Data sources: internet, books, images
* Pre-training + human feedback
* Algorithm

### What does this teach us about how to use GenAI?

TODO

* It's not magic, just simple maths
* We know *how* it works, but we don't really know *why* it works
* It doesn't learn during your chats - "memory" is just context (which
  can sometimes end up confusing it)

### GenAI Strengths and Limitations

TODO

* Strengths
  * Generates text that looks similar to what a human would write
  * Reads lots of text really fast
  * Surprisingly good responses to a wide variety of tasks
* Limitations
  * Everything is a hallucination - but it's correct surprisingly often
  * It might not "pay attention" to the full context
  * It might not consistently give the same answer
  * Different versions of the same model might give very different
    responses to the same prompt

### Tips for using GenAI

TODO

* Golden rule: Don't trust a response if you can't verify it
  * Example: meeting and document summarisation - where you
    attended/read yourself vs didn't
* Use it to *help* you learn things by providing personalised
  explanations and answers to questions
  * Use references to verify
* Prompt crafting guidelines
  * "answer step-by-step"


### Tutorial Objectives

TODO


### Homework

* TODO
* See 3Blue1Brown: https://www.youtube.com/watch?v=wjZofJX0v4M
