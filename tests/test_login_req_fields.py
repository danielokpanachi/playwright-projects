import re
from playwright.sync_api import Page, expect
import pytest


def get_json_data() -> list:
    import json
    with open("./test_data/data.json") as jsonfile:
        data = json.load(jsonfile)
    return[(item['username'], item['password'])  for item in data]
   


@pytest.mark.parametrize("username,password",
    [
    ("",""),
    ("","admin123"),
    ("Admin",""),                                                                                  
    
    ])  
      
        
def test_login_req_fields(page: Page,username,password) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill(username)
    
    
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(password)
    
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Required")).to_be_visible()
    