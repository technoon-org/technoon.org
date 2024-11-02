---
title: GitNoon Lesson 1 - Tutorial
---

In this tutorial, you will learn how to use Git to track versions of
your files in a personal project:

1. Configure Git on your machine
2. Create your first Git repository (aka repo)
3. Track file changes
4. Revert to a previous version


## Configuring Git

* Before we start using Git, we're going to set a few important
  configuration options.
* Open your terminal ("Git Bash" on Windows) and run each of the
  following configuration commands
* **For anyone new to using the command-line:** type out one line at a
  time, then press the enter key to run the command

**Set the name and email address that will be associated with your changes:**

```
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Use the nano command-line text editor (which we will use in this course):**

```
git config --global core.editor nano
```

**Use `main` as the name of the default branch (for consistency across versions of Git):**

```
git config --global init.defaultBranch main
```

**Use native line-endings locally, but commit UNIX-style line-endings:**

```
# For Linux or macOS:
git config --global core.autocrlf input
# For Windows:
git config --global core.autocrlf true
```

**If you're behind a corporate proxy on Windows, tell Git to use the Windows certificate store:**

```
git config --global http.sslBackend schannel
```

> NOTE: All of these settings will be stored in a `.gitconfig` file in
> your user's home directory.


## Creating a Git repository

Let's create a **Git repository (aka repo)** to track entries in a
personal blog.

A Git repo is just a directory of files we are tracking with Git, so
let's start by creating a directory:

```
mkdir blog
```

* You may like to open your file explorer to see the files we are
  creating.
* `blog/` should be in the Home directory that opens by default in
  your operating system's file explorer.
* On Windows, you can run `explorer .` to open Explorer to the current
  directory.

Now change into the `blog/` directory, and list its contents:

```
cd blog
ls -la
```

* There's nothing in the `blog/` directory yet except for the
  standard pointers to the current directory (`.`) and the parent
  directory (`..`)

Now let's initialise the `blog/` directory as a Git repo:

```
git init
```

Now list the contents again:

> TIP: If you want to repeat a command at the command-line, you can
> browse recent commands with the up and down arrow keys.

```
ls -la
```

* You'll see a new `.git/` sub-directory
* Because it starts with `.`, it will be "hidden" by default in file
  explorers on Linux and macOS
* This is where Git will store past versions and all other data about
  the repo - **so don't delete it!**
* Any time you run a Git command, Git will look for a `.git/`
  directory inside the current directory or any of its parent
  directories

Now let's check that status of the repo:

```
git status
```

* You're going to get used to running `git status` a lot to see Git's
  view of your files.
* You should be on a branch called **main** - we'll talk about
  branches in a future lesson.
* There are no **commits (aka versions)** yet - we'll fix that now!


## Committing a new file

Now let's add a first entry into your blog. Open a new file called
`entry_1.md` in the `nano` text editor:

> TIP: You could use any text editor to create this file, but we'll
> use nano so that attendees on different operating systems will have
> the same experience.

```
nano entry_1.md
```

* The `.md` extension indicates this file a Markdown file - a plain
  text format with simple markup to indicate formatting.
* Let's enter a heading and a simple entry:
* Using `nano`:
  * Type to enter text at the cursor
  * Use arrow keys to navigate the document
  * When you're finished:
    * Press `Ctrl + x` to exit (hinted at the bottom of the editor)
    * Type `y` to save your changes
    * Press `Enter` to confirm the filename

```
# Entry 1

This is my first blog entry!
```

Now check the status of your repository

```
git status
```

You should see your `entry_1.md`, and that it is currently untracked by Git.

Let's tell Git to track the file by *adding* it:

```
git add entry_1.md
```

Running Git status again, we can see that the file has been added to
the **staging area** of changes that are ready to be committed:

```
git status
```

Now let's create the first **commit (aka version)** of our blog repo:

```
git commit
```

* Git will drop you into a text editor
  * Because of our configuration earlier, this will be `nano`
* Enter a commit message to describe the change you have made:
  * `Add first blog entry`
* Then exit `nano` while saving changes:
  * `Ctrl + x`
  * `y`
  * `Enter`

Now check the status again (there should be no uncommitted changes):

```
git status
```

`git log` will show us a history of commits, so we can use it to see
our first commit:

```
git log
```

* Note that our commit has been recorded with:
  * The author
  * The date/time
  * The commit message
  * A SHA hash that uniquely identifies this commit


## Modifying a file

Now let's modify our blog entry:

```
nano entry_1.md
```

> TIP: If you don't want to type out the entire filename, try typing
> `ent` and then pressing `TAB` to auto-complete it.

Replace the `This is my first blog entry!` with:

```
I've just learned how to commit changes in Git!
```

Save and exit, then check `git status`:

```
git status
```

Git sees that we've modified our file, and it can tell us what has
changed:

```
git diff
```

* The output of `git diff` includes:
  * The path to each file that has changed
  * Each contiguous "hunk" that has changed
  * Red lines starting with `-` have been removed by your changes
  * Green lines starting with `+` have been added by your changes

Now let's stage our changes for commit:

```
git add entry_1.md
git status
```

It is prudent to check the "diff" of staged changes before we commit
them:

```
git diff --staged
```

Now commit a new version, use a message with `Update first entry with
more detail`:

```
git commit
```

Check the status and log:

```
git status
git log
```

We can also see what changed in each commit:

```
git log -p
```


## Undoing uncommitted changes

Once a version has been committed, we can always restore that previous
version. This gives us confidence to make radical (and potentially
breaking) changes to our files without worrying about losing a
good/working version.

Let's say we accidentally deleted our blog entry:

```
rm entry_1.md
```

We can see that Git notices it's deletion:

```
git status
```

And `git status` even reminds us how to undo that deletion, by
**restoring** the file to whatever content it had in the last commit:

```
git restore entry_1.md
```

Now let's check the file has been restored by printing its contents
and checking Git status:

```
cat entry_1.md
git status
```

You can also restore the full contents of any previous commit from the
log by:

1. Specifying its unique SHA as the source
   * We only need to specify enough of the SHA to uniquely identify it
     in the repository.
2. Specifying `.` to target the entire current directory

```
git log
git restore --source=<USE SHA FROM OLDEST COMMIT IN LOG> .
```

We now have the old version's content as uncommitted changes on top of
the latest commit:

```
cat entry_1.md
git status
git diff
```

* You will need to add and commit the restored content like any other
  changes.
* Here we'll add all files at once using `.`
  * You should only do this when you're sure you want to add all files
  * It's best to consider carefully which files to include in a
    commit, and consider breaking up unrelated file changes into
    multiple commits.
  * To help us consider what we want to add, we'll use `--patch` to
    have Git ask us about whether to add each changed "hunk".

```
git add --patch .
git commit
# Commit message: Restore initial version of first entry
git log
```

**IMPORTANT:** You should always be careful running `git restore`, as
it might wipe out uncommitted changes.

* If you want to "undo" the changes of a specific commit, you can use
  `git revert` to automatically add a new commit that is the exact
  opposite of that commit.
* Let's revert that latest commit - we can use `HEAD` as a for the
  most recent commit.

```
git revert HEAD
```

Let's look at a log of the commits, and here use the `--patch` option
to see what changed in each:

```
git log --patch
```

Having lots of commits changing the content back and forth like this
is a bit silly, but **it illustrates how we typically undo work in Git
by *adding new commits* that restore older content or revert earlier
commits.**


## Conclusion

* You have now learned how to track versions of your files in a
  personal project
* In the next lesson, you'll learn how to use git **remotes** to share
  your repo with others.
* In future lessons, we'll learn more of Git's tools for collaborating
  with others.
