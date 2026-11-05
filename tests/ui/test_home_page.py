def test_home_page(home_page):
  title = home_page.get_title()
  assert title == "Guru99 Telecom"