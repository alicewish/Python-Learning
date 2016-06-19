import markdown
from markdown.extensions import Extension

html = markdown.markdownFromFile('/Users/alicewish/Documents/美漫图源制作.md', extensions=['markdown.extensions.extra'])
print (html)