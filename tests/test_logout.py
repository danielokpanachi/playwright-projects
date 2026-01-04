import re
from playwright.sync_api import Page, expect
import pytest

        
def test_logout(page: Page) -> None:
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    
    page.get_by_role("button", name="Login").click()
    
    page.get_by_role("listitem").filter(has_text="Mironov user").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_role("heading", name="Login")).to_be_visible()
    

    
    