from get_essay_href import get_essay_url
from get_essay_content import get_essay_content

if __name__ == '__main__':
    href_list = get_essay_url()
    get_essay_content(href_list)

