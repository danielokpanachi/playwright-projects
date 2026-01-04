import re
from playwright.sync_api import Page, expect
import pytest

        
def test_auth_session(page: Page) -> None:
   
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    
    
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    
    page.get_by_role("button", name="Login").click()
    
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    
    page.get_by_role("listitem").filter(has_text="Mironov Farrell").locator("i").click()
    
    expect(page.get_by_role("menuitem", name="Logout")).to_be_visible()
    page.get_by_role("menuitem", name="Logout").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    expect(page.get_by_role("heading")).to_contain_text("Login")
    
    
    
  