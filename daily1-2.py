total_post = int(input('게시글의 총 갯수를 입력하세요: '))
one_page_post = int(input('한 페이지에 필요한 게시글 수를 입력하세요: '))

total_page = int(total_post / one_page_post)
print(total_page)