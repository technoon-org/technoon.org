---
title: GitNoon Lesson 1
---

### Get Ready for GitNoon!

1. Install `git` if you haven't already: https://git-scm.com/downloads
   * On Windows, choose `Git Bash` when installing
2. Open a terminal (or `Git Bash` on Windows)
3. Make sure you can run the `git` command
4. You should see usage instructions for `git`

### Thanks

* To the host for the great venue!
* To our sponsors

### Administrivia

* Fire escapes
* Toilets
* Cleaning up after ourselves
* WiFi

### Lunch Talk: Intro to Git

* What is Git?
* Why use Git?
* When should I use Git?
* What are GitHub, GitLab, etc?
* What to expect from GitNoon

### What is Git?

::: incremental

* Git is a tool to record **versions** of files over time
* Git works with **any type of file**
  * Works *especially well* with **plain-text** like source-code and config
* The most popular Version Control System (VCS)
  * [About **90%** of devs use Git for version control](https://stackoverflow.blog/2023/01/09/beyond-git-the-other-version-control-systems-developers-use/)

:::

### Why use Git?

::: incremental

1. **Backup every version of your files**
   * Being able to *restore any previous version* gives you confidence
     to make radical changes
2. **Seamlessly collaborate with others**
   * Everyone can *work on the same files at the same time*, then
     combine their changes later
3. **Explore file history**
   * Every version in Git records the author, date, and change
     description
   * Find *who* made a change, *when*, and *why*

:::

### What about GitHub, GitLab, BitBucket, etc?

<div style="font-size: 0.8em;">

* Online services for **hosting/sharing Git repositories**
  * Many can be self-hosted in your corporate environment
  * GitLab even has an open-source version

::: incremental

* Provide features for:
  * **Change Control**
    * *Merge/Pull requests* with discussions and approvals
  * **Continuous Integration/Delivery (CI/CD)**
    * Automated checks and tests, deploying code
  * **Static web hosting**
    * Turn a Git repository into a website - great for docs!
  * **And more**
    * Issues, security scanning, container registries

:::

</div>

### What to expect from GitNoon

::: incremental

* Each lesson will have:
  * A **15 minute presentation**
  * A **30 minute hands-on tutorial**
* We'll use Git from the **command-line** / **terminal**
  * The fundamentals you'll learn apply to any GUI
  * A GUI is not always available (e.g. on a server)
  * No previous command-line experience required
* We'll focus on **Git itself**
  * Less on specific features of services like GitHub

:::

### Structure of this Course

<div style="font-size: 0.7em;">

| Lesson | Presentation             | Tutorial                         |
|--------|--------------------------|----------------------------------|
| **1**  | Intro to Git             | Tracking changes in Git          |
| **2**  | Exploring History        | Working with remote repositories |
| **3**  | Collaboration Strategies | Branching and merging            |
| **4**  | Rewriting History        | Rebasing your branch             |

</div>

### Tutorial Objectives

1. Configure Git on your machine
2. Create your first Git repository (aka repo)
3. Track changes to some files

### Independent Work/Homework

<div style="font-size: 0.75em;">

1. **Set a daily reminder to commit a journal entry**
   * Build up your Git muscle memory
   * Use an editor that can preview Markdown, like VS Code
   * Try more Markdown syntax:
     [markdownguide.org/basic-syntax](https://markdownguide.org/basic-syntax/)
2. **Prepare for the next tutorial on remote repos**
   * Create an account on [github.com](https://github.com/)
   * Add an SSH key to your account: [docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
   * If you have any issues, please contact the instructor well ahead
     of the next lesson!

</div>
