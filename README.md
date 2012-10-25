Test case for a bug in [webassets][]: If you have multiple handlebars templates
in a single `Bundle`, the first time they compile correctly. However, changing
just one of the templates in the bundle causes the bundle to be regenerated
with only the changed template. Steps to reproduce:

0. Create virtualenv and `pip install -r requirements.txt`
1. `./manage runserver`
2. Navigate to http://localhost:12345/; you should see a list of two templates
   ("a" and "b").
3. Append some text to `static/a.handlebars` to invalidate webassets's cache.
4. Refresh your browser; you'll now see just the "a" template.

The workaround is to disable the webassets cache for the given bundle, which
can be accomplished simply by adding a `depends` keyword argument.

[webassets]: https://github.com/miracle2k/webassets
