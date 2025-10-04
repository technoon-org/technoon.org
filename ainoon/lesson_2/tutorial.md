---
title: AINoon Tutorial 2
---

The goal of this tutorial is to **make your own chatbot to answer
questions based on information in a document.**

* Chatbots can answer "general knowledge" questions based on
  information in the text they were trained on
* But we often want them to be able to answer questions about
  domain-specific or company knowledge sources, like:
  * Frequently asked questions and other help documents
  * Instruction manuals
  * Past problems and resolutions from issue tracking systems

We're going to make a chatbot that can answer questions about TechNoon
courses, like AINoon.


## Create a chatbot

1. Open [chatbase.co](https://chatbase.co)
2. Go to the **Dashboard**
3. Click **New AI agent**
   * If you already have one, select **Create agent** from the agent
     list dropdown.
3. *If it forces you to upload a source:*
   * We're going to skip uploading files for now
   * Select **Text** from the sidebar, and fill in:
     * Title: `TechNoon`
     * Text: `TechNoon delivers free lunchtime industry training courses.`
     * Click **Add text snippet**
4. Select **Create agent**
   * Note that it tells us the total size of our sources compared to
     the limit - we won't be getting anywhere near that limit today.


## Playground and settings

* You should now be on the **Playground** for your agent.
* Let's ask a simple question about TechNoon:

```
What is TechNoon?
```

> It will only give a good answer if you provided the **Text** source
> above.

Now let's look at the options we have to configure our chatbot:

* We can choose what **Model** it uses
  * Lot's of options from different providers
  * You can see a brief description of each model
  * Some are only available for a paid account
* We can set the **temperature**
  * With a higher temperature, you will get more variety in the
    results - which you may or may not want
  * Note that Chatbase may re-use answers to questions your chatbot
    has been asked previously
  * We'll leave it at zero for our informative chatbot.
* We can customise the **Instructions** to the chatbot:
  * Every time a message is sent to the chatbot, the instructions will
    be included in the prompt to the underlying model.
  * You can choose from
    * e.g. "Customer Service Agent"
  * Or write your own! Include instructions like:
    * Some services might refer to these as a **role** or **persona**
    * The chatbot's goal - "Encourage the user to attend TechNoon"
    * Style - professional, relaxed, or a pirate :)
    * Specific instructions
      * E.g. Link the user to the TechNoon website
      * "Dos" have been found to work better than "don'ts"
    * **Remember:** The user can potentially get the chatbot to reveal
      any details in the prompt, so treat it like a public document.


## Providing more knowledge

What if we ask it for information about TechNoon it doesn't have the
answer for?

```
List the available TechNoon courses
```

Let's give it more detailed knowledge!

1. In a new tab, open [technoon.org/ainoon](https://technoon.org/ainoon)
2. Download the [`technoon_knowledge.txt`](https://technoon.org/ainoon/lesson_2/technoon_knowledge.txt)
   * Or share it with everyone in chat.
3. Open the file and have a quick read
   * It contains lots of information about TechNoon courses
4. From Chatbase, open **Sources -> Files** from the sidebar
5. Click the big **Upload** button and select the txt file.
   * Remember, any file you upload can be seen by the service
     provider, or information from it extracted by users asking
     questions of the chatbot
   * Check with your organisation before uploading any private files
6. After uploading, click **Retrain agent**
   * It's not *really* training the chatbot, it's just preparing the
     file for the chatbot to use.
7. After it's finished "training", go back to the **Playground**
8. Ask it the question again:

```
List the available TechNoon courses
```

**But how is it using the file?**

1. Every time a question is asked, it searches through the file for
   chunks that are relevant to the question
   * A bit like a Google search
2. Those chunks are added to the prompt so that the LLM can use them
   to answer the question!
   * You can click on **Sources** below the chatbot to see the chunks
     it used - some might be quite large!

This is a technique called **Retrieval Augmented Generation** or
**RAG** which we'll talk more about next week.


## Deploying your chatbot

Let's share our chatbot with the world!

1. First, let's give the chatbot a better name
   1. Open **Settings -> General** from the sidebar
   2. Change the name to **TechNoon Bot**
      * We should make it clear to our users that this isn't a human
        they're chatting with.
2. Open **Deploy** from the sidebar
   * Lots of options for places we could deploy it
3. Select **Help Page**
   * This will let us serve the chatbot on a web page
   * There are lots of options to customise how the page looks
   * We'll keep the defaults
4. Select **Deploy**
5. Open the **Domain setup** tab, and click **Visit Page**
6. Try asking a question!
   ```
   What can you help me with?
   ```
7. You can now share the link to this page with anyone in the world!
   * This means the information in your instructions and sources is
     publicly accessible!


## Testing

It's important to test chatbots **for their intended use case**.

*Refer to the **Testing a Chatbot** slide*


## Conclusion

You've successfully built a chatbot that can answer questions about
your own documents!

This is a great example of a pattern for using LLMs to build apps that
extend their capabilities.

Next week we're going to look more at **Retrieval Augmented
Generation** and other patterns for building applications with LLMs.
