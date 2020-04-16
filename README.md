# Braindead
Braindead is a braindead simple static site generator for minimalists, that has support for markdown and code highlighting.
I created this package simply to have a bit of fun and because I'm tired of bloated software.

You can read more about the idea behind it on [medium](https://medium.com/thirty3hq/how-i-created-my-blogging-system-in-less-than-100-lines-of-code-to-save-the-environment-dd848cc29c02) or [my blog](https://grski.pl/posts/python/creating-braindead.html)

Can't we just have [simple software nowadays](https://tonsky.me/blog/disenchantment/) that does what it needs to do and nothing more?
Existing solutions felt like they are too much for my needs. So I built this thing. It's still under active development.

Live example: [grski.pl](https://grski.pl/)

One of my main ideals here is to create template that is as fast as it gets. Generated pages take around 10-15 KB in total.
No JavaScript used here, at least in the base template. Just css/html.

You are free to change that though by creating your own templates. More on that below.

Benefits of simple approach:

![Google PageSpeed Insights withh 100 score](https://imgur.com/7IwldRE.png)
![requests made if loading this template](https://imgur.com/GmYcP08.png)
 
Default template scores 100/100 on Google PageSpeed Insights and has very fast load times.

Default template design looks like this:

![Default template of braindead](https://imgur.com/oPdgdvW.png)
It's based on: [Kiss template](https://github.com/ribice), slightly modified - with minimized styles. In the future I'll probably slim them down even more.

It's also eco friendly - it uses less power by not being a bloatware. [CarbonReport of the demo](https://www.websitecarbon.com/website/grski-pl/)
![Carbon report of the grski.pl blog](https://imgur.com/cfQJqQgl.png)
# Installation
```
pip install braindead
```
[PyPi page](https://pypi.org/project/braindead/)

# Usage
Create `index.md` and run `braindead` that's it. You'll find your generated site in `dist` directory.
It can be empty or not - your choice. If you want index  to contain just the posts - leave it empty.

That's the minimal setup you need. That'll generate index.html for you, but well, it's not enough, right?
More robust structure you can use is:
```bash
pages/
  page.md
posts/
  post.md
index.md
site.toml
```

The url for generated html will be `{DIR_LOCATION}/{FILENAME}.html`,
 so url generated will be `{site.base_url}/{DIR_LOCATION}/{FILENAME}.html` in order to change that, add
```markdown
Slug: custom-location
```
To your post/page header - then the location will be `{BASE_URL}/{SLUG}.html`

## Example post/page structure:

```markdown
Title: Title of the post or of the page 
Date: 2018-03-22
Authors: Olaf Górski
Description: Description of the post/page. If not provided it'll default to first 140 chars of the content. 

CONTENT GOES HERE...
```

All of the metadata used here will be available during given page rendering. You can add more keys and metadata if you'd like. 

## Config

All of the variables that are used to generate the page can be overwritten by creating `pyproject.toml` file, but it's not required to get started.
Example of your `pyproject` `tool.braindead.site` section (these are also the defaults):

```toml
[tool.braindead.site]
base_url = "" # give full url ending with slash here - eg. if you host your blog on https://grski.pl/ enter it there.
author = "Olaf Górski"  # author/owner of the site <- will be appended to the title
title = "Site generated with braindead"  # base title of the website
description = "Just a description of site generated in braindead"  # description used in the meta tags
content = ""  # this will display under heading
name = "braindeadsite" # og tags
logo = "logo_url"  # url to the logo for og tags
heading = "Braindead Example"  # heading at the top of the site
github = "https://github.com/grski"  # link to your github
linkedin = "https://linkedin.com/in/olafgorski"  # link to your li
copy_text = "Olaf Górski"  # copy text in the footer
copy_link = "https://grski.pl"  # and copy link of the footer
language = "en"  # default language set in the top level html lang property
```

None of these are required. You can overwrite none, one or more. Your choice.

# Code higlighting
Just do
<pre>
```python
Your code here
```</pre>

[List of languages supported by pygments can be found here.](https://pygments.org/languages/)

# Creating your own templates
TODO

# Technology
This bases on 
[toml](https://github.com/uiri/toml), 
[markdown](https://github.com/Python-Markdown/markdown) and [jinja2](https://github.com/pallets/jinja).

Toml is used for configuration.
Markdown to render all the .md and .markdows into proper html.
Lastly jinja2 to add some contexts here and there.

Formatting of the code is done using [black](https://github.com/psf/black), [isort](https://github.com/timothycrosley/isort).
[flake8](https://gitlab.com/pycqa/flake8), [autoflake](https://github.com/myint/autoflake) and [bandit](https://github.com/PyCQA/bandit/) to check for potential vulns. 

Versioning is done with [bumpversion](https://github.com/peritus/bumpversion).
Patch for merges to develop, minor for merged to master. Merge to master means release to pypi.

And wonderful [poetry](https://github.com/python-poetry/poetry) as dependency manager. BTW pipenv should die.

Code highligthing is done with [pygments](https://github.com/pygments/pygments).

I use type hinting where it's possible.

To start developing you need to install poetry
`pip install poetry==0.1.0` and then just `poetry install`. 

# Known make commands
```bash
flake
isort
isort-inplace
bandit
black
linters
bumpversion
black-inplace
autoflake-inplace
format-inplace
```
Most important ones are `make linters` and `make format-inplace`. Before each commit it's required to run these checks.

# License
MIT


