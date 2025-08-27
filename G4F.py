from pdf_maker import pdf_maker
from imgs_downloader import imgs_downloader

if __name__ == "__main__":
    total_pages = imgs_downloader()
    pdf_maker(total_pages)
