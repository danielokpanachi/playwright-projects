import re
from playwright.sync_api import Page, expect
import pytest

def get_csv_data() -> list:
    import csv
    data = []
    with open("/Users/danze/Desktop/playwright-projects/test_data/data.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data    

def get_json_data() -> list:
    import json
    with open("/Users/danze/Desktop/playwright-projects/test_data/data.json") as jsonfile:
        data = json.load(jsonfile)
    return[(item['username'], item['password'])  for item in data]
    


@pytest.mark.parametrize("username,password", get_csv_data())  
      
        
def test_datadriven(page: Page,username,password) -> None:
   
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill(username)
    

    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(password)
    
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    page.get_by_role("button", name="Login").click()
   
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
   
    
   
    expect(page.get_by_role("heading")).to_contain_text("Dashboard")
    page.get_by_role("link", name="Buzz").click()
    expect(page.locator("#app")).to_contain_text("Buzz Newsfeed")
    page.get_by_role("link", name="Dashboard").click()
    
    
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    
    
    page.get_by_role("listitem").filter(has_text="manda user").locator("i").click()
    expect(page.get_by_role("menuitem", name="Logout")).to_be_visible()
    page.get_by_role("menuitem", name="Logout").click()
   
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    expect(page.get_by_role("heading")).to_contain_text("Login")
    
    
    
   
