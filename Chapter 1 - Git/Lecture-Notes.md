# CHAPTER 1 - GIT

## Git Clone

We can run git clone in order to take a repository from the internet and download it onto our own computer

    git clone <url>

## Git Add

Tells Git that I would like to add a file as one to track the next time I save, the next time I make a commit to say that I would like to take a snapshot of all these files, such that I'm able to refer back to them later.

    git add <filename>

## Git Commit

Tells Git repository that I would like to save a snapshot of the current state of the repository, keeping track of any of the changes that have been made to the files that I have added using git add

    git commit -m "message"

With all these steps I am making changes only into my local copy of the repository, I still didn't put anything on the online repository which holds the "official" version of the repository.

## Git Status

It tells the status of my local repository against the online repository, saying for example if I commited files but still didn't put them online, my local repository will be "ahead" by 1 commit from the branch online.

## Git Push

Says that now, whatever changes I've made, when I run

    git push

those changes get pushed (published) up to GitHub.

## Git Pull

Will say take the changes that currently exist on GitHub, and go ahead and pull the most recent changes down, so that I in my local version of the repository have access to the latest version of all of the code that is currently on GitHub.

## Merge Conflicts

This conflicts happens when you try to merge the changes with someone else's changes, there are two different set of changes, that you will need to solve manually and then commit the results.

In this case, Git will add some sort of metadata to the file in order to describe the things that it can't figure out by itself. This will divide in two pieces

    somecode
    <<<< HEAD
    YOUR CHANGES
    ============
    REMOTE CHANGES
    >>>>> ID of the remote commit of the conflict

    somecode

Firstly we will need to erase all of the conflict markers and decide what we want as the resolution of the conflict.

## Git Log

Usefil if you ever need to keep track of all of the changes you have made to your code, you want to keep track of all of the commits that have been made in a particular repository.

    git log

Git will respond with a meesage that brings out a list of all of the IDs, Authors, Dates and Messages of all of the commits made.

## Git Reset

Will take the current state of the repository, and revert it back to an older state of the respository. There are a couple of ways to use it.

    git reset --hard <commit>

This will revert to the commit referenced.

    git reset --hard origin/master

This will revert the repository to the current online version in GitHub.

## Branching

Branches are Git's way of working on different parts of the repository at the same time.

Each branch will have a name:

- master: Is the default branch of the repository. It will generally contain the most up to date stable version of the code.

- other branches: To work on newer features, make some testings, etc.

The HEAD, is the pointer that tells you which branch you are looking at. So you could check out to a different branch anytime you want.

At the time you are happy with the new feature, bug fixes or whatever made you create a new branch, you can merch some or all of them together, to set the master new up to date stable version of the application.

## Forking Repositories

By forking, you are making your own copy of an original repository into your own GitHub account.

If you do fork a repository in your own account, and want to push the changes to the original account's repository, you can make a **pull request**, that you are requesting that your code be pulled in the original code of the original repository, so the people that mantain that original code can review and add are feedback, so when they are satisfied, they can merge those changes with their code.

This is one of the key benefits of open source code, that the community is able to collaborate with an existant repository.

## GitHub Pages

This is a feature of GitHub, that allows anyone with a GitHub account to store an online web page benefiting from the features of GitHub for free.
