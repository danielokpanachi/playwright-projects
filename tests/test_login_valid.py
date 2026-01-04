import re
from playwright.sync_api import Page, expect
import pytest

      
        
def test_login_valid(page: Page,) -> None:
   
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    
    page.wait_for_timeout(3000)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    page.get_by_role("button", name="Login").click()
   
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()