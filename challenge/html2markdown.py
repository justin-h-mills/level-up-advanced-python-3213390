import re

def html2markdown(html: str):
    '''Take in html text as input and return markdown'''
    
    # replace italics
    markdown = re.sub(r'<em>(.*?)</em>', r'*\1*', html)

    # replace consecutive spaces or line breaks with a single space
    markdown = re.sub(r'\s+', ' ', markdown)

    # replace paragraphs with 2 line breaks
    markdown = re.sub(r'<p>(.*?)</p>', r'\1\n\n', markdown)

    # convert html links to markdown format
    markdown = re.sub(r'<a\s+href=[\'"](.*?)[\'"].*?>(.*?)</a>', r'[\2](\1)', markdown)

    return markdown.strip()