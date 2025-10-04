---
title: GitNoon Lesson 4
---

In this tutorial, you will learn how to:

1. Make a pull request
2. Rebase a pull request
3. Complete a pull request


## Making sure our `main` branch is clean

Before we get started, let's make sure we're all on the `main` branch:

```
git switch main
```

And make sure we have a clean status (**warning:** this will get rid
of any unpushed commits or uncommitted changes):

```
git fetch
git reset --hard origin/main
```


## Setting up a branch for a pull request

Now let's get started on a pull request where we'll be adding a guide
for contributors to our repo.

First, make a new branch and switch to it:

```
git branch contributing-guide
git switch contributing-guide
```

Now open a `CONTRIBUTING.md`:

```
nano CONTRIBUTING.md
```

Enter the following content:

```
* Pull requests are welcome!
```

Save and exit `nano` (`Ctrl + x`, `y`, `Enter`), then add and commit
`CONTRIBUTING.md`:

```
git status
git add CONTRIBUTING.md
git status
# We'll use a shortcut to write the message inline
git commit -m "Add contributing guide"
git status
```

You should now see `contributing-guide` one commit ahead of `main`:

```
git graph
```

* (press `q` to exit `git graph`)


## Making a pull request

* Many teams will use a **pull request** (also know as a **merge
  request**) to manage the merging of a feature branch back into the
  `main` branch.
* We'll do that ourselves now.

First, let's push the `contributing-guide` branch to the `origin`
remote:

```
git push -u origin contributing-guide
```

* `-u` is only needed the first time you push a particular branch

Now open your repo's page on GitHub, you'll see various shortcuts to
create a pull request for your newly pushed branch, but let's do it
the standard way:

1. Open the `Pull requests` tab
2. Select `New pull request`
3. Choose `main` for the **base** branch
4. Choose `contributing-guide` for the **compare** branch
   * You'll see a summary showing the commit to be merged in from
     `contributing-guide`, along with a diff of the changes
5. Select `Create pull request`
6. You can fill in some details for the pull request:
   * Change the title and description if more context is needed
   * If you were in a team, you could add a reviewer
7. Finally, click `Create pull request`

* Because there are no merge conflicts, GitHub will say the branch is
  ready to merge.
* Normally, this would be the point for someone else to review and
  merge your pull request.


## Creating a merge conflict with your pull request

Now let's see what happens if someone updates `main` and causes a
merge conflict between your pull request branch and `main`.

Let's switch back to `main`:

```
git switch main
```

And add a `CONTRIBUTING.md` on this branch

```
nano CONTRIBUTING.md
```

Give it some **different** content:

```
* Please rebase conflicting pull requests
```

Save and exit `nano` (`Ctrl + x`, `y`, `Enter`), then add and commit
`CONTRIBUTING.md`:

```
git status
git add CONTRIBUTING.md
git status
# We'll use a shortcut to write the message inline
git commit -m "Remind contributors to rebase"
git status
```

Now push the new commit on `main` to the `origin` remote:

```
git push origin main
```

And see that the two branches have now diverged, both locally and on
`origin`:

```
git graph
```


## Rebasing the pull request

Look at your pull request on GitHub, and you'll see that it can no
longer be merged because of a *merge conflict*.

Let's resolve the conflict by rebasing your pull request branch on top
of `main`, which is the standard approach used by most teams and
open-source projects:

First, switch back to your pull request branch:

```
git switch contributing-guide
```

Before rebasing onto `main`, it's important to make sure you have
fetched all of the commits on it:

```
git fetch
```

Now rebase onto `origin/main` to update our current branch, just as we
would if we were merging:

```
git rebase origin/main
```

* Rebasing onto `origin/main` is safer than rebasing onto the local
  `main` because we might forget to make sure `main` is up to date
  with `origin/main`

If you've done this correctly, you should see a conflict!

Let's check the details:

```
git status
git diff
```

* Just like a merge, if you ever reach this point and don't want to
  handle the conflicts right now, you can just run `git rebase --abort`

Just like last lesson, we need to manually resolve the conflict by
editing `CONTRIBUTING.md`

```
nano CONTRIBUTING.md
```

Edit it to contain **both** lines and **nothing else**:

```
* Please rebase conflicting pull requests
* Pull requests are welcome!
```

Git diff shows the resolution we have made:

```
git diff
```

To finish the rebase, we need to add the resolution:

```
git add CONTRIBUTING.md
git status
```

And finally, tell Git to commit the resolution, and continue rebasing
any more commits in the rebased branch:

```
git rebase --continue
```

* We will be prompted to re-confirm the commit message for the
  replayed commit that we had to resolve the conflict in.
  * Just save and exit to confirm the message (`Ctrl + x`, `y`, `Enter`)
* In this case, there are no more commits to replay, so the rebase is
  complete!

Let's see what that's done to the repo:

```
git graph
```

* You should see two `Add contributing guide` commits:
  * The first is the old commit that `origin/contributing-guide` still
    points to
  * The other is the rebased commit that the local
    `contributing-guide` now points to
    * See that it is based on the top of `origin/main`
* Notice that both of the commits have a different SHA!

What happens if we try and push our branch:

```
git push origin contributing-guide
```

* Git stops us, because pushing the current state of our local branch
  would remove the *old* commits from the remote.

Because we do actually want to get rid of the old commits, we can
destructively update the remote with a **force push**:

```
git push --force origin contributing-guide
```

* **Important:** You should always double-check which commits will be
  lost by fetching and checking `git graph` before force pushing.

Now that the push has succeeded, `origin/contributing-guide` will be
on the same commit as your local branch, and you should no longer see
the old commit in the graph:

```
git graph
```


## Completing the pull request

Now that the merge conflict has been resolved, we can complete the
pull request.

1. Open your pull request on GitHub
2. Select `Merge pull request`
3. Then select `Confirm merge`

Now let's fetch the results of that merge from the `origin` remote to
our local repo:

```
git fetch
git graph
```

* We can see `origin/main` contains a new merge commit
* Even though a fast-forward merge was possible, a pull request will
  always create a merge commit by default
  * This is good, as it keeps a log of significant merges into `main`

You'll now need to switch back to your main branch and "fast-forward"
merge it to the latest state of `origin/main` - just like we did last
week:

```
git switch main
git merge --ff-only origin/main
```

Now you can understand why we use the "fast-forward only" option:

* If there were local commits that weren't in the remote branch, then
  we'd want to stop and think about what to do next, probably either
  merging or rebasing

Finally, now that our branch is merged, we should tidy-up by deleting
our feature branch on the remote and locally:

```
# Delete the remote branch
git push -d origin contributing-guide
# Delete the local branch
git branch -d contributing-guide
```

Finally, a last look at the graph will show that we have removed the
branch, and are just left with `main`:

```
git graph
```


## Conclusion

* You've now learned how to:
  * Work on a feature branch
  * Make a pull request for it
  * Rebase the pull request to resolve conflicts
  * Complete the pull request
* This is the standard approach for working on many projects,
  including open-source projects, so you're all set to contribute to a
  whole world of Git repos!
