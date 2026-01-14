---
title: AINoon Tutorial 4
---

The goal of this tutorial is to **vibe code a simple web application**.


## What is vibe coding?

*Refer to **What is vibe coding?** and **What is vibe coding useful for?** slides*


## Vibe coding an app

* Let's say you're responsible for writing a weekly newsletter at your
  company.
* Each newsletter needs an image in a standard shape and size, but
  your coworkers provide you with images of all shapes and sizes.
* To save you time each week, let's build an app that will let you:
  * Upload an image
  * Automatically crop it to the correct dimensions
  * Download the image

1. Open [gemini.google.com](https://gemini.google.com)
2. Give it the following prompt:

```
Build an app that lets me upload an image and crops that image to 200 x 200 and then lets me download it
```

What did that do?

1. It explains to us what it's doing
   * It's going to build a web app that will run in a web browser
   * This is the only kind of app it can run
2. It generates a lot of code
   * This looks quite similar to the web app code we saw before
3. It's running the app for us to try!


## Does it work?

1. Open [technoon.org/ainoon](https://technoon.org/ainoon)
2. Download [cooper.jpg](https://technoon.org/ainoon/lesson_4/cooper.jpg)
   from the **Resources** section
3. Upload `cooper.jpg` into your app
4. Download the image

**AUDIENCE QUESTION:** Did it work?

* I find it often resizes before it crops - sometimes explaining
  that's what it's doing - I can ask it to not do that:
  ```
  Don't resize the image before cropping
  ```


## What has it generated?

* At any time, you can switch to viewing the **Code**
* It's very quickly generated quite a lot of code that would take a
  while to review - even for someone who's familiar with the HTML and
  JavaScript languages it's using!
* We can ask it explain specific parts of the code if we're
  interested:
  1. Scroll to the bottom and highlight an event handler
  2. In the "Ask Gemini" pop-up:
     ```
     What does this code do?
     ```
  3. The explanation may only make sense if you're familiar with
     coding in the JavaScript language.


## Making changes

Ask the agent to make some changes to the app, like:

1. ```
Allow me to select the cropped region of the image
   ```
2. ```
Add the image filename as a watermark to the image
   ```
3. ```
Change the title of the app to "Image Cropper 2000"
   ```

* It's important to make sure key functionality is working after each
  change, as it may change features you were already happy with!
* If you're ever unhappy with a change that it made, you can use the
  **Previous version** and **Next version** buttons


## Adding an AI Feature

With Gemini, we can even add a feature to our app that uses Gemini AI:

```
Add a button to generate a caption for the image using Gemini
```


## Sharing your app

Under the **Share** button, you can:

* Copy the contents of the file
  * You could paste and save that in a `.html` file
  * Then anyone could open that file in a web browser, or you could
    use a hosting service to serve it as a website.
* More conveniently, you can click **Share** again to get a link that
  anyone can use to view the app on Google


## Gotchas

* It's a good idea to test if this will work for other users
* I'm going to open the share link in an **Incognito** window, where I
  won't be logged into my Google account
* Uploading, cropping, and downloading an image works well
* But it fails to generate a caption!
* We can try asking why:
  ```
  Why does the caption generation fail when used by a user who isn't logged into Google?
  ```
* The reason is that it can only make a call to Gemini when the user
  is logged into Google in their browser
  * It may give an incorrect explanation - asserting it should work
    for users who aren't logged into Google!
* Dangerously, the code likely contains `apiKey = ""` that you could
  fill in with an API key
  * But, just like any code in your app, that API key would be visible
    for anyone with access to the app!
* That might not be obvious unless you're familiar with how web apps
  work

This highlights the security risks of releasing apps when you don't
know what the code is actually doing!

The same warning goes for not being sure of the correctness

* Are you confident this app will do the right thing when...
  * Someone uploads a second image?
  * The image is already smaller than 200 x 200?
  * The filename is too long for the watermark?
* Extensive testing is a good idea, but how would you be confident in
  its correctness if the app...
  * Performed a more complex calculation
  * Analysed some data


## Scaling up AI-Assisted Coding

*Refer to **Scaling up AI-Assisted Coding** slide*


## Conclusion

In this tutorial, we've seen how vibe coding is a powerful tool for
**rapid prototyping** and **simple, low-stakes apps**.

However, we've also seen the risks to **security** and **correctness**
if you don't know what the code is *actually* doing.

This recurring theme of **great power** requiring **great
responsibility** is something we've seen multiple times throughout the
course - and is one of the most important ideas to keep in mind as you
learn and use even more AI tools in the future!
