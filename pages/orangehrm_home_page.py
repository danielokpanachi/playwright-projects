from playwright.sync_api import Page,expect

class HomePage:
    
    def __init__(self, page:Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.admin_link = page.get_by_role("link", name="Admin")
        self.logout_menuitem = page.get_by_role("menuitem", name="Logout")  
        
    def click_admin_link(self):
        self.admin_link.click()
        
    def click_logout(self):
        self.logout_menuitem.click()    