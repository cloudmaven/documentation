---
title: GitHub for Research Computing
keywords: azure, procedural
last_updated: October 6, 2016
tags: [GitHub]
summary: "A set of commands and context for using GitHub in research"
sidebar: mydoc_sidebar
permalink: rc_github.html
folder: mydoc
---

# GitHub for Research Computing

## Introduction

The purpose of this page is to walk through GitHub procedures with two implementations in mind: 

1. A Jekyll implementation (e.g. http://cloudmaven.org) that renders markdown (.md) properly. 
2. A Jupyter Notebook: Both static rendering and as a backup of a dynamic instance.

Using a code repository (distinguish: not a data repository) like GitHub accomplishes: 

- You have a safe back-up of your code base
- You can work on your code with others simultaneously, managing versions
- You can take advantage of interpreters like Jekyll that build documentation pages
- You can maintain versions of your code for development, testing and deployment (use)


## Links
[GitHub](http://github.com)


break 1




## Warnings
- For a Jekyll instance such as [this website](http://cloudmaven.org): Work from the gh-pages branch, not the master. 
  - You risk 'breaking' your GitHub implementation if you work on the wrong branch.
- If GitHub is balking (throwing fail/error messages): Use 'git status' on the command line and diagnose the output. 
  - For example a 'rebase' in progress (unresolved) can be halted using 'git rebase abort' but be sure you know what you are doing. 
  - Once 'git status' is ok you can return to business as usual. 
- GitHub can sometimes be mysterious. When in doubt: Make an independent local copy of the repo folder first.
- While Jekyll renders markdown there does not appear to be a reliably good way of rendering LaTeX. 
  - In research this is important. Until there is a fix we are obliged to render to pngs and embed them as images.

## What is Jekyll?
Jekyll is a GitHub repo that includes rendering software 'for itself'. That is: If you make a copy of the Jekyll repo and rename it something else, 
like 'Hyde', it will be visible on GitHub as both a normal repo (let's call that the back door) and as a rendered website (the front door). The 
way this works is your version will start out with some default files that have the markdown file extension '.md'. These you can modify to suit 
your own purposes. When you hit the front door Jekyll manually creates from these markdown files some pretty html content which renders in your 
browser. Follow the recipe provided by the Jekyll documentation and you can start building out content in Hyde. This is what we have done 
with http://cloudmaven.org. 

Notice that there is a side comment (Kilroy) needed here about the distinction between the front door URL and the DNS entry. 
  
## GitHub Commit from Command Line on Windows
This assumes you already have a GitHub repo and a local copy. You have modified something in the local copy and you have permission to just execute a 
push that will override anything on the GitHub repo.  

- Start the Power Shell on a Windows machine connected to the internet.
- Navigate to the base directory of the repository.
- Issue these in sequence; note I have paraphrased what they do
  - git status                             state the current status of the local repository
    - Is there a 'rebase' in the response? You may need to issue 'git rebase abort' but be sure this is safe to do 
  - git pull                               update my copy of the repo from GitHub to latest
  - git add .                              stage everything new recursively (this folder on down) for a commit
  - git commit -m "a comment"              creates a 'commit' of the current state of the local repo
  - git push origin master                 update the GitHub repo based on mine
    - This push may require login information: login name and password




{% include links.html %}
